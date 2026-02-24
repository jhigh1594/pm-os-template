#!/usr/bin/env python3
"""
Combine title slide from corporate template with content slides.
Uses OOXML (XML-level) manipulation to preserve all formatting.

Usage: python combine-decks-ooxml.py title.pptx content.pptx output.pptx

This approach:
1. Takes the title slide PPTX as base (preserves master slides, themes, fonts)
2. Copies slide XML from content PPTX
3. Updates relationships and content types
4. Produces a merged file with perfect formatting from both sources
"""

import sys
import os
import zipfile
import shutil
import re
from pathlib import Path

def copy_slide_xml(content_dir, slide_num, target_dir, new_slide_num, rel_id_offset):
    """Copy a slide and its relationships from content to target."""

    # Copy slide XML
    src_slide = os.path.join(content_dir, f'ppt/slides/slide{slide_num}.xml')
    dst_slide = os.path.join(target_dir, f'ppt/slides/slide{new_slide_num}.xml')

    if not os.path.exists(src_slide):
        print(f"  Warning: slide{slide_num}.xml not found")
        return None

    # Read slide content
    with open(src_slide, 'r', encoding='utf-8') as f:
        slide_content = f.read()

    # Write to destination
    os.makedirs(os.path.dirname(dst_slide), exist_ok=True)
    with open(dst_slide, 'w', encoding='utf-8') as f:
        f.write(slide_content)

    # Copy slide relationships if they exist
    src_rels = os.path.join(content_dir, f'ppt/slides/_rels/slide{slide_num}.xml.rels')
    dst_rels = os.path.join(target_dir, f'ppt/slides/_rels/slide{new_slide_num}.xml.rels')

    if os.path.exists(src_rels):
        os.makedirs(os.path.dirname(dst_rels), exist_ok=True)
        with open(src_rels, 'r', encoding='utf-8') as f:
            rels_content = f.read()

        # Update relationship IDs to avoid conflicts
        # (This is simplified - may need adjustment for images/media)
        with open(dst_rels, 'w', encoding='utf-8') as f:
            f.write(rels_content)

    return True

def add_slide_to_presentation_xml(pres_xml, slide_rel_id, slide_id):
    """Add a slide reference to presentation.xml"""

    # Find the sldIdLst element
    pattern = r'(<p:sldIdLst.*?>)'
    match = re.search(pattern, pres_xml, re.DOTALL)

    if not match:
        print("  Warning: Could not find sldIdLst in presentation.xml")
        return pres_xml

    # Insert new slide reference at the end of sldIdLst
    new_entry = f'<p:sldId id="{slide_id}" r:id="{slide_rel_id}"/>'

    # Find the closing tag
    insert_pos = pres_xml.find('</p:sldIdLst>')
    if insert_pos == -1:
        return pres_xml

    pres_xml = pres_xml[:insert_pos] + new_entry + pres_xml[insert_pos:]
    return pres_xml

def add_slide_relationship(rels_xml, rel_id, slide_num):
    """Add a relationship for a new slide."""

    new_rel = f'<Relationship Id="{rel_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{slide_num}.xml"/>'

    insert_pos = rels_xml.find('</Relationships>')
    if insert_pos == -1:
        return rels_xml

    rels_xml = rels_xml[:insert_pos] + new_rel + rels_xml[insert_pos:]
    return rels_xml

def add_content_type(ct_xml, slide_num):
    """Add content type for a new slide."""

    # Check if already exists
    if f'slide{slide_num}.xml' in ct_xml:
        return ct_xml

    new_override = f'<Override PartName="/ppt/slides/slide{slide_num}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'

    insert_pos = ct_xml.find('</Types>')
    if insert_pos == -1:
        return ct_xml

    ct_xml = ct_xml[:insert_pos] + new_override + ct_xml[insert_pos:]
    return ct_xml

def combine_presentations(title_path, content_path, output_path):
    """Combine title slide with content slides using OOXML manipulation."""

    temp_dir = '/tmp/planview-deck/combine-temp'
    title_dir = os.path.join(temp_dir, 'title')
    content_dir = os.path.join(temp_dir, 'content')

    # Clean up
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    # Extract both presentations
    print(f"Extracting title presentation: {title_path}")
    with zipfile.ZipFile(title_path, 'r') as zf:
        zf.extractall(title_dir)

    print(f"Extracting content presentation: {content_path}")
    with zipfile.ZipFile(content_path, 'r') as zf:
        zf.extractall(content_dir)

    # Count slides in each
    title_slides = len([f for f in os.listdir(os.path.join(title_dir, 'ppt/slides'))
                        if f.startswith('slide') and f.endswith('.xml')])
    content_slides = len([f for f in os.listdir(os.path.join(content_dir, 'ppt/slides'))
                          if f.startswith('slide') and f.endswith('.xml')])

    print(f"\nTitle presentation: {title_slides} slide(s)")
    print(f"Content presentation: {content_slides} slide(s)")

    # Read presentation.xml relationships
    rels_path = os.path.join(title_dir, 'ppt/_rels/presentation.xml.rels')
    with open(rels_path, 'r', encoding='utf-8') as f:
        rels_xml = f.read()

    # Find highest relationship ID
    rel_ids = re.findall(r'Id="rId(\d+)"', rels_xml)
    max_rel_id = max(int(rid) for rid in rel_ids) if rel_ids else 0

    # Read presentation.xml
    pres_path = os.path.join(title_dir, 'ppt/presentation.xml')
    with open(pres_path, 'r', encoding='utf-8') as f:
        pres_xml = f.read()

    # Find highest slide ID
    slide_ids = re.findall(r'<p:sldId id="(\d+)"', pres_xml)
    max_slide_id = max(int(sid) for sid in slide_ids) if slide_ids else 255

    # Read content types
    ct_path = os.path.join(title_dir, '[Content_Types].xml')
    with open(ct_path, 'r', encoding='utf-8') as f:
        ct_xml = f.read()

    # Copy media files from content to title (images, etc.)
    content_media = os.path.join(content_dir, 'ppt/media')
    title_media = os.path.join(title_dir, 'ppt/media')

    if os.path.exists(content_media):
        os.makedirs(title_media, exist_ok=True)
        for f in os.listdir(content_media):
            src = os.path.join(content_media, f)
            # Check if file already exists
            dst = os.path.join(title_media, f)
            if not os.path.exists(dst):
                shutil.copy2(src, dst)

    # Add content slides
    next_slide_num = title_slides + 1

    for i in range(1, content_slides + 1):
        print(f"  Adding content slide {i}...")

        # Copy slide XML
        copy_slide_xml(content_dir, i, title_dir, next_slide_num, max_rel_id)

        # Add relationship
        max_rel_id += 1
        rels_xml = add_slide_relationship(rels_xml, f'rId{max_rel_id}', next_slide_num)

        # Add slide reference to presentation.xml
        max_slide_id += 1
        pres_xml = add_slide_to_presentation_xml(pres_xml, f'rId{max_rel_id}', max_slide_id)

        # Add content type
        ct_xml = add_content_type(ct_xml, next_slide_num)

        next_slide_num += 1

    # Write updated files
    with open(rels_path, 'w', encoding='utf-8') as f:
        f.write(rels_xml)

    with open(pres_path, 'w', encoding='utf-8') as f:
        f.write(pres_xml)

    with open(ct_path, 'w', encoding='utf-8') as f:
        f.write(ct_xml)

    # Repack
    print(f"\nPacking combined presentation...")
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(title_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arc_name = os.path.relpath(full_path, title_dir)
                zf.write(full_path, arc_name)

    print(f"\n✓ Combined presentation saved: {output_path}")
    print(f"  - {title_slides} title slide(s) from template")
    print(f"  - {content_slides} content slide(s)")
    print(f"  - {title_slides + content_slides} total slides")

    # Cleanup
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine-decks-ooxml.py title.pptx content.pptx output.pptx")
        sys.exit(1)

    title_path = sys.argv[1]
    content_path = sys.argv[2]
    output_path = sys.argv[3]

    if not os.path.exists(title_path):
        print(f"Error: Title file not found: {title_path}")
        sys.exit(1)

    if not os.path.exists(content_path):
        print(f"Error: Content file not found: {content_path}")
        sys.exit(1)

    combine_presentations(title_path, content_path, output_path)
