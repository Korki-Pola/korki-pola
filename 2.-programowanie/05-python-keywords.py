def get_user_input(value_text: str, error_text: str) -> float:
    value = None
    value_incorrect = True
    while value_incorrect:
        try:
            value = float(input(value_text))
            value_incorrect = False

        except ValueError:
            print(error_text)

    return value


def get_user_continue() -> bool:
    decision = None
    input_incorrect = True
    while input_incorrect:
        decision = input("Czy chcesz wykonac nowe dzialanie? Y/N: ")

        if decision.upper() in ['Y', 'N']:
            input_incorrect = False
        else:
            print("Podaj Y lub N")

    if decision.upper() == 'Y':
        return True
    else:
        return False


def get_operator(operator_list: list[str]) -> str:
    operator = None
    operator_incorrect = True

    while operator_incorrect:
        operator = input(f"Podaj typ dzialania: {operator_list}: ")

        if operator in operator_list:
            operator_incorrect = False
        else:
            print("Podales zly typ operatora!!!")

    return operator


def calculate(value_one: float, value_two: float, operator: str) -> float:
    try:
        return eval(f'{value_one}{operator}{value_two}')
    except ZeroDivisionError:
        return "Proba dzielenia przez zero"


def calculator():
    flag = True
    while flag:
        value_one = get_user_input(
            "Podaj pierwsza liczbe: ", "Podales znak ktory nie jest liczba!!!")
        value_two = get_user_input(
            "Podaj druga liczbe: ", "Podales znak ktory nie jest liczba!!!")
        operator = get_operator(['+', '-', '/', '*'])

        result = calculate(value_one, value_two, operator)
        print(f'{value_one} {operator} {value_two} = {result}')

        flag = get_user_continue()


def main():
    calculator()


if __name__ == "__main__":
    main()
