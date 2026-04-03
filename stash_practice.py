def decorator_1(func):
    def wraper(*args):
        #here i want to write teh logic of sum of add numbers
        sum=0
        for n in args:
            sum+=n
        print("the sum is",sum)
        return func(args)
    return wraper

@decorator_1
def add_numbers(*args):
    print("the numbers are:",args)
add_numbers(1,2,3,4,5)



