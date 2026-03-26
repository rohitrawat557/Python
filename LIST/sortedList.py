a = [12,13,14,15,16]

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("List is sorted")