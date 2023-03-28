text = input("Enter message: ")

# Validate shift value input
while True:
    try:
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1, 26):
            raise ValueError
        break
    except ValueError:
        print("Invalid shift value! Please enter an integer between 1 and 25 (inclusive).")

cipher = ''
for char in text:
    if char.isalpha():
        if char.isupper():
            cipher += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            cipher += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        cipher += char

print("Encoded message:", cipher)
