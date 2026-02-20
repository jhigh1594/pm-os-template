"""Abstract base class for all data collectors."""

import logging
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger(__name__)


class BaseCollector(ABC):
    """Abstract base for all data collectors."""

    @abstractmethod
    async def collect(self) -> Any:
        """Collect data from source.

        Returns:
            Collected data in workflow-specific format.
            Must include an "errors" key for graceful degradation.
        """
        pass

    def is_available(self) -> bool:
        """Check if source is available.

        Returns:
            True if collector can be used, False otherwise.
        """
        return True
