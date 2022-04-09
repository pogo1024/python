def caesar_encrypt(text):
    result = ""
    for i in range(len(text)):
        char_position = ord(text[i])
        char_position = char_position - 97
        new_char_position = char_position + 3
        new_char_position = new_char_position % 26
        new_char_podition = new_char_position + 97
        result = result + chr(new_char_position)
        print(result)
    return result

def caesar_decrypt(cipher_text):
    result = ""
    for i in range(len(cipher_text)):
        char_position = ord(cipher_text[i])
        char_position = char_position - 97
        new_char_position = char_position - 3
        new_char_position = new_char_position % 26
        new_char_position = new_char_position + 97
        result = result + chr(new_char_position)
        print(result)
    return result

text = "picocft"
print(f"Plain Text: {text}")
cipher_text = caesar_encrypt(text)
print(f"Encrypted: {caesar_encrypt(cipher_text)}")
cipher_text = caesar_decrypt(text)
print(f"Decrypted: {caesar_decrypt(cipher_text)}")


