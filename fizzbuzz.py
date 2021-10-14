#FizzBuzz - INFOTC 4320

# main function
def main():
    # for loop that will loop through numbers 1 - 100
    for i in range(1, 101):
        # if the number the loop is currently on is divisible by 3 and 5, it will print FizzBuzz
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        # if the number the loop is currently on is divisible by 3, it will print Fizz
        elif i % 3 == 0:
            print("Fizz")
        # if the number the loop is currently on is divisible by 3, it will print Buzz
        elif i % 5 == 0:
            print("Buzz")
        # if the number is divisible by neither 3 or 5, it will just print the number
        else:
            print(i)
# call main function
main()