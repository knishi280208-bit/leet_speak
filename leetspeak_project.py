

def leetspeak_converter(text):
    # Dictionary containing letter replacements
    leet_dict = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }

    result = ""

    # Check each character
    for char in text:
        if char.lower() in leet_dict:
            result += leet_dict[char.lower()]
        else:
            result += char

    return result


# Main program
print("===== LEETSPEAK TRANSLATOR =====")

sentence = input("Enter an English sentence: ")

converted = leetspeak_converter(sentence)

print("Original Text:", sentence)
print("Leetspeak Text:", converted)
