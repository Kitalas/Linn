# exp1
def reverse_generator(lst):
    for item in reversed(lst):
        yield item

# exp2
def even_squares_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num
def even_squares_list(numbers):
    squares = []
    for num in numbers:
        if num % 2 == 0:
            squares.append(num * num)
    return squares

# exp 3
def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num*0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1