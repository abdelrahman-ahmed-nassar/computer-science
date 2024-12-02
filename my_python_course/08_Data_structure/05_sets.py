# un ordered collection of unique items 

college = set(["bill", "katy", "verne","dillon","olivia","richard","jim"])

coworker = set(["aron", "bill", "brandon", "david", "frank","connie", "kyle", "olivia"])

family = set(["garry","landon", "larry", "mark", "olivia","katy", "rea", "tom"])

friends = college.union(coworker, family)


#-- check exit

"verne" in family 


#-- add to the list 

family.add("ss")

#-- remove an element

coworker.remove("ss")

#-- remove random element

family.pop()

