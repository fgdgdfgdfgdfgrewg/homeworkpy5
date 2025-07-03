import csv
from typing import Dict, List

import pandas as pd


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV-файла

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с транзакциями (все значения строковые)
    """
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(dict(row))
    return transactions


def read_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из Excel-файла

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список словарей с транзакциями (все значения строковые)
    """
    df = pd.read_excel(file_path)
    # Конвертируем все значения в строки для единообразия
    return df.astype(str).to_dict(orient='records')
