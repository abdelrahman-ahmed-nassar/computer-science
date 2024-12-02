
for letter in "school":
    print(letter)

'''
for :
specifies a variable name that we can use in each iteration of the loop to reference the current value 

in :
indicate that what follows is the set of values that we want to iterate through 

iteration
repeats the same procedure multiple times until it reaches a specific endpoint

loop
code that iterates, moving from beginning to end of the process, then starting over


iteration
1- specify the data
2- what should happen to the data
3- what is the end point


'''

friends = ["ali", "ahmed", "ahmed", "mohamed"]

#-- looping over a list 

for friend in friends:
    print(friend)

#-- looping over a number range

for x in range(10):
    print(x)

#-- define a start and an end 

for y in range(5, 10):
    print(y)


#-- using the length of the list 

for z in range(len(friends)):
    print(z)

## printing element
for index in range(3):
    print(friends[index])


# check even or odd for 10 numbers
for num in range(10):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")


#-- using the length of the list

for some_one in range(len(friends)):
    if friends[some_one] == "ali":
        print(some_one, "is the winner")
    else:
        print(some_one, "is not the winner")

#-- break key word

for friend in friends:
    if friend == "omar":
        print(friend, " is your friend")
        break
else:
    print(" not found")

#--  continue key word

for t in range(3, 10):
    if t == 5:
        continue
    print(t, " is the chosen number")
