words=input("Input:").split()
words_count={}
for word in words:
    if word.lower() in words_count:
        words_count[word.lower()]+=1
    else:
        words_count[word.lower()]=1
max_words={}
for key,count in words_count.items():
    if count==max(words_count.values()):
        max_words[key]=count
print("output:")
for key,val in max_words.items():
    print(key,"=",val)
            