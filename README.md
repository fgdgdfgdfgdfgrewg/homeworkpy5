## Новая функциональность: Поддержка CSV и Excel форматов

Теперь приложение поддерживает чтение финансовых транзакций из CSV и Excel файлов.

### Доступные функции

#### `read_csv(file_path: str) -> List[Dict]`
- **Описание**: Считывает финансовые операции из CSV-файла
- **Параметры**:
  - `file_path`: Путь к CSV-файлу
- **Возвращает**: Список словарей, где каждый словарь представляет одну транзакцию
- **Пример использования**:
  ```python
  from src.file_handlers import read_csv
  
  transactions = read_csv("data/transactions.csv")
  for transaction in transactions:
      print(f"ID: {transaction['id']}, Amount: {transaction['amount']}, Date: {transaction['date']}")