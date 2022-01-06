# Q2: Write Python code to create a dictionary for the same 
# information above and convert it to JSON

# Run this in your terminal by going to your directory and: python3 function.py

# importing JSON package
import json 

name = 'John Doe'
age = 35
city = 'Collingwood'

personDict = {
    "Name": name,
    "Age": age,
    "City": city,
}

# Converting into JSON
localPerson = json.dumps(personDict)

# Printing JSON as string
print('Stored Data: ', localPerson)


