dict_new = {}


#decoraratore see use we function with argument or not
def decorater(func):
    def wrapper(*elements):

        if elements in dict_new.keys():
            print(dict_new.get(elements))

        else:
            func(*elements)
            print(dict_new.get(elements))

    return wrapper


@decorater
def foo(*elements):
    """
    function give key is argument; value - summarize of argument
    :param elements: int and float
    :return: int: summarize of argument
    """
    list_elem_count = list(elements)
    summ_elem = sum(list_elem_count)
    dict_new[elements] = summ_elem
    return summ_elem


foo(1, 2, 3, 4, 5)
foo(1, 2, 3, 4, 5 )
foo(1, 2, 3, 4, 5)
foo(1, 2, 3, 4, 5)
foo(5, 23, 4, 5, 67)
foo(5, 23, 4, 5, 67)
foo(1, 2, 3, 4, 5)
foo(5, 23, 4, 5, 67)
foo(5, 23, 4, 5, 67)
print(dict_new)
