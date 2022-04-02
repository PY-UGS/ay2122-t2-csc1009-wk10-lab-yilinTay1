#. Create another Python project, repeat the Question 2b and 2c from Laboratory Wk01.

#.b. Example 3, change the currency variable into the module code you are taking
#.in this trimester, while the switch case will print out the complete module
#.title. E.g.: input CSC1009 > Output “Object-Oriented Programming”
def moduleCode(i):
        switcher={
                "CSC1009":'Object-Oriented Programming',
                "CSC1006":'Mathematics 2',
                "CSC1007":'Operating Systems',
             }
        return switcher.get(i,"Invalid module code")
b = input('Enter the module code you are taking: ') # Get user's input
print(moduleCode(b)) # Switch statement

#.c. Example 4: change the for loop, print out the odd number in descending order
#.starting from 102 and ending with 66
for x in range (102, 66, -1):
    if(x%2 == 1):
        print(x); #  print out the odd number