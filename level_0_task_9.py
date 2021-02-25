def vowels_in_the_string(string):
    
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    for i in vowels:
        if i in string:
            print(i)