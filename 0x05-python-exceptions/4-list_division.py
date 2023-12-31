#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if (isinstance(my_list_1[i], (int, float)) is False):
                raise TypeError("wrong type")

            if (isinstance(my_list_2[i], (int, float)) is False):
                raise TypeError("wrong type")

            if (my_list_2[i] == 0):
                raise ZeroDivisionError("division by 0")

            if (i >= len(my_list_1) or i >= len(my_list_2)):
                raise IndexError("out of range")

            quot = my_list_1[i]/my_list_2[i]
            result.append(quot)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass

    return result
