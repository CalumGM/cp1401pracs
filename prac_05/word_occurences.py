
word_to_count = {}

text = input("Text: ")
string_list = text.split()
for item in string_list:
    frequency = word_to_count.get(item, 0)
    word_to_count[item] = frequency + 1

key_list = list(word_to_count.keys())
key_list.sort()

spacing = max((len(word) for word in key_list))
for element in key_list:
    print("{:{}} : {}".format(element, spacing, word_to_count[element]))
