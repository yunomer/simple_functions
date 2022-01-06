# Q2: Write Python code to create a dictionary for the same 
# information above and convert it to JSON

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
print(localPerson)


