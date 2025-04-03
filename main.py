import sys

# Task 1. Division error decorator
def check_division_error(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            print(
                f"[ERROR]: Expected numerical values, but got {', '.join([type(arg).__name__ for arg in args])}")
            sys.exit(1)
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"[ERROR]: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR]: {e}")
            sys.exit(1)
        else:
            return result

    return wrapper


# Task 2. Check index decorator
def check_index_error(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], list):
            print(f"[ERROR]: Expected a list, but got {type(args[0]).__name__}")
            sys.exit(1)
        try:
            result = func(*args, **kwargs)
        except IndexError as e:
            print(f"[ERROR]: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR]: {e}")
            sys.exit(1)
        else:
            return result

    return wrapper


# Task 3. Testing division func
@check_division_error
def divide_numbers(a, b):
    return a / b

print(divide_numbers(1, 2))
# print(divide_numbers(1, 0))
# print(divide_numbers(0))
# print(divide_numbers('15', 'abc'))

print("-" * 20)


# Task 4. # Task 3. Testing index func
@check_index_error
def check_listed_items_index(lst, index):
    return lst[index]

some_list = [5, 10, 13, 23, 24, 234]
print(check_listed_items_index(some_list, 1))
# print(check_listed_items_index(some_list, 10))

some_dict = {}
# print(check_listed_items_index(some_dict, 13))
