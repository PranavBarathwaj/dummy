def count_occurrences(token, file_path="corpus.txt"):
    """
    Count how many times the token appears in the given text file.
    
    Parameters:
    token (str): The word to search for in the text.
    file_path (str): The path to the text file.
    
    Returns:
    int: The number of occurrences of the token in the text.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Convert the text to lowercase to make search case-insensitive
            return text.split().count(token.lower())
    except FileNotFoundError:
        return 0
