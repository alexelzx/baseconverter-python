#Code made by Alexios Elizalde Xirokosta
def convert_base(number, base):
  if base not in [2, 8, 10, 16]:
    raise ValueError("Base invalide! Selectionne une des bases suivantes: 2, 8, 10, or 16.")

  if base == 10:
    return str(number)

  digits = []
  while number > 0:
    remainder = number % base
    digits.append(str(remainder))
    number //= base

  digits.reverse()
  return "".join(digits)

# Ask the user for input
base = int(input("Tapez la base désiré (2, 8, 10, or 16): "))
number = int(input("Tapez le nombre/chiffre a etre converti "))

converted_number = convert_base(number, base)
print(f"{number} in base {base} is {converted_number}")
