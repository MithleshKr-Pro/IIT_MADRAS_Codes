l1 = [[1,2],[3,4]]
l2 = [[2,1],[3,5]]
lProd = []
col=-1;
for i in range(len(l1)):
    while col < len(l2[i]):
        col += 1
        lProd.append([0] * len(l2[0]))
        for j in range(len(l1)):        
            lProd[i][col] += l1[i][j]*l2[j][col]
    col = -1
print(lProd) 