import uuid

def generate_transaction_id():
    # Генерация уникального идентификатора транзакции с помощью модуля uuid
    return str(uuid.uuid4())


def validate_card(card_number):
    """
    Проверяет, что номер карты содержит только цифры и имеет правильный формат.
    """
    # Проверяем, что номер карты содержит только цифры
    if not card_number.isdigit():
        return False

    # Проверяем, что номер карты имеет правильный формат (16 цифр)
    if len(card_number) != 16:
        return False

    return True
