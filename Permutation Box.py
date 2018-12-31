s = int(input())
i=0
pbox =[]
pbox=input().split(" ")
while(i<len(pbox)):
    pbox[i] = int(pbox[i])
    i+=1
n = int(input())
input_table = input()
binary_input_table = bin(int(input_table, 16))[2:].zfill(n)
output = ""
for p in pbox:
    output+=binary_input_table[p-1]
k = hex(int(output, 2))[2:].zfill(int(s/4))
k = k.upper()
print(k)
