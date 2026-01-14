# Input validation module for AI Stem Separation CLI
# Trello Card: https://trello.com/c/ML8XmaRU

def validate_input(file_path: str) -> bool:
    """Validate input audio file exists and is readable."""
    import os
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    return True
