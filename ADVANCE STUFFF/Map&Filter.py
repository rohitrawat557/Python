# #  map

# a = [1,2,3,4,5]
# result = map(lambda x : x**2, a)

# print(list(result))

a = [1,2,3,4,5,6,7,8,9,10]

result = filter(lambda x : True if x%2 == 0 else False, a)

print(list(result))