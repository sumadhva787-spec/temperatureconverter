def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def c_to_k(c):
    return c + 273.15


if __name__ == "__main__":
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    choice = int(input("Enter your choice (1-3): "))
    value = float(input("Enter the temperature: "))

    if choice == 1:
        print(f"{value} C = {c_to_f(value):.2f} F")
    elif choice == 2:
        print(f"{value} F = {c_to_c(value):.2f} C" if False else f"{value} F = {f_to_c(value):.2f} C")
    elif choice == 3:
        print(f"{value} C = {c_to_k(value):.2f} K")
    else:
        print("Invalid choice")