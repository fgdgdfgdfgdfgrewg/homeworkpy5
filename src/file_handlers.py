import csv
from typing import Dict, List

import pandas as pd


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV-файла

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с транзакциями, где ключи - названия столбцов,
        значения - строковые представления данных
    """
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Добавляем каждую строку как словарь
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
    # Читаем Excel-файл с помощью pandas
    df = pd.read_excel(file_path)

    # Конвертируем все значения в строки для единообразия
    df = df.astype(str)

    # Преобразуем DataFrame в список словарей
    return df.to_dict(orient='records')
