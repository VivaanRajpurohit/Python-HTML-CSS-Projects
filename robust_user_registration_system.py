class RegistrationError(Exception):
    """Custom exception for registration errors"""
    pass

def user_registration(username, password):
    try:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        print(f"User {username} is registered successfully")
    except ValueError as e:
        print(f"Registration error: {e}")
    finally:
        print("Cleanup actions completed.")

user_registration("John Doe", "Pass")
