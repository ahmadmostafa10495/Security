key = input()
plain = input()
if(len(key) == len(plain)):
    output0 = "YES"
else:
    output0 = "NO"
i=0
j=0
output1= ''
while(j<len(plain)):
    x=ord(plain[j])+ord(key[i])
    if(x > ord('Z')):
        x%= 26
        x+=ord("A")
    output1+=chr(x)
    i+=1
    i%=len(key)
    j+=1
i = 0
j = 0
output2 = ""
while(j<len(plain)):
    x= (ord(plain[j])) ^ (ord(key[i]))
    output2 += format(x, '02X')
    
    i+=1
    i%=len(key)
    j+=1

print("Vigenere: " + output1 + "\nVernam: " + output2 + "\nOne-Time Pad: " + output0)
