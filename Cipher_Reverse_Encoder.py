cipher = input("Enter encoded message: ")

while True:
    try:
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1, 26):
            raise ValueError
        break
    except ValueError:
        print("Invalid shift value! Please enter an integer between 1 and 25 (inclusive).")

text = ''
for char in cipher:
    if char.isalpha():
        if char.isupper():
            text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            text += chr((ord(char) - 97 - shift) % 26 + 97)
    else:
        text += char

print("Decoded message:", text)
