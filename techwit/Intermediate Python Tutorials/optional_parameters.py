# Optional Parameters Tutorial #1

def func(x=5): # This default value is the Optional Parameter
    return x **2

call = func(6) # This Parameter '6' placed in the function will override the Optional Parameter in the Method defined...
print(call)


def func2(word, freq=5): # Again this default value makes this an Optional Parameter
    print(word*freq)

call = func2('dexter', 2)


# Multiple Optional Parameters

def func3(word, add=4, freq=2):
    print(word*(freq+add))

call = func3('Hello')