from math import factorial


def dictionary_search(Aword, Asearch_word):
    def _validate_input(word, search_word):
        try:
            word = word.lower()
            search_word = search_word.lower()
        except:
            raise "PARAMETER_IS_NOT_STRING"

        if not len(search_word) == len(word):
            raise "WORD_LENGTH_ERROR"

        for letter in search_word:
            if not letter in word:
                raise "LETTERS_NOT_IN_RANGE"

    def create_dict(word):
        word_dict = dict()
        word_list = list(word)
        word_list.sort()
        for letter in word_list:
            if letter in word_dict.keys():
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        return word_dict

    def search(word, search_word):
        word_dict = create_dict(word)
        length = len(word)
        sum = 0
        for i, letter in enumerate(search_word, start=1):
            for current_letter in word_dict:
                if letter == current_letter:
                    if word_dict[current_letter] > 1:
                        word_dict[current_letter] -= 1
                    else:
                        word_dict.pop(current_letter)
                    break

                x = factorial(length - i)

                for values in word_dict.values():
                    x /= factorial(values)

                sum = sum + x * factorial(word_dict[current_letter]) / factorial(word_dict[current_letter] - 1)

        return sum + 1

    _validate_input(Aword, Asearch_word)
    return search(Aword, Asearch_word)


if __name__ == "__main__":
    print(dictionary_search(input("main word: "), input("search word: ")))
