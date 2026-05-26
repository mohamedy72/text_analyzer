"""
A helper function that read and load text files from CLI
"""

from pathlib import Path


def read_file(filepath: str):
    p = Path(filepath)
    print(f"📖 Reading your file..., {p}")

    # Check if the file is actually a txt file
    if p.suffix == ".txt":
        with open(filepath, "r") as f:
            contents = f.read()
    else:
        return f"The file format is not correct {p.suffix}. Please provide txt file"

    # Check if file is empty
    if len(contents) == 0:
        return f"Your file is probably empty: It contains {len(contents)} character"

    return contents
