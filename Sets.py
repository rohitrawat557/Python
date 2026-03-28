# # s = {1,2,3,4,5}

# # print(s)
# b = hash("Hello")
# print(b)

# c = hash((1,2,34))
# print(c)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
a.remove(5)
print(a)
for i in a:
    print(i)

s = a.union(b)
print(s)