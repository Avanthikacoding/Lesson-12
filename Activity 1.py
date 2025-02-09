string = input("Please enter your own word: ")
character = input("Please enter your own character: ")
a = 0
hi = 0
while(a < len(string)):
    if(string[a] == character):
        hi = hi + 1
    a = a + 1
print("The total number of times " , character , " has occured = " , hi )