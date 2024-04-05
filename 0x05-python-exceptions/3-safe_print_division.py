#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: DIvision by zero")
        return None
    except exception as e:
        print("Inside result: {}".format(e))
        return None
    else:
        print("inside result: {:.1f}".format(result))
        return result
    finally:
        print("Iinside result: finally")
