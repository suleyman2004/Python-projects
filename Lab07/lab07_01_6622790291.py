word_list = []

while True:
    word = input("Enter a word (type 'exit' to finish): ")
    word2=""
    if word.lower() == 'exit':
        break
    if word.endswith("y"):
        b=len(word)
        c=0
        for i in word:
            c=c+1
            if b==c:
                word2=word2+"il"+i
            else:
                word2=word2+i
    else:
        word2=word
    word_list.append(word2)


print(word_list)
