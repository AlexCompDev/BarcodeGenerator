# Генератор штрих-кодов


Этот проект представляет собой генератор уникальных штрих-кодов. Он позволяет создавать штрих-коды, состоящие из различных компонентов, включая версию, алккод, джобкод, номер марки в заявке и криптографическую подпись.


## Описание


Генератор создает штрих-коды в следующем формате:


- **Версия**: 3 символа (например, "22N")

- **Алккод**: 13 символов в формате base36

- **Джобкод**: 12 символов, включающий:

  - 4 символа кода организации (в формате base36)

  - Последняя цифра года

  - Месяц (2 цифры)

  - День (2 цифры)

  - Номер задачи (3 цифры)

- **Номер марки в заявке**: 6 символов

- **Криптографическая подпись**: 31 символ
