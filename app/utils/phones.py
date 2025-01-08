import phonenumbers
from phonenumbers import NumberParseException

def validate_and_format_phone_number(phone_number: str, country_code: str) -> str:
    try:
        # Парсинг номера телефона в зависимости от кода страны
        parsed_number = phonenumbers.parse(phone_number, country_code)
        # Проверка валидности номера телефона
        if phonenumbers.is_valid_number(parsed_number):
            # Форматирование номера в международном формате (E164)
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            raise ValueError("Invalid phone number")
    except NumberParseException as e:
        raise ValueError(f"Error parsing phone number: {e}") from e
