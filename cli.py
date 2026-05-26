from typing import Annotated
from pathlib import Path
import typer

from features import word_count, word_frequency, sentence_count, reading_time
from helpers import read_file


def analyze_text(
    filename: Annotated[
        str, typer.Argument(help="The name of the file to be anaylzed")
    ],
    words_count: Annotated[
        bool, typer.Option(help="Display the total word counts for the txt file")
    ] = False,
    words_freq: Annotated[
        bool, typer.Option(help="Display words frequency for a given text")
    ] = False,
    sentences_count: Annotated[
        bool, typer.Option(help="Display how many sentences are in a given text")
    ] = False,
    read_time: Annotated[
        bool, typer.Option(help="Display the approx. reading time for a given text")
    ] = False,
):
    """
    Function to recieve a file name then print stats to terminal
    """
    # Parse filename into Full Path
    file_path = Path(filename).absolute()

    if not file_path.exists():
        return "File doesnt exist"

    text = read_file(file_path)
    count_words = word_count(text)
    words_frequency = word_frequency(text)
    count_sentences = sentence_count(text)
    rd_time = reading_time(count_words, 235)

    # print(text, count_sentences, count_words, words_frequency, rd_time)
    if words_count:
        print(f"Words count is: {count_words}")

    if words_freq:
        for word, count in sorted(
            words_frequency.copy().items(), key=lambda item: item[1], reverse=True
        ):
            if word == "•":
                continue
            print(f"The word *{word}* appears {count} times")

    if sentences_count:
        print(f"The whole text contains {count_sentences} sentences")

    if read_time:
        print(f"Total reading time is: {rd_time}")
