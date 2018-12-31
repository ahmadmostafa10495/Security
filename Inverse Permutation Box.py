s = int(input())
i=0
pbox =[]
pbox=input().split(" ")
while(i<len(pbox)):
    pbox[i] = int(pbox[i])
    i+=1
num = []
i=0
while(i<len(pbox)):
    num.append( i+1)
    i+=1
sorted_input = pbox[:]
sorted_input.sort()
q =0
w =0
output = ""
if sorted_input == num:
    while (q<s):
        while(w<s):
            if(pbox[w] == q+1):
                u = w+1
                output+=str(u)
                output+=" "
                #print(output)
            w+=1
        q+=1
        w =0
    #output = output[:len(output)-2]
    print(output)
else:
    print("IMPOSSIBLE")
