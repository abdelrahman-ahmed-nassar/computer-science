# iteration  loops
# repeats the same procedure multiple times until it reaches a specified end point


i = 1
while i <= 10:
    print(i)
    i += 1
    # or i = i + 1
else:
    print("the condition is not true")


print("the loop has ended")

#-- infinite loop

# bug that can occur when the ending condition is omitted or specified incorrectly

# while i == True:
# print(i)
# i += 1

#-- continue

while i <= 10:
    i += 1
    if i == 6:
        continue
    print(i)

#-- break

while i <= 10:
    i += 1
    if i == 6:
        break
    print(i)
