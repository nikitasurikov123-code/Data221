def dictionary_from_string(string):
    #empty dictionary
    dictionary = {}
    #loop through each word in the list
    for s in string:
        #finds the length of the word in the list
        length_of_string = len(s)
        #checks if pairity is odd or even by dividing the length of the string by 2
        if length_of_string % 2 == 0:
            pairity = "even"
        else:
            pairity = "odd"
            #puts the length and parity information into dictionary
        dictionary[s] = {"length": length_of_string, "pairity": pairity}
    return dictionary
words = ["data", "science"]
print(dictionary_from_string(words))