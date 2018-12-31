s = (input().split(" "))
sin = int(s[0])
sout = int(s[1])
out = input().split(" ")
to_get_out = 0
while (to_get_out == 0):
    to_get_out = 1
    i=0
    if(sout<sin):
        print("IMPOSSIBLE")
        break
    while(i<len(out)):
        out[i] = int(out[i])
        i+=1

    num = []
    i=0
    while(i<sin):
        num.append( i+1)
        i+=1


    x = set(out)
    y = set(num)
    if(x !=y): 
        print("IMPOSSIBLE")
        break

    output = ""
    q =0
    w =0
    done = []
    while (q<sout):
        while(w<sout):
            if((out[w] == q+1) and (out[w] not in done)):
                u = w+1
                done.append(u)
                output+=str(u)
                output+=" "
                #print(output)
            w+=1
        q+=1
        w =0
    print(output)
    break

















    

"""sorted_input = pbox[:]
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
    print("IMPOSSIBLE")"""
