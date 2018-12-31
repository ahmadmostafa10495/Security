key = input()
s = 56
i=0
pbox =[57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26,
       18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52,
       44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46,
       38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5,
       28, 20, 12, 4 ]
n = 64
input_table = key
binary_input_table = bin(int(input_table, 16))[2:].zfill(n)
output = ""
for p in pbox:
    output+=binary_input_table[p-1]
i = 0
to_be_shifted= output
this_key=""
rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
while(i<16):
    left = to_be_shifted[:28]
    right = to_be_shifted[28:]
    #print(left+right)
    """if((rotations[i]) == 1):
        print(to_be_shifted)
        to_be_shifted = pep[1:] + pep[0]
        print(to_be_shifted)
    else:
        print(to_be_shifted)
        to_be_shifted = pep[2:] + pep[0] + pep[1]
        print(to_be_shifted)"""
    left = left[(rotations[i]):]+left[:(rotations[i])]
    right = right[(rotations[i]):]+right[:(rotations[i])]
    to_be_shifted = left + right
    s = 48
    pbox =[14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23,
           19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52,
           31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49,
           39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    n = 56
    binary_input_table = to_be_shifted
    output = ""
    for p in pbox:
        output+=binary_input_table[p-1]
    k = hex(int(output, 2))[2:].zfill(12)
    k = k.upper()
    print(k)
    i+=1
                                  
