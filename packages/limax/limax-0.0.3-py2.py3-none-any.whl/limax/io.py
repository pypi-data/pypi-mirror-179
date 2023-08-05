"""
Reading data from RAW Limax files.

Anonymization.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def read_metadata(str: str) -> None:
    """Read LiMAx metadata."""
    pass


def read_data(str: str) -> None:
    """Read LiMAx data."""
    pass


def read_limax_csv(limax_csv: Path, line_offset: int = 13) -> pd.DataFrame:
    """Read limax data."""
    with open(limax_csv, "r") as f:
        lines: List[str] = f.readlines()
        # remove empty lines
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if len(line) > 0]
        # strip header lines
        time, dob, error = [], [], []
        for line in lines[line_offset:]:
            tokens = [t.strip() for t in line.split("\t")]
            time.append(int(tokens[0]))
            dob.append(float(tokens[1]))
            error.append(str(tokens[2]))

    d: Dict[str, Any] = {
        "time": time,
        "dob": dob,
        "error": error,
    }
    df = pd.DataFrame(data=d)
    df = df[["time", "dob", "error"]]
    # make columns numeric
    # df = pd.to_numeric(df)
    # print(df.head())

    # sort by time (some strange artefacts in some files)
    df.sort_values(by=["time"], inplace=True)
    return df


if __name__ == "__main__":
    from limax import EXAMPLE_LIMAX_PATH

    df = read_limax_csv(EXAMPLE_LIMAX_PATH)

    print(df)
