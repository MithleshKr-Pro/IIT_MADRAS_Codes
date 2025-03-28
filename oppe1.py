no_of_rows = int(input())

initial_space_count = 0
between_space_count = no_of_rows*2 -3
for i in range(no_of_rows):
    for j in range(initial_space_count):
        print(" ",end="")
    if i == no_of_rows-1:
        print("v")
        break
    print("\\", end="")
    
    for j in range(between_space_count):
        print(" ", end = "")
    
    print("/")
    between_space_count -=2
    initial_space_count +=1
    


    
