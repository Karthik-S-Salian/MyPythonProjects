# PROGRAM TO COUNT VOWEL IN THE GIVEN WORD

word = input("Enter a word: ")
word = word.lower()
vowel=0

l = list()
for letter in word.lower():
    if letter in 'aeiou':
        l.append(letter)
        vowel += 1

print(f'vowels in {word} are {l} \n The number of {vowel = }')

