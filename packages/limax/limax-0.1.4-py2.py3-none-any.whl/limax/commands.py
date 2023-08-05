"""Definition of command line commands for limax."""
import argparse
from pathlib import Path

from pymetadata import log
from pymetadata.console import console

from limax import __citation__, __version__
from limax.io import read_limax_dir, read_limax_file


logger = log.get_logger(__name__)


def main() -> None:
    """Entry point which runs LiMAx script.

    The script is registered as `limax` command.

    Example (process single file):
        limax -i src/limax/resources/patient1.csv -o src/limax/resources/limax_example_processed.csv

    Example (process all limax file in folder):
        limax --input_dir src/limax/resources --output_dir src/limax/resources
    """

    import optparse
    import sys

    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--input",
        action="store",
        dest="input_path",
        help="Path to input LiMAx raw file.",
    )
    parser.add_option(
        "-o",
        "--output",
        action="store",
        dest="output_path",
        help="Path to output processed LiMAx file (without patient data) as '*.csv'.",
    )
    parser.add_option(
        "--input_dir",
        action="store",
        dest="input_dir_path",
        help="Path to input folder with LiMAx raw files as '*.csv'.",
    )
    parser.add_option(
        "--output_dir",
        action="store",
        dest="output_dir_path",
        help="Path to output folder with processed LiMAx files",
    )

    console.rule(style="white")
    console.print(":syringe: LIMAX ANALYSIS :syringe:")
    console.print(f"Version {__version__} (https://github.com/matthiaskoenig/limax)")
    console.print(f"Citation {__citation__}")
    console.rule(style="white")
    console.print("Example (single file):")
    console.print("    limax -i patient1.csv -o limax_example_processed.csv")
    console.print("Example (folder):")
    console.print(
        "    limax --input_dir limax_examples --output_dir limax_examples_processed"
    )
    console.rule(style="white")

    options, args = parser.parse_args()

    def _parser_message(text: str) -> None:
        console.print(text)
        parser.print_help()
        console.rule(style="white")
        sys.exit(1)

    if not options.input_path and not options.input_dir_path:
        _parser_message("Required argument '--input' or '--input_dir' missing")
    if not options.output_path and not options.output_dir_path:
        _parser_message("Required argument '--output' or '--output_dir' missing")
    if options.input_path and not options.output_path:
        _parser_message("If '--input' is provided '--output' is required")
    if options.input_dir_path and not options.output_dir_path:
        _parser_message("If '--input_dir' is provided '--output_dir' is required")

    # process single LiMAx
    if options.input_path and options.output_path:
        input_path = Path(options.input_path)
        output_path = Path(options.output_path)
        if not input_path.exists():
            _parser_message(f"'--input {input_path}' does not exist.")
        if not input_path.is_file():
            _parser_message(f"'--input {input_path}' is not a file.")
        read_limax_file(limax_csv=input_path, output_path=output_path)

    # process folder with LiMAx raw data
    elif options.input_dir_path and options.output_dir_path:
        input_dir_path = Path(options.input_dir_path)
        output_dir_path = Path(options.output_dir_path)
        if not input_dir_path.exists():
            _parser_message(f"'--input {input_dir_path}' does not exist.")
        if not input_dir_path.is_dir():
            _parser_message(f"'--input {input_dir_path}' is not a directory.")

        # process all files
        read_limax_dir(input_dir=input_dir_path, output_dir=output_dir_path)


if __name__ == "__main__":
    main()
