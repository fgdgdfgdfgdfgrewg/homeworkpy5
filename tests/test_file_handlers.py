import unittest
from unittest.mock import patch, mock_open
from src.file_handlers import read_csv, read_excel
import pandas as pd


class TestFileHandlers(unittest.TestCase):

    def test_read_csv(self):
        """Тестирование чтения CSV файла"""
        # Подготавливаем тестовые данные CSV
        csv_data = "id,amount,date\n1,100.50,2023-01-01\n2,200.75,2023-01-02"

        # Используем mock для имитации файла
        with patch('builtins.open', mock_open(read_data=csv_data)):
            result = read_csv("dummy.csv")

            # Проверяем результаты
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0], {"id": "1", "amount": "100.50", "date": "2023-01-01"})
            self.assertEqual(result[1], {"id": "2", "amount": "200.75", "date": "2023-01-02"})

    @patch('pandas.read_excel')
    def test_read_excel(self, mock_read_excel):
        """Тестирование чтения Excel файла"""
        # Создаем mock DataFrame
        mock_df = pd.DataFrame({
            'id': [1, 2],
            'amount': [150.75, 200.50],
            'date': ['2023-01-01', '2023-01-02']
        })
        mock_read_excel.return_value = mock_df

        # Вызываем функцию
        result = read_excel("dummy.xlsx")

        # Проверяем результаты (все значения должны быть строками)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], {"id": "1", "amount": "150.75", "date": "2023-01-01"})
        self.assertEqual(result[1], {"id": "2", "amount": "200.5", "date": "2023-01-02"})


if __name__ == '__main__':
    unittest.main()
