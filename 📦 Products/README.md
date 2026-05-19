# 📦 Products Directory

Product strategy, ICPs, ROI frameworks, and feature specifications.

## Structure

Each product you own gets its own subdirectory. **Do not commit predefined product names** — start from `_template/`:

```
📦 Products/
├── _template/              # Copy → rename to your product slug
│   ├── README.md
│   ├── context.md
│   └── initiatives/        # Feature specs and PRDs
└── <your-product-slug>/    # e.g. after /onboard or manual copy
    ├── README.md
    ├── ICP.md              # Optional
    ├── ROI-framework.md    # Optional
    ├── competitive/        # Optional
    ├── designs/            # Optional
    └── initiatives/
```

**Setup:** `cp -R "📦 Products/_template" "📦 Products/[your-product-slug]"` then replace `[FILL IN]` placeholders.

## Usage

- Update product strategy quarterly
- Add feature specs to `initiatives/` subdirectory
- Keep ICP current with customer research
