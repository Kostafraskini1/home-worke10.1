from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for i in data_card:
        if i.isalpha():
            text_result += i
        elif i.isalpha():
            digit_count += 1
            digit_result += i
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"

print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_str: str) -> str:
    """Функция принимает строку и возвращает дату в формате ДД.MM.ГГГГ"""
    date_slice = date_str[0:10].split("-")
    return ".".join(date_slice[::-1])
