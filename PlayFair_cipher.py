alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

#no j

# Initialize a 5 by 5 table of stars
table = []

def print_table():
    for row in range(5):
        for col in range(5):
            print(table[row][col],end="")
        print("")

def clear_table():
    global table
    table = []
    for row in range(5):
        table.append([])
        for col in range(5):
            table[row].append("*")

# This was added by
def find_letter(letter):
        for row in range(5):
            for col in range(5):
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
    letter= "I" if letter == "J" else letter
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
    while(1):
        if(i == (len(plain_text)-1)):
            if(plain_text[i] == 'X'):
                token = plain_text[i] + "Q"
                list_of_tokens.append(token)
                break
            token = plain_text[i] + "X"
            list_of_tokens.append(token)
            break
        elif(plain_text[i] == plain_text[i+1]):
            if(plain_text[i] == 'X'):
                token = plain_text[i] + "Q"
                list_of_tokens.append(token)
                i+=1
                continue
            token = plain_text[i] + "X"
            list_of_tokens.append(token)
            i+=1
            continue
        else:
            token = plain_text[i] + plain_text[i+1]
            list_of_tokens.append(token)              
            i+=2
            if(i == (len(plain_text))):
                break
            continue
    return list_of_tokens
        



#start dealing with input
key = input()
i=0
while(i<len(key)):
    if(key[i]=="J"):
        key = key[:i] +"I"+key[i+1:]
    i+=1
i=0    
plain = input()
while(i<len(plain)):
    if(plain[i]=="J"):
        plain = plain[:i] +"I"+plain[i+1:]
    i+=1

create_table(key)
tokens = plain_handling(plain)
output=""
for token in tokens:
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
print(output)    


