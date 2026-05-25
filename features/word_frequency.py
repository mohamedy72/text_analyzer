def word_frequency(text: str) -> dict:
    """
    Purpose: Takes a text and returns how many times each word apppears
    """
    count_words = {}
    if not text.strip():
        return "No text provided"

    splitting_text = text.split()

    for word in splitting_text:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1

    return count_words


# end def
