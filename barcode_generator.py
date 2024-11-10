import random


def generate_barcode():
    # Версия (3 символа)
    version = "22N"

    # Алккод в base36 (13 символов)
    alkcode_base10 = random.randint(0, 36**13 - 1)
    alkcode_base36 = convert_base10_to_base36(alkcode_base10)
    alkcode = alkcode_base36.ljust(13, "0")  # Ensure exactly 13 characters

    # Джобкод (12 символов)
    org_code_base10 = random.randint(0, 36**4 - 1)
    org_code_base36 = convert_base10_to_base36(org_code_base10)
    org_code = org_code_base36.ljust(4, "0")  # Ensure exactly 4 characters
    year_digit = str(random.randint(0, 9))  # Last digit of the year
    month = str(random.randint(1, 12)).zfill(2)  # Month (2 digits)
    day = str(random.randint(1, 28)).zfill(2)  # Day (2 digits)
    task_number = str(random.randint(1, 999)).zfill(3)  # Task number (3 digits)
    jobcode = org_code + year_digit + month + day + task_number  # Total 12 characters

    # Номер марки в заявке (6 символов)
    mark_number = str(random.randint(0, 999999)).zfill(6)

    # Криптографическая подпись (31 символ)
    signature = "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(31)
    )

    # Сборка штрих-кода
    barcode = version + alkcode + jobcode + mark_number + signature
    return barcode


def convert_base10_to_base36(n):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base36 = ""
    while n > 0:
        n, remainder = divmod(n, 36)
        base36 = alphabet[remainder] + base36
    return base36


# Генерация штрих-кода
try:
    barcode = generate_barcode()
    print(barcode)
except ValueError as e:
    print(f"Error: {e}")
