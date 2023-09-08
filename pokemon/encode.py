
chars = {
    'a': (3,          0b000),
    'e': (4,         0b0100),
    'o': (4,         0b1100),
    'r': (4,         0b0010),
    'i': (4,         0b1010),
    'l': (4,         0b0110),
    'n': (4,         0b1110),
    't': (4,         0b0001),
    's': (4,         0b1001),
    'u': (5,        0b00101),
    'g': (5,        0b10101),
    'c': (5,        0b01101),
    'm': (5,        0b11101),
    'd': (5,        0b00011),
    'p': (5,        0b10011),
    'h': (5,        0b01011),
    'b': (5,        0b11011),
    'k': (5,        0b00111),
    'y': (6,       0b010111),
    'w': (6,       0b110111),
    'f': (6,       0b001111),
    'v': (6,       0b101111),
    'z': (7,      0b0011111),
    'x': (7,      0b1011111),
    'j': (8,     0b00111111),
    'q': (8,     0b10111111),
    'N': (8,     0b01111111),
    '-': (11, 0b00011111111),
    ' ': (11, 0b10011111111),
    '.': (11, 0b01011111111),
    'é': (11, 0b11011111111),
    '♀': (11, 0b00111111111),
    '♂': (11, 0b10111111111),
    "'": (11, 0b01111111111),
    '2': (11, 0b11111111111)
}


with open('pokemon.txt', encoding='utf-8') as f:
    pokemon_list = f.readlines()

pokemon_list.sort(key=len)

current_len = len(pokemon_list[0])
binary = []
last_pokemon = 'a'
matches = not_matches = 0
for pokemon in pokemon_list:
    same_letter = 1 if pokemon[0] == last_pokemon[0] else 0
    binary.append((1, same_letter))
    
    if len(pokemon) > current_len:
        binary.append(chars['N'])
        current_len = len(pokemon)
    
    
    for letter in pokemon[same_letter:-1]:
        binary.append(chars[letter])
    
    last_pokemon = pokemon


big_number = 1
for length, value in reversed(binary[1:]):
    big_number *= 2**length
    big_number += value


excluded_chars = [13, 92, 96]
data = []
while big_number > 0:
    next_char = big_number % 125
    big_number //= 125
    for e in excluded_chars:
        if next_char >= e:
            next_char += 1
    data.append(next_char)

with open('data.bin', 'wb') as f:
    f.write(bytearray(reversed(data)))
