#это для шифрования флага
import base64
def generate_vigenere_table():
    table = []
    for i in range(256): #используем не 26 символов, а всю таблицу ASCII
        row = []
        for j in range(256):
            row.append(chr((i + j) % 256))
        table.append(row)
    return table


def modified_vigenere_encrypt(plaintext, key):
    table = generate_vigenere_table()
    ciphertext = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        row = ord(key[i % key_length])
        col = ord(char)
        encrypted_char = table[row][col]
        ciphertext.append(encrypted_char)
    return ''.join(ciphertext)


def main():
    with open('flag.txt', 'r') as file:
        plaintext = file.read().strip()

    with open('key.txt', 'r') as file:
        key = file.read().strip()

    ciphertext = modified_vigenere_encrypt(plaintext, key) #зашифрованный текст
    ascii85_ciphertext = base64.a85encode(ciphertext.encode()).decode() #закодированный текст

    with open('ciphertext.txt', 'w') as file:
        file.write(ascii85_ciphertext)

    print(f"Ciphertext saved in ciphertext.txt")

if __name__ == "__main__":
    main()
