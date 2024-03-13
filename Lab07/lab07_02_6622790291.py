word_list = []

while True:
    word = input("Enter a word (type 'exit' to finish): ")
    if word.lower() == 'exit':
        break
    word_list.append(word.capitalize())


print(word_list)