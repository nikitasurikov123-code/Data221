from random import random
values = [random() for i in range(20)]
x = random()
#sorts the values
values.sort()
#new empty list to store the indices
indices = []
#loops through the list values
for i in range(len(values)):
    #checks if the value is greater than or equal to x
    if values[i] >= x:
        #adds the indices greater than or equal to x to the indices list
        indices.append(i)
print("Sorted Values: " + str(values))
print("X: " + str(x))
print(indices)