def decipher_message(secret_message):
    words = secret_message.split()
    deciphered_words = []

    for word in words:
        num_str = ''.join([char for char in word if char.isdigit()])
        first_char = chr(int(num_str))
        
        rest_of_word = ''.join([char for char in word if not char.isdigit()])
        
        if len(rest_of_word) > 1:
            
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
        
        deciphered_word = first_char + rest_of_word
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)

secret_message = input()
print(decipher_message(secret_message))