# Test Report Parser

Скрипт для получения отчёта голосового робота, извлечения уникальных номеров телефонов, генерации Excel-файла и отправки его на почту.

---

## Цель проекта

Автоматически:
1. Получать отчёт через API `test_report`
2. Собирать **уникальные** номера телефонов (`msisdn`)
3. Создавать Excel-файл
4. Отправлять файл на почту `ykuzmin@fromtech.ru`
5. Уведомлять о процессе и ошибках в Telegram-бот

---

## Алгоритм работы
![Алгоритм работы](mermaid-diagram.svg)

## Как запустить 
### 1. Клонировать репозиторий

```Bash
git clone https://github.com/dinmukhamed1729/tz_report_parser.git
cd tz_report_parser
```

### 2. Установить зависимости
```Bash
pip install -r requirements.txt
```

### 3. Настроить переменные окружения

```Bash
cp .env.example .env
```

### 4. Запустить скрипт
```bash
python main.py
```