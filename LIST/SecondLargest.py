l = [12,16,13,19,17]
largest = l[0]
second_largest = l[0]
index = 0

for i in range(len(l)):
    if l[i]>largest:
        second_largest = largest
        largest = l[i]
        index = i
    elif l[i]>second_largest:
        second_largest = l[i]
        index = i

print(f"Second largest element in the list is: {second_largest} at index {index}")
