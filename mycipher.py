def mycipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python mycipher.py <shift>")
        sys.exit(1)

    shift = int(sys.argv[1])

    # Read input text from stdin (allows for interactive input or redirected file input)
    text = sys.stdin.read().strip()

    encrypted_text = mycipher(text, shift)
    print("Encrypted:", encrypted_text)

    decrypted_text = mycipher(encrypted_text, -shift % 26)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
