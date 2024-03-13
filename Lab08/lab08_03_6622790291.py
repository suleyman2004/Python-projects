while True:
    seq1=input("Input sequence1:").split()
    seq2=input("Input sequence2:").split()
    a=[]
    b=[]
    for i in seq1:
        if i.isnumeric():
            a.append(i)
    for i in seq2:
        if i.isnumeric():
            b.append(i)

    a,b=set(a),set(b)
    if a==b:
        print("Output: same set")
    else:
        print("Output: different set")