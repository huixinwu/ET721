"""
student's full name
Python data and function
"""
print("\n------ example 1: dictionary -------")
car = {
    "brand": "Tesla",
    "model":"S",
    "year" : 2023,
    "last_visit": "March, 2022"
}

print(f"Best car 2022 = {car["brand"]}, model = {car["model"]}")

print("\n------ example 2: loop through each key in a dictionary -------")
for k in car:
    print(f"{k} has a value of {car[k]}")  

print("\n------ example 3: among of key-pair in a dictionary -------")
print(f"dictionary has {len(car)} key-value pairs")

print("\n------ example 4: remove a key-value pair from a dictionary -------")
car.pop("year")
print(f"dictionary after removing the 'year' key ")
for k in car:
    print(f"{k} , {car[k]}")

print("\n------ example 5: get value of a key -------")
look_key = "last_visit"
print(f"The value of key {look_key} is {car.get(look_key)}")

print("\n------ example 6: store data in a dictionary -------")
phrase ="to be or not to be"
phrase = phrase.split()
print(f"phrase after split method {phrase}")
word_count_dict = {}  # empty dictionary
# for loop to count how many times a word is in the dictionary
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1
        

print(word_count_dict)

print("\n------ EXERICSE -------")
# given the following user list, find the number of users that use 'gmail', 'hotmail', and 'yahoo'
user ="""
    peter = ppan@gmail.com
    diana = d@hotmail.com
    Kent = ckent@yahoo.com
    Bruce = bwayne@hotmail.com
    tony = tstark@gmail.com
    shrek = shrek@gmail.com
"""
user = user.split()
"""
# test
user1 = user[2]
check1 = '@hotmail' in user1
print(check1)
"""
# set up dictionary
email_count_dict = {
    '@hotmail':0,
    '@gmail':0,
    '@yahoo':0,
}
# loop to go through each word
# save the count of emails in a dictionary
for email in user:
    if '@hotmail' in email:
        email_count_dict['@hotmail'] += 1
    elif '@gmail' in email:
        email_count_dict['@gmail'] += 1
    elif '@yahoo' in email:
        email_count_dict['@yahoo'] += 1
# print dictionary
for countemail in email_count_dict:
    print(f"{countemail} = {email_count_dict[countemail]}")