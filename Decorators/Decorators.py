# Simple decorators ##########

# def multiple(a, b): # This is sample method for demo
#      return a * b

# def double_args(func): # This is the decorator method which takes in the function
#     def wrapper(a, b): # This is the wrapper function which pass arguments to the input function
#         return func(a, b) # This is the method call with the input function and arguments
#     return wrapper

# if __name__ == '__main__':
#     m = double_args(multiple) # This is the decorator call to wrapped the requested function
#     print(m(1, 5))

    ##########
    # 5 (Answers is same as calling multiple(1,5))
    ##########

##############################


# Simple decorators with modifications ##########

# def double_args(func):
#     def wrapper(a, b):
#         return func(a * 2, b * 2) # The input arguement is been modified before reaching the requested method by the decorator's wrapper
#     return wrapper

# if __name__ == '__main__':
#     m = double_args(multiple)
#     print(m(1, 5))

    ##########
    # 20 (Answers is 20 because warpper * 2 al arguements before calling the multply method)
    ##########

    # print(m.__closure__[0].cell_contents)
    ##########
    # <function multiple at 0x000002861DF92E18> # The cell content in the closure attributes holds the function requested
    ##########

##############################



# Decorators using the @ symbol ##########

def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2) # Modify input arguments before passing to requested function
    return wrapper

@double_args # This is to indicate the decorators is used on the multiple function
def multiple(a, b):
    return a * b

if __name__ == '__main__':
    m = multiple(1, 5) # No need to call double_args to wrap the multiple method as the @ declaration already done that
    print(m)

    ##########
    # 20 (Answers is 20 because warpper * 2 al arguements before calling the multply method)
    ##########

##############################