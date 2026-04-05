# # *args 
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
    
#     print(sum)

# addition(12,34,56,78)


# # **kwargs
def information(**kwargs):
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name = "Rohit", age = 21, designation = "AI/ML")