# Cortana Onboarding Program Test 
# Print To Screen Fuction 

from operator import contains


print("Supp, Gawd ^_^" /n )

print("Welcome to the world of coding!")

# Ask user for name 
name = input("Who am I talking to? ")

# Removes anyspaces + Capitilize name would be.capitalize() if just the first word but Two word names get .title()
# Alternitivley you can also use name = input("__").strip().title 

name = name.strip().title()

# Greet user
print("Hey " + name + " lovely name, I am Cortana. Your guide to your digital revolution! I'm here to teach you by showing you how easy it all is to learn.")

# Are they ready to learn?

readytolearn = input("Do you think your up for the challenge?")

# Confirm + Data Collect  

print("Okay bet, lets get it!")

print("First lets start off by gathering some basic info to help my algorithms learn more about ya.")

age = int(input("What year were you born?"))

