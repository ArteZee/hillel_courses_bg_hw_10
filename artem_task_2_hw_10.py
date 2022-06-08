import ast


# decorator launch function
def decoration_func(func):
    def wrapper(method: type):
        func(method)
        len_of_method: int = len(dir(method))
        print("Total methods:",len_of_method)

    return wrapper


# get users object
user_input: str = input("Please input your object: ")
# get type of obj
type_user_input = type(ast.literal_eval(user_input))


@decoration_func
def methods(method: type):
    """
    function output the list of not magic methods
    :param method: type of user object
    :return: list of not magic methods 
    """
    user_method: list = dir(method)
    lst_of_method_dir: list = []

    for i in user_method:
        if i.startswith("_"):
            continue
        else:
            lst_of_method_dir.append(i)
    print("Not magic methods are:", lst_of_method_dir)


methods(type_user_input)

user_input: str = input("Please input your object: ")
type_user_input: type = type(ast.literal_eval(user_input))


# @decorate_func
def methods_2(method: type):
    user_method = dir(method)
    lst_of_method_dir = []
    for i in user_method:
        if i.startswith("_"):
            continue
        else:
            lst_of_method_dir.append(i)
    print("Not magic methods are:", lst_of_method_dir)


methods_2(type_user_input)
