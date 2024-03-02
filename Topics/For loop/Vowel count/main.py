string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowels_number = 0

for char in string:
    if char in vowels:
        vowels_number += 1

print(vowels_number)