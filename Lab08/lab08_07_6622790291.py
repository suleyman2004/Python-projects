seq1=input("Input sequence1:").split()
seq2=input("Input sequence2:").split()
seq1=[i for i in seq1 if i.isnumeric()]
seq2=[i for i in seq2 if i.isnumeric()]

seq1,seq2=set(seq1),set(seq2)

same=seq1 & seq2

if len(same>0):
    print("Output: True")
else:
    print("Output:False")