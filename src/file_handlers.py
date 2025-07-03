import csv
from typing import Dict, List

import pandas as pd


def read_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с транзакциями
    """
    transactions = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Конвертация числовых полей при необходимости
            if 'amount' in row:
                row['amount'] = float(row['amount'])
            transactions.append(row)
    return transactions


def read_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
