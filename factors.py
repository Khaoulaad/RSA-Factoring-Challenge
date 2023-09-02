import sys

def factorize(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
        if number == 1:
            break
    return factors

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as file:
        for line in file:
            number = int(line)
            factors = factorize(number)
            factors_str = '*'.join(map(str, factors))
            print(f"{number}={factors_str}")

except FileNotFoundError:
    print(f"File '{sys.argv[1]}' not found.")
except ValueError:
    print("Invalid number in the file.")

