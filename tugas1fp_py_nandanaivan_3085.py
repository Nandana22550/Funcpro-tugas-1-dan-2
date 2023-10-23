#Kode 1
sequenceGenerator = lambda start, stop: list(range(start, stop + 1)); print(sequenceGenerator(1, 10))

#Kode 2
fizzBuzz = lambda a, b: ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(a, b)]

#Kode 3
twoNumber = lambda lst: [lst[i] + lst[i+1] for i in range(len(lst) - 1)]


