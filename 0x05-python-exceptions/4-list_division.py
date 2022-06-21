#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        division = my_list_1[i] / my_list_2[i]
    except TypeError:
        division = None
        print("wrong type")
    except ZeroDivisionError:
        division = None
        print("division by 0")
    except Exception as IndexError:
        division = None
        print("out of range")
    finally:
        result.append(division)

    return response
