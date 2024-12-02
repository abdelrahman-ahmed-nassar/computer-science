#-- creating a list 

my_friends = ["ali", "omar", "adam", "osman", "ahmed"]

#-- open data type

my_list = [1, True, False, "name", "programming", "ali"]


#-- using it 

print(my_friends)

#-- extracting from it 

print(my_friends[0])

print(my_friends[0 : ])

print(my_list[0:-1])

#-- changing the list (Mutable)

my_friends[0] = "josef"
print(my_friends)

#-- concatenating two lists

new_list = my_list + my_friends

new_list = my_friends.extend(my_friends)

print(new_list)

#-- append elements

my_friends.append("ahmed")

print(my_friends)

#-- inserting

my_friends.insert(0, "mohamed")

print(my_friends)

#-- removing

my_friends.remove("josef")

print(my_friends)

# extracting last element

last_friend = my_friends.pop()

print(my_friends)
print(last_friend)

#-- get the index 

print(my_friends.index("omar"))

#-- sorting the list 

print(my_friends.sort())

#-- count

print(my_friends.count("ahmed"))

#-- joining the list and make it a string

separator = "-"

separator.join(my_friends)

#-- deleting

my_friends.clear()
