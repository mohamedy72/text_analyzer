def sentence_count(text: str) -> int:
    """
    Purpose: Takes a string and returns how many sentencts in it
    """
    if not text.strip():
        return 0

    # 1. Split text based on (.) at the end
    split_text = [sentence.strip() for sentence in text.split(".") if sentence]

    return len(split_text)


# end def
