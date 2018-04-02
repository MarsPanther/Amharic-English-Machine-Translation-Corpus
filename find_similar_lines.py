amharic_dictionary = {}
english_dictionary = {}

with open('am.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        amharic_dictionary[count] = line

with open('en.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        english_dictionary[count] = line


list_of_similarity = []
for n in range(1,len(english_dictionary)-2):
    count = 0
    for each in english_dictionary.values():
        if english_dictionary[n] == each:
            count += 1
    if count > 1:
        list_of_similarity.append(n)
        continue
    n += 1
    print(n)

print(list_of_similarity)



lines_to_remove = []

while len(list_of_similarity) > 1:

    first_index = list_of_similarity[0]
    first_english = english_dictionary[first_index]
    first_amharic = amharic_dictionary[first_index]
    list_of_similarity.pop(0)


    for each in list_of_similarity:
        if amharic_dictionary[each] == first_amharic and english_dictionary[each] == first_english:
            lines_to_remove.append(each)

print(lines_to_remove)
for items in lines_to_remove:
    print(items)
    if items in amharic_dictionary.keys() and items in amharic_dictionary.keys():
        amharic_dictionary.pop(items)
        english_dictionary.pop(items)

print(len(amharic_dictionary))
print(len(english_dictionary))



fo_amharic = open('new-am.txt', 'w')

for k, v in amharic_dictionary.items():
    fo_amharic.write(str(v))

fo_amharic.close()


fo_english = open('new-en.txt', 'w')

for k, v in english_dictionary.items():
    fo_english.write(str(v))

fo_english.close()

