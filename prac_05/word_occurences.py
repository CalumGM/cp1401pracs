
word_to_count = {}

text = input("Text: ")
string_list = text.split()
print(string_list)
for item in string_list:
    frequency = word_to_count.get(item, 0)
    word_to_count[item] = frequency + 1
print(word_to_count)
