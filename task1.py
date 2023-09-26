try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * 1.5 * rate
    print("The total salary is:", salary)
except ValueError:
    print("Error, please enter numeric input.")
