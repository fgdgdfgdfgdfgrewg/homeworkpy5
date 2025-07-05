import csv
from typing import Dict, List, cast

import pandas as pd
from pandas.core.frame import DataFrame


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV-файла

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с транзакциями, где ключи - названия столбцов,
        значения - строковые представления данных
    """
    transactions: List[Dict[str, str]] = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        # Явное указание разделителя - запятой
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            transactions.append(dict(row))
    return transactions


def read_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из Excel-файла

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список словарей с транзакциями, где ключи - названия столбцов,
        значения - строковые представления данных
    """
    df: DataFrame = pd.read_excel(file_path)
    df = df.astype(str)
    records = df.to_dict(orient='records')
    return cast(List[Dict[str, str]], records)