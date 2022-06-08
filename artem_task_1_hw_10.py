def user_number():
    end_number: str = input("Введите свой номер телефона: ")
    list_number: list = list(end_number)
    list_number.pop(0)
    ready_end_number = "".join(list_number)

    def code_country():
        ready_number: str = "+380" + ready_end_number
        return ready_number

    return code_country()


telefone_number = user_number()

print(telefone_number)
