#question 1
#set a threshold to reach
threshold = 150
#product starts at 5
product = 5
#multiplied into product each loop of the while loop
currentNumber = 1
#loops as long as the product is less than the threshold
while product < threshold:
    #multiply product by current number
    product = currentNumber*product
    #add one to current number each iteration
    currentNumber += 1
#print product after it is equal to or above threshold
print(product)
#subtract one from current number as it adds one on the last iteration, but product already reached its number above the threshold
#it's one value larger than the one used
print(currentNumber-1)
