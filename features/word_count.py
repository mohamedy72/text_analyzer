"""
A Function which takes a string and return how many words in it
"""


def word_count(text: str) -> int:
    """
    Purpose: Takes a string and return word counts
    """
    non_words = ["-", "_", "—"]

    if not text.strip():
        return 0

    filtered_str = [word for word in text.split() if word not in non_words]

    word_counts = len(filtered_str)

    return word_counts


# end def
