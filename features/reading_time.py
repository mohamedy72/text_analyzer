import math


def reading_time(word_counts, word_per_minute=230):
    """
    Purpose: This function accept (word_counts, word_per_miute) and returns estimated reading time
    """
    if not word_counts:
        return "You didnt pass any word counts. Cannot estimate"

    total_reading_time = math.ceil(word_counts / word_per_minute)
    if total_reading_time <= 1:
        return "Estimated reading: 1 min"
    else:
        return f"Estimated reading: {total_reading_time} mins"
