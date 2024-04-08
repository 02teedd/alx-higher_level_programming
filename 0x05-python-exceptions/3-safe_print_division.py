#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: division by zero")
        return None
    except Exception as e:
        print("Inside result: {}".format(e))
        return None
    else:
        print("{} / {} = {:.1f}".format(a, b, result))
        print("Inside result: {:.1f}".format(result))
        return result
    finally:
        print("Inside result: finally")
