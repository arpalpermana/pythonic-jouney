# math module


def add(*args):
    return sum(args)


def multiplyall(*args):
    result = 1
    for number in args:
        result *= number
    return result


def powering(number: int) -> int:
    return lambda n: number**n
