import base64

def generate_vigenere_table():
    table = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(chr((i + j) % 256))
        table.append(row)
    return table


def modified_vigenere_decrypt(ciphertext, key):
    table = generate_vigenere_table()
    plaintext = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        row = ord(key[i % key_length])
        col = table[row].index(char)
        decrypted_char = chr(col)
        plaintext.append(decrypted_char)
    return ''.join(plaintext)


def main():
    with open('crypto/ciphertext.txt', 'r') as file:
        ascii85_ciphertext = file.read().strip()

    ciphertext = base64.a85decode(ascii85_ciphertext.encode()).decode()
    key = input("Enter the key: ")

    plaintext = modified_vigenere_decrypt(ciphertext, key)
    print(f"Your flag: {plaintext}")

if __name__ == "__main__":
    main()
