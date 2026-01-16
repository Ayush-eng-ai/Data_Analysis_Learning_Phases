# Loops in Python
'''
    Loops are used for sequential traversal.. for traversing list, string, tuples etc
'''

'''
        for Loops
        for el in list:
            #some work
'''

list = [1,2,3,4]

for el in list:
    print(el)

print(" End of code ")

'''
            for loop with else

            for el in list
                #some work
            else:
                #work when loop ends
    '''
for el in list:
    print(el)
else:
    print("END")

tuple = (1,2,3,4)

for val in tuple:
    print(val)


str = "Ayush Rajput"

for char in str:
    print(char)
else:
    print("End")


str = "Data Scientiest"

for char in str:
    if(char == "s"):
        print("s found")
        break
    print(char)
else:
    print("End")

