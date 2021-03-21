'''Create one list of five element. Find 
the index of 10 in the list. Insert a 
new element in the 2nd position.'''

l1 = [20,10,50,12.8]
print(l1)
for i in range(len(l1)):
    if l1[i] == 10:
        print("Index of 10 is: " + str(i))
l1.insert(2, "abc")
print(l1)