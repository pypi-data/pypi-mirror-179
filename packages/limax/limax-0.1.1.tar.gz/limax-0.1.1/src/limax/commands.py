"""Definition of command line commands.

Upload study or studies, delete studies and upload available info nodes.
This commands are available after installation.
"""
import argparse
from pathlib import Path

from pymetadata import log
from pymetadata.console import console

from limax import __citation__, __version__
from limax.io import read_limax_csv


logger = log.get_logger(__name__)


def main() -> None:
    """Entry point which runs LiMAx script.

    The script is registered as `limax` command.

    Example:
        limax --i src/limax/resources/limax_example.csv --o src/limax/resources/limax_example_processed.csv
    """

    import optparse
    import sys

    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--input",
        action="store",
        dest="input_path",
        help="Path to LiMAx raw file.",
    )
    parser.add_option(
        "-o",
        "--output",
        action="store",
        dest="output_path",
        help="Path to processed LiMAx file (without patient data) as '*.csv'.",
    )

    console.rule(style="white")
    console.print(":syringe: LIMAX ANALYSIS :syringe:")
    console.print(f"Version {__version__} (https://github.com/matthiaskoenig/limax)")
    console.print(f"Citation {__citation__}")
    console.rule(style="white")

    options, args = parser.parse_args()

    def _parser_message(text: str) -> None:
        console.print(text)
        parser.print_help()
        console.rule(style="white")
        sys.exit(1)

    if not options.input_path:
        _parser_message("Required argument '--input' missing")
    if not options.output_path:
        _parser_message("Required argument '--output' missing")

    input_path = Path(options.input_path)
    if not input_path.exists():
        _parser_message(
            f"--input '{options.input_path}' does not exist, ensure valid LiMAx raw "
            f"file."
        )

    output_path = Path(options.output_path)
    if not str(output_path).endswith(".csv"):
        _parser_message(
            f"--output '{options.input_path}' output path must end in '.csv'"
        )

    read_limax_csv(limax_csv=input_path, output_path=output_path)


if __name__ == "__main__":
    main()
