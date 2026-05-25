def clean_phone(phone: str) -> str:
    """Очистка номера телефона"""
    if not phone:
        return ""
    cleaned = ''.join(filter(str.isdigit, str(phone)))
    if len(cleaned) == 10:
        return "7" + cleaned
    return cleaned