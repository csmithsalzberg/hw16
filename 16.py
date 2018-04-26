#Caleb Smith-Salzberg, Shaina Peters
#SoftDev2 pd7
#K16 -- Ready, Set, Math!
#2018-04-27

def union(a,b):
    return a + [x for x in b if x not in a]

print union([1,2,3],[2,3,4]) #[1,2,3,4]

def intersection(a,b):
    return [x for x in a if x in b]
    
print intersection([1,2,3],[2,3,4]) #[2,3]

def setDifference(a,b):
    return [x for x in a if x not in b]
    
print setDifference([1,2,3],[2,3,4]) #1

def symDifference(a,b):
    return [x for x in a if x not in b] + [x for x in b if x not in a]

print symDifference([1,2,3],[2,3,4]) #[1,4]

def cartProduct(a,b):
    return [(x,y) for x in a for y in b]
    
print cartProduct([1,2],['red','white'])
