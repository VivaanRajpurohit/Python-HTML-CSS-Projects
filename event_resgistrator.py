user_name = input("What is your name: ")
event_invited_to = input("What event are you going to: ")
event_location = input("Where is the location of the event: ")

user_party_details = "Hello, %s, you have succefully been registered for the %s event near %s." % (user_name, event_invited_to, event_location)

print(user_party_details)
