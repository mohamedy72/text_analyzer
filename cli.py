from typing import Annotated
import typer


def analyze_text(
    filename: Annotated[
        str, typer.Argument(help="The name of the file to be anaylzed")
    ],
    stats: Annotated[bool, typer.Option(help="Display all stats about a text file")],
    word_count: Annotated[
        bool, typer.Option(help="Display the total word counts for the txt file")
    ],
    word_freq: Annotated[
        bool, typer.Option(help="Display words frequency for a given text")
    ],
    sentence_count: Annotated[
        bool, typer.Option(help="Display how many sentences are in a given text")
    ],
    reading_time: Annotated[
        bool, typer.Option(help="Display the approx. reading time for a given text")
    ],
):
    """
    Function to recieve a file name then print stats to terminal
    """
    print("hello")
