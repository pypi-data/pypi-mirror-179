"""limax - Python utilities for limax."""
from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "0.0.2"


program_name: str = "limax"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
EXAMPLE_LIMAX_PATH: Path = RESOURCES_DIR / "limax_example.csv"
