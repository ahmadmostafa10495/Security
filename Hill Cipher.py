import math
def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print ("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = int(input())
L = math.ceil(math.sqrt(length))
mat = []
mat = (input().split(" "))
i = 0
while(i<length):
    mat[i] = int(mat[i])
    i+=1
plain = input()
i = 0
j = 0
k = 0
key = [[0 for x in range(L)] for y in range(L)]
mat1 = [[0 for x in range(1)] for y in range(L)]
while(i<L):
    while(j<L):
        key[i][j] = mat[k]
        k+=1
        j+=1
    i+=1
    j=0
i = 0
j = 0
k = 0
a_count = 0
output = ""
while(a_count<len(plain)):
    while(i<L):
        if(a_count<len(plain)):
            mat1[i][0] = alphabet.find(plain[a_count])
        else:
            plain+="X"
            mat1[i][0] = alphabet.find(plain[a_count])
        a_count+=1
        i+=1
    i = 0
    ans = matrixmult(key,mat1)
    x = 0
    y = 0
    while(x<len(ans)):
        while(y<len(ans[x])):
            z = ans[x][y]
            z %= 26
            output += alphabet[z]
            y+=1
        x+=1
        y=0
print(output)
