"""limax - Python utilities for limax."""
from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "0.1.0"
__citation__ = "https://doi.org/10.5281/zenodo.3708271"


program_name: str = "limax"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
EXAMPLE_LIMAX_PATH: Path = RESOURCES_DIR / "limax_example.csv"
EXAMPLE_LIMAX_PROCESSED_PATH: Path = RESOURCES_DIR / "limax_example_processed.csv"
