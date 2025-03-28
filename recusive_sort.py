def mini(L: list):
    mini = L[0]
    for i in L[1:]:
        if i<mini:
            mini = i
    return mini
     
L1 = [ ]       
def sort(L: list):
    # find & Remove mini
    if len(L) == 0:
        return L
    
    min = mini(L)
    L.remove(min)
    return [min] + sort(L)
        
        

print(sort([2,3,4,3,5,8]))    
    