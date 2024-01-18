# Dictionary comprehensions

# player = 'Lionel Messi'
# count_alphabet = {letter: player.count(letter) for letter in player}
# print(count_alphabet)

player = 'Minjae Kim'
count_alphabet = dict()
for letter in player :
    count_alphabet[letter] = player.count(letter)
print(count_alphabet)