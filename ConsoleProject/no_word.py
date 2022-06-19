from math import factorial

def search(word):
    word = word.lower()
    counts = dict()
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    arrange_all(word, counts)


def arrange_all(word, counts):
    repeated = 1
    for key in counts:
        if counts[key] > 1:
            repeated *= factorial(counts[key])
    print("number of ways word " + word + " can be arranged =" + str(factorial(len(word)) / repeated))


if __name__ == "__main__":
    search(input(" input word "))
