def multiply(a, b):
    return a * b

def main():
    print("Welcome to the multiplication program!")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = multiply(a, b)
    print(f"The result of {a} * {b} is {result}")

if __name__ == "__main__":
    main()
