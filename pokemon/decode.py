chars = {
    'a': (3, 0b000),
    'e': (4, 0b0010), #2->1
    'o': (4, 0b0011),
    'r': (4, 0b0100),
    'i': (4, 0b0101),
    'l': (4, 0b0110),
    'n': (4, 0b0111),
    't': (4, 0b1000),
    's': (4, 0b1001),
    'u': (5, 0b10100), #20->9
    'g': (5, 0b10101),
    'c': (5, 0b10110),
    'm': (5, 0b10111),
    'd': (5, 0b11000),
    'p': (5, 0b11001),
    'h': (5, 0b11010),
    'b': (5, 0b11011),
    'k': (5, 0b11100),
    'y': (6, 0b111010), #58->18
    'w': (6, 0b111011),
    'f': (6, 0b111100),
    'v': (6, 0b111101),
    'z': (7, 0b1111100), #124->22
    'x': (7, 0b1111101),
    'j': (8, 0b11111100), #252->24
    'q': (8, 0b11111101),
    'N': (8, 0b11111110),
    '-': (11, 0b11111111000), #2040->27
    ' ': (11, 0b11111111001),
    '.': (11, 0b11111111010),
    'é': (11, 0b11111111011),
    '♀': (11, 0b11111111100),
    '♂': (11, 0b11111111101),
    "'": (11, 0b11111111110),
    '2': (11, 0b11111111111)
}

chars = {v: c for c, v in chars.items()}

with open('data.bin', 'rb') as f:
    data = f.read()

big_number = 0
excluded_chars = [13, 92, 96]
for character in data:
    for e in reversed(excluded_chars):
        if character >= e:
            character -= 1
    big_number *= 125
    big_number += character

def biterator(n):
    while n > 0:
        yield n % 2
        n //= 2
        
pokemon = []
char_size = char_bits = 0
pokemon_size = 3
bits = biterator(big_number)
previous_pokemon_char = 'a'

for bit in bits:
    char_bits *= 2
    char_bits += bit
    char_size += 1
    if (char_size, char_bits) in chars:
        if chars[(char_size, char_bits)] == 'N':
            pokemon_size += 1
        else:
            pokemon.append(chars[(char_size, char_bits)])
        char_size = char_bits = 0
        if len(pokemon) == pokemon_size:
            previous_pokemon_char = pokemon[0]
            print(''.join(pokemon))
            pokemon = []
            if next(bits, 0) == 1:
                pokemon.append(previous_pokemon_char)
