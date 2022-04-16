
def repeat(key, length):
    multiple = int(length/len(key) + 1)
    repeated_string = key * multiple
    return repeated_string[:length] 
    


print('GIVE IT TO ME')
txt = input(str())
print('YOUR FUCKEN KEY PLEASE BITCH')
key = input(str())
length = len(txt)

key_ultimate = (repeat(key, length))
key_arr = []
txt_arr = []
for i in range(length):
        char_position = ord(key_ultimate[i])
        char_position = char_position - 97
        key_arr.append(char_position)


for j in range(len(txt)):
    char_position = ord(txt[j])
    char_position = char_position - 97
    txt_arr.append(char_position)



def addFunc(a,b):
    return a + b

x = map(addFunc, key_arr, txt_arr) 


encrypted_list = (list(x))
print(encrypted_list)

encrypted_arr = []

for k in range(len(encrypted_list)):
    new_char_position = encrypted_list[k] % 26
    new_char_position = new_char_position + 97 
    new_char_position = chr(new_char_position)
    encrypted_arr.append(new_char_position)

print("".join(encrypted_arr))






  
