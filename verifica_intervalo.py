#Verifica se um número está num dado intervalo

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            if value < min or value > max:
                raise ValueError()
            ok = True
        except ValueError:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value

v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
