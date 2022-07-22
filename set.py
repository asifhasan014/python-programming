s={1,2,3,4,2}
s.add(5)
print(s)
s.remove(3)
s.discard(5)
print(s)
l=[1,2,3,4,5,6,5,5,4,6,7,8,9]
s2 = set(l)
print(s2)
l2= list(s2)
print(l2)
#union
union_set = s | s2
print(union_set)
#intersection of two set
intersect = s & s2
print(intersect)

#set comprehention
s3 = {i+1 for i in range(1,11)}
print(s3)
