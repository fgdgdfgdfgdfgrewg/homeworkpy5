## Новая функциональность

### Поддержка новых форматов данных
- Чтение транзакций из CSV-файлов: `read_csv(file_path)`
- Чтение транзакций из Excel-файлов: `read_excel(file_path)`

### Пример использования
```python
from src.file_handlers import read_csv, read_excel

csv_data = read_csv("data/transactions.csv")
excel_data = read_excel("data/transactions_excel.xlsx")

### Проверочные команды:

1. Запуск тестов:
```bash
pytest --cov=src/file_handlers.py

flake8 src/file_handlers.py

mypy src/file_handlers.py

isort src/file_handlers.py