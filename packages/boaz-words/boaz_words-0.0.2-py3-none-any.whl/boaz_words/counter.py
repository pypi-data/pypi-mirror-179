def word_count(doc: str):
    """Return the number of words in the given text."""
    words = doc.split()
    count = len(words)
    return count
