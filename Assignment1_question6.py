def list_of_numbers_from_dictionary(numbers):
    result = {}
    #sorts the numbers for later
    sorted_numbers = sorted(numbers)
    #loops through each number in the sorted list
    for num in sorted_numbers:
        #resets the total for every number
        total = 0
        #checks if n is in numbers
        for n in numbers:
            #if n <= num, then it adds on to the total until n > num for every number in the list
            if n <= num:
                #add 1 to the increment count if n <= num
                total += 1
                #calculates percentage
        result[num] = (total/ len(numbers)) * 100
    return result
print(list_of_numbers_from_dictionary([3, 1, 2, 3, 4, 2]))




