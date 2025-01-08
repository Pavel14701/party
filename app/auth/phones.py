import phonenumbers
from phonenumbers import NumberParseException

def validate_and_format_phone_number(phone_number: str, country_code: str) -> str:
    """## Проверяет и форматирует номер телефона.
    Анализирует, проверяет и форматирует номер телефона в соответствии с предоставленным кодом страны.
    ## Аргументы:
        :class:`phone_number:` номер телефона для проверки и форматирования.
        :class:`Country_code:` двухбуквенный код страны (например, «США», «RU»).
    ## Возврат:
        Отформатированный номер телефона в формате E164.
    ## Исключения:
        :class:`ValueError:` Если номер телефона недействителен или не может быть проанализирован.
    """
    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            raise ValueError("Invalid phone number")
    except NumberParseException as e:
        raise ValueError(f"Error parsing phone number: {e}") from e