# def decorate(func):
#     def wrapper(a,b):
#         print("The addition to your numbers are ")
#         func(a,b)
#         print("Thankyou I hope you liked it ")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"Your sum is {a+b}")

# addition(12,68)



# # use of args and kwargs in decorator
def decorate(func):
    def wrapper(*args,**kwargs):
        print("The addition to your numbers are ")
        func(*args,**kwargs)
        print("Thankyou I hope you liked it ")
    return wrapper


@decorate
def addition(a,b):
    print(f"Your sum is {a+b}")

addition(12,68)