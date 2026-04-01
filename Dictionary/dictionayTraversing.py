# d = {10:100,20:200,30:300,40:400,50:500}


# for i in d:
#     print(d[i])

d = {10:100,20:200,30:300,40:400}

# b = d  # deep copy

d2 = d.copy()  # shallow copy
d2[10] = 1000
print(d)
