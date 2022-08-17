def words_sorting(*args):

    def find_ascii_value(word):
        ascii_value = 0
        for letter in word:
            ascii_value += ord(letter)
        return ascii_value

    words_dict = {}
    sorted_dict = {}

    for word in args:
        words_dict[word] = find_ascii_value(word)


    if len(words_dict)%2 == 0:
        for word in sorted(list(words_dict)):
            sorted_dict[word] = find_ascii_value(word)
    else:
        for word in sorted(list(words_dict)):
            sorted_dict[word] = find_ascii_value(word)

    end_string = ''
    for key in sorted_dict:
        end_string += f"{key} - {words_dict[key]}\n"

    return end_string