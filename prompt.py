from ._init_ import count_occurrences

def report_count(token):
    """
    Print the number of times the token appears in the corpus.txt file.
    
    Parameters:
    token (str): The word to search for in the corpus.
    """
    count = count_occurrences(token)
    print(f"The term {token} shows up in the corpus {count} times.")
