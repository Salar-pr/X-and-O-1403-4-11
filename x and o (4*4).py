jadval = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def create_X_O_table(jadval):
    
    

    for i in range(0, len(jadval), 4):
        

        
        
        print(jadval[i:i + 4])
    return jadval 

create_X_O_table(jadval)
count = 0
while True:
    
    count += 1

    if count % 2 == 0:
        a = int(input(" X choose your indax for x: "))
        
        c = a

        jadval[c] = "X"
        
    else:
        a = int(input(" O choose your indax for o: "))
        
        c = a
        jadval[c] = "O"
    create_X_O_table(jadval)

    if jadval[0] == "X" and jadval[1] == "X" and jadval[2] == "X" and jadval[3]:
        print("X win")
        break
    if jadval[0] == "X" and jadval[5] == "X" and jadval[10] == "X" and jadval[15]:
        print("X win")
        break
    if jadval[0] == "X" and jadval[4] == "X" and jadval[8] == "X" and jadval[12]:
        print("X win")
        break
    if jadval[1] == "X" and jadval[5] == "X" and jadval[9] == "X" and jadval[13]:
        print("X win")
        break
    if jadval[2] == "X" and jadval[6] == "X" and jadval[10] == "X" and jadval[14]:
        print("X win")
        break    
    if jadval[3] == "X" and jadval[7] == "X" and jadval[11] == "X" and jadval[15]:
        print("X win")
        break
    if jadval[3] == "X" and jadval[6] == "X" and jadval[9] == "X" and jadval[12]:
        print("X win")
        break
    if jadval[4] == "X" and jadval[5] == "X" and jadval[6] == "X" and jadval[7]:
        print("X win")
        break
    if jadval[8] == "X" and jadval[9] == "X" and jadval[10] == "X" and jadval[11]:
        print("X win")
        break
    if jadval[12] == "X" and jadval[13] == "X" and jadval[14] == "X" and jadval[15]:
        print("X win")
        break



    if jadval[0] == "O" and jadval[1] == "O" and jadval[2] == "O" and jadval[3]:
        print("O win")
        break
    if jadval[0] == "O" and jadval[5] == "O" and jadval[10] == "O" and jadval[15]:
        print("O win")
        break
    if jadval[0] == "O" and jadval[4] == "O" and jadval[8] == "O" and jadval[12]:
        print("O win")
        break
    if jadval[1] == "O" and jadval[5] == "O" and jadval[9] == "O" and jadval[13]:
        print("O win")
        break
    if jadval[2] == "O" and jadval[6] == "O" and jadval[10] == "O" and jadval[14]:
        print("O win")
        break    
    if jadval[3] == "O" and jadval[7] == "O" and jadval[11] == "O" and jadval[15]:
        print("O win")
        break
    if jadval[3] == "O" and jadval[6] == "O" and jadval[9] == "O" and jadval[12]:
        print("O win")
        break
    if jadval[4] == "O" and jadval[5] == "O" and jadval[6] == "O" and jadval[7]:
        print("O win")
        break
    if jadval[8] == "O" and jadval[9] == "O" and jadval[10] == "O" and jadval[11]:
        print("O win")
        break
    if jadval[12] == "O" and jadval[13] == "O" and jadval[14] == "O" and jadval[15]:
        print("O win")
        break


    