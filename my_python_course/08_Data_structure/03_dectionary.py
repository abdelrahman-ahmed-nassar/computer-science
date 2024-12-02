#-- hash table

# key : value 

# key must be unique


convert_month = {
    "Jan": "january",
    "Feb": "february",
    "Mar": "march",
    4: " april",
    "May": 5,
}

#-- extracting

print(convert_month["Feb"])

#-- extracting with error message

print(convert_month.get("ali", "the value is not exist"))


rolodex = {
  "arron": 5556069,
  "bill": 5559824,
  "jim": 555547,
  "verne": 555309
}
print(rolodex["verne"])

#-- getting the hash of the key 

hash("verne")

#-- adding new pair

rolodex["amanda"] = 555974

#-- changing value

rolodex["amanda"] = 55999
