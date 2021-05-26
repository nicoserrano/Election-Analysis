print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on AC")

else:
    print("open windows")

# what is the score
score = int(input("What is your score?"))

#Determine grade
if score >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade is a B')
    else:
        if score >= 70:
            print('Your grade is a C')
        else: 
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is an F')

#We can also do an elif statement (makes it look prettier)
# what is the score
score = int(input("What is your score?"))

if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is a B')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
    print('Your grade is an F')

# Membership operators
counties = ["Arapahoe","Denver","Jefferson"] #already was initiated
if "El Paso" in counties:
    print('El paso is in the list of counties')
else:
    print('El paso is not in the list of counties')


#Membership and logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

#other try but with or (either)
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")


#Iteration and FOR loops
for county in counties:
    print(county)

#ITERATION IN DICTIONARIES for keys
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county in counties_dict:
    print(county)

#Also for keys
for county in counties_dict.keys():
    print(county)

#To iterate for getting values
for voters in counties_dict.values():
    print(voters)

#Other way to get the values
for county in counties_dict:
    print(counties_dict[county])

#Another way to get the values
for county in counties_dict:
    print(counties_dict.get(county))

#TO GET KEY-VALUE PAIRS
for county, voters in counties_dict.items():
    print(county +" has " ,voters, "registered voters.")


#ITERATE THROUGH A LIST OF DICTIONARIES
voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)

#To get the list of values from a list of dictionaries (nested for loop)
for county_dict in voting_data:
    for values in county_dict.values():
        print(values)

#if we only want to print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict["county"])

#if we only want to print the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict["registered_voters"])

## Practicing print format
my_votes = int(input("How many votes did you get?"))
total_votes = int(input("What are the total votes in the election?"))

percentage_votes = (my_votes / total_votes) *100

print("Your percentage of votes votes was " ,percentage_votes, "%")
#or
print("Your percentage of votes votes was " + str(percentage_votes) + "%")
#using print(f""")
print(f"Your percentage of votes was {(my_votes / total_votes) *100}%")

##Print drill of dictionaries

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
#We are going to print the key-value pair with a complete sentence f-string
for county, voters in counties_dict.items():
    print(county + " county has " ,voters, "registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} ristered voters.")

#multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)