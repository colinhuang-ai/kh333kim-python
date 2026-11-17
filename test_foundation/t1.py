# question 14
# function 1
def process(a: int, b: int) -> int:
    # only use in this function
    # if a > 10 then a reset = 10
    # call 1: a = 3, b = 20
    # call 2: a = 4, b = 5
    if a > 10:
        a = 10
    b = b + a
    return b

# function 2
def main():
    # define two variables, only use in this function   
    a = 20
    b = 3

    # pass only values to the function
    b = process(b, a) # b = 3 + 20 = 23, process(3, 20)
    print(a, b) # 20 23

    # pass only variables to the function
    c = process(4, 5) # c = 5 + 4 = 9
    print(c) # 9

# call the main function
main()

# question 1
# false/true --> boolean
print(type(False), type(4.5 * 2), type(["apple", "banana", "cherry"]))

