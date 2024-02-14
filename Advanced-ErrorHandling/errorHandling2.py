# Error handling selection/match
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Something error happen!: {err}")

print(sum('1',2))

# Error msg binding
def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"Something error happen!: {err}")

print(sum(3,'0'))