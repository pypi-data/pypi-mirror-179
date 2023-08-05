"""limax - Python utilities for limax."""
from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "0.1.4"
__citation__ = "https://doi.org/10.5281/zenodo.7382670"


program_name: str = "limax"

RESOURCES_DIR: Path = Path(__file__).parent / "resources"
RAW_DIR: Path = RESOURCES_DIR / "raw"
PROCESSED_DIR: Path = RESOURCES_DIR / "processed"
EXAMPLE_LIMAX_PATH: Path = RAW_DIR / "patient1.csv"
