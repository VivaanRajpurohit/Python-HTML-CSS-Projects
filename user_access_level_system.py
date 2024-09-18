user_role = "user"
user_status = "active"

if user_role == "admin":
    access_level = "full"
elif user_role == "user" and user_status == "active":
    access_level = "standard"
else:
    access_level = "none"

print(f"The user has {access_level} acccess.")
