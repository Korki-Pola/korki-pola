
def get_change(money: float, price: float, denomination_table: list[float]) -> list[tuple[int, float]]:
    change_value = money - price

    print(f'change_value: {change_value}')

    denomination_table.sort(reverse=True)

    lowest_denomination = denomination_table[len(denomination_table) - 1]
    change: list[tuple[int, float]] = []
    index = 0
    while change_value >= lowest_denomination:
        denomination = denomination_table[index]
        amount = int(change_value // denomination)

        if amount != 0:
            change.append((amount, denomination))
            change_value = round(change_value - amount * denomination, 2)

        index += 1

    return change


nominaly = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.01, 0.02, 0.05]
price = 500.24
money = 728

print(get_change(money, price, nominaly))
