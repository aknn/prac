
example = ['left','right','up','down']
example_dict = {'left':'<','right':'>','up':'^','down':'v',}
for i,j in enumerate(example):
    print(i,j)
print("----------")
[print(i,j) for i,j in enumerate(example_dict)]


print("----------")
x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

#Let's first combine x and y:

for a,b in zip(x,y):
    print(a,b)

print("----------")
print(list(zip(x,y,z)))


print("----------")
names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(zip(names,grades))
print(d)