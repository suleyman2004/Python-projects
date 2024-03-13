words=input("Input:").split()
words_count={}
for word in words:
    if word.lower() in words_count:
        words_count[word.lower()]+=1
    else:
        words_count[word.lower()]=1
max_words={}
print("output:")
none=True
for key,val in words_count.items():
    if val>1:
        print(key)
        none=False
if none==True:
    print("None") 
            