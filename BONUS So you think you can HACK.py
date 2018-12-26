alphabet = "ABCDEFGHI"
alphabet_list = list(alphabet)
from itertools import permutations
import random
#no j

# Initialize a 3 by 3 table of stars
table = []

def print_table():
    for row in range(3):
        for col in range(3):
            print(table[row][col],end="")
        print("")

def clear_table():
    global table
    table = []
    for row in range(3):
        table.append([])
        for col in range(3):
            table[row].append("*")

# This was added by
def find_letter(letter):
        for row in range(3):
            for col in range(3):
                if table[row][col] == letter:
                    return row, col
        return -1, -1

def table_has_letter(letter):
    return find_letter(letter)[0] != -1
    # Write code here to search the table for the given letter
    # and return True or False depending on if the letter exists

def table_next_opening():
    return find_letter("*")

def table_insert_letter(letter):
    letter=letter.upper()
    if letter in alphabet and not table_has_letter(letter):
        open_pos= table_next_opening()
        table[open_pos[0]][open_pos[1]] = letter
        ww = open_pos
        return (ww)

def create_table(secret):
    clear_table()
    for letter in secret:
        table_insert_letter(letter)
    for ex_letter in  alphabet:
        table_insert_letter(ex_letter)

def plain_handling(plain_text):
    list_of_tokens = []
    i=0
    while(i < (len(plain_text)-1)):
            token = plain_text[i] + plain_text[i+1]
            list_of_tokens.append(token)              
            i+=2
    return list_of_tokens

def cipher_handling(cipher_text):
    list_of_tokens = []
    i=0
    while(i < (len(cipher_text)-1)):
            token = cipher_text[i] + cipher_text[i+1]
            list_of_tokens.append(token)              
            i+=2
            continue
    return list_of_tokens
def make_table(key):
    table = [[0] * 3 for row in range(3)]
    counter = 0
    for row in range(3):
        for col in range(3):
            table[row][col] = key[counter]
            counter += 1
    return table

def do_the_shit(key, plaintext):
    cipher = []
    table = make_table(key)
    for i in range(0, len(plaintext), 2):
        col1 = 0
        raw1 = 0
        col2 = 0
        raw2 = 0
        for r in range(3):
            for c in range(3):
                if table[r][c] == plaintext[i]:
                    raw1 = r
                    col1 = c
                if table[r][c] == plaintext[i+1]:
                    raw2 = r
                    col2 = c
        if raw1 == raw2:
            cipher.append(table[raw1][(col1 + 1) % 3])
            cipher.append(table[raw2][(col2 + 1) % 3])
        elif col1 == col2:
            cipher.append(table[(raw1 + 1) % 3][col1])
            cipher.append(table[(raw2 + 1) % 3][col2])
        else:
            cipher.append(table[raw1][col2])
            cipher.append(table[raw2][col1])
    cipher_text = "".join(cipher)
    return cipher_text

plain = input()
cipher = input()



#tokens = plain_handling(plain)
#cipher_tokens = plain_handling(cipher)
output=""
i = 0

#ahmad = itertools.permutations(alphabet, 9)
def keys(str1):
    x = []
    perms = (p for p in permutations(str1))
    for p in perms:
        x.append(''.join(p))
    return x
all_keys = keys("ABCDEFGHI")

for key in all_keys:
    result = (do_the_shit(key, plain))
    if result == cipher:
        print(key)
        break












"""#while(1):
        #random.shuffle(alphabet_list)
        #x = ''.join(alphabet_list)
        #clear_table()
        create_table(x)
        for token in tokens:
            row1,col1 = find_letter(token[0])
            row2,col2 = find_letter(token[1])
            #print(str(row1)+str(col1)+str(row2)+str(col2))
            if(row1 == row2):
                col1 += 1
                col1 %= 3
                col2 += 1
                col2 %= 3
                output+=table[row1][col1]
                output+=table[row2][col2]
                continue
            elif(col1 == col2):
                row1 += 1
                row1 %= 3
                row2 += 1
                row2 %= 3
                output+=table[row1][col1]
                output+=table[row2][col2]
                continue
            else:
                output+=table[row1][col2]
                output+=table[row2][col1]
                continue
        if(output == cipher):
            print(x)
            break



"""















"""while(i<len(tokens)):
    if(tokens[i][0] == cipher_tokens[i][1]):
        print("HELLO")
        
    elif(tokens[i][1] == cipher_tokens[i][0]):
        print("HELLO")
    else:
        print("HELLO")
    i+=1
"""





































    
"""for token in tokens:
    
    
    row1,col1 = find_letter(token[0])
    row2,col2 = find_letter(token[1])
    #print(str(row1)+str(col1)+str(row2)+str(col2))
    if(row1 == row2):
        col1 += 1
        col1 %= 5
        col2 += 1
        col2 %= 5
        output+=table[row1][col1]
        output+=table[row2][col2]
        continue
    elif(col1 == col2):
        row1 += 1
        row1 %= 5
        row2 += 1
        row2 %= 5
        output+=table[row1][col1]
        output+=table[row2][col2]
        continue
    else:
        output+=table[row1][col2]
        output+=table[row2][col1]
        continue
"""
