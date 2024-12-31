# function that count vowels in a word 

def count_vowels(word):
    
    vowels = "aeiou"
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

# Get user input and count vowels
user_input = input("Enter a word: ")
vowel_count = count_vowels(user_input)
print(f"The word '{user_input}' contains {vowel_count} vowels.")
