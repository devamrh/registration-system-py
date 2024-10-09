from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)
print(top_level_domains)



def validate_user(name,email,password):
    """validate the user name, email and password
        
    Args:
        name (string) : Rafi
        email (string) : syedrafinulhuq@gmail.com
        password (string) : rafi123
        
    Returns:
        Boolean: True
        
    
    Raise ValueError if validation fails.
    
    
    """
    
    
    if validate_name(name) == False:
        raise ValueError ("Please make sure your name is greater than 8 characters")

 
    if validate_email(email)  == False:
        raise ValueError("Your email is incorrect")
    
    if validate_password(password) == False:
        raise ValueError("Your password is incorrect")
        
    return True


def register_user(name,email,password):
    
    """
        Attempt to register the user if they pass validation.
        
        Args:
            name (string) : name of the user
            email (string) : email of the user
            password (string) : password of the user
            
        Returns:
            Dict: return a dictionary with the user details
            
        Raises ValueError on missing argument
    """
    
    
    if validate_user(name,email,password):
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        
        return user
    
    return False
