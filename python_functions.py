top_level_domains = [
    "com", "org", "net", "edu", "gov", "mil", "int", "co", "io"
]

def validate_name(name):
    """
    Validate if the provided name is greater than 8 characters.
    
    Args:
        name (string): The name to validate
    
    Returns:
        bool: True if the name is valid, False otherwise
    """
    if len(name) > 8:
        return True
    return False


def validate_email(email):
    """
    Validate if the provided email has the correct format and top-level domain.
    
    Args:
        email (string): The email to validate
    
    Returns:
        bool: True if the email is valid, False otherwise
    """
    if "@" not in email or "." not in email:
        return False

    domain = email.split('.')[-1]
    
    if domain in top_level_domains:
        return True
    return False


def validate_password(password):
    """
    Validate if the provided password is at least 6 characters long.
    
    Args:
        password (string): The password to validate
    
    Returns:
        bool: True if the password is valid, False otherwise
    """
    if len(password) >= 6:
        return True
    return False
