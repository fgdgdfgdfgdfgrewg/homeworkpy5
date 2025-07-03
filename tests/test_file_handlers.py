import unittest
from unittest.mock import patch, mock_open
from src.file_handlers import read_csv, read_excel
import pandas as pd


class TestFileHandlers(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="id,amount,date\n1,100.50,2023-01-01")
    @patch("csv.DictReader")
    def test_read_csv(self, mock_dict_reader, mock_file):
        mock_dict_reader.return_value = [{"id": "1", "amount": "100.50", "date": "2023-01-01"}]
        result = read_csv("dummy.csv")
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0]["amount"], 100.50)

    @patch("pandas.read_excel")
    def test_read_excel(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'id': [1, 2],
            'amount': [150.75, 200.50],
            'date': ['2023-01-01', '2023-01-02']
        })
        mock_read_excel.return_value = mock_df
        result = read_excel("dummy.xlsx")
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0]["amount"], 150.75)


if __name__ == "__main__":
    unittest.main()
