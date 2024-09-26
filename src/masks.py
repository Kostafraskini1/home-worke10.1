card_number = input()
account_number = input()


def get_mask_card_number(card_number: int) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""

    return f"{card_number[:4]}{card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"


print(get_mask_card_number(7000792289606361))
print(get_mask_account(7365410843013587430))
