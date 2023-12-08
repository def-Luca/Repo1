def fizz_buzz(input):
    if input %3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 ==0:
        print("Fizz")
    elif input %5 == 0:
        print("Buzz")
    else:
        return(input)


print(fizz_buzz(7))

# varianta mai cleannnnnn


def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return"Buzz"

    return input

print(fizzbuzz(23))