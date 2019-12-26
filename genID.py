#import uuid module for generating unique random alphanumeric string
import uuid, csv
#import csv for output

#gen id function
def gen_key(string_length=10):
    """Returns a random string of length string_length."""

# Convert UUID format to a Python string.
    random = str(uuid.uuid4())

# Make all characters uppercase.
    random = random.upper()

# Remove the UUID '-'.
    random = random.replace("-","")
# Formating with dashes
    result = '{}-{}-{}'.format(random[:3], random[3:6], random[6:string_length])
# Return the formatted result.
    return result

# Gen unique key for any amount
def gen_amount(amount):
    """Returns a list of keys of any amount"""
    data_list = [["Serial No","Unique ID"]]
    i = 1
    while (i< amount):
        for x in range (0,amount):
            data_list.append([i,gen_key(9)])
            i+=1
    return data_list

list_keys = gen_amount(300000)

#output csv file
with open("keyId.csv", 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(list_keys)


