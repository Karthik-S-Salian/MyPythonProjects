# PROGRAM TO COUNT VOWEL IN THE GIVEN WORD

word = input("Enter a word: ")
word = word.lower()
vowel = 0

vowels = ['a', 'e', 'i', 'o', 'u']
l = list()
for letter in word:
    if letter in vowels:
        l.append(letter)
        vowel += 1

print('vowels: ', l)
print("The number of vowel in " + word + " is " + str(vowel))
