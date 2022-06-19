from math import factorial

def search_word_pos(main_word, search_word):
    counts = dict()
    letters = list()
    s_letters = list()
    r_letters = list()

    def _list_letters(word):
        for letter in word:
            r_letters.append(letter)
            if letter in letters:
                counts[letter] += 1
            else:
                letters.append(letter)
                counts[letter] = counts.get(letter, 1)
        letters.sort()
        for l in search_word:
            s_letters.append(l)

    def _error_check(search_word):
        try:
            word = main_word.lower()
            search_word=search_word.lower()
        except:
            return "PARAMETER_IS_NOT_STRING"
        _list_letters(word)
        if not len(search_word) == len(word):
            return "WORD_LENGTH_ERROR"

        for letter in search_word:
            if not letter in word:
                r_letters.remove(letter)
            else:
                return "LETTERS_NOT_IN_RANGE"

    def search(current_letter, Aletters, Acounts, l):
        sum = 0
        for letter in Aletters:
            if letter == current_letter:
                break
            product = 1
            for key, val in Acounts.items():
                if key == letter:
                    continue
                if val > 1:
                    product *= factorial(val)
            sum += factorial(l - 1) / product
        return sum

    def main_search():
        test_array = letters.copy()
        test_dict = counts.copy()
        total = 0
        for _ in search_word:
            break_letter = s_letters[0]

            total += search(break_letter, test_array, test_dict, len(s_letters))
            s_letters.remove(break_letter)
            test_array.remove(break_letter)
            if test_dict[break_letter] > 1:
                test_dict[break_letter] -= 1
                test_array.append(break_letter)
                test_array.sort()
            else:
                del test_dict[break_letter]
        total += 1
        return total

    _error_check(search_word)
    return main_search()


if __name__ == "__main__":
    print(search_word_pos(input(" input word "), input("search word  ")))
