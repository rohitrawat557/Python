l = [50,40,10,20,70,10,90]
greatest = l[0]
index = 0 

for i in range(len(l)):
    if l[i]>greatest:
        greatest = l[i]
        index = i

print(f"Greatest element in the list is: {greatest} at index {index}")