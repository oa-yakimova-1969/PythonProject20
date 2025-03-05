from typing import Iterable, Any
from datetime import datetime

#def filter_by_state(transactions: Iterable[list[dict[str, Any]]], state: str='EXECUTED') -> Iterable[list[dict[str, Any]]]:
#    filtered_transactions = []

#    for transaction in transactions:
#       if transaction['state'] == state:
#           filtered_transactions.append(transaction)
#    return filtered_transactions

#def filter_by_state(transactions: Iterable[list[dict[str, Any]]], state: str='EXECUTED') -> Iterable[list[dict[str, Any]]]:
#    filtered_transactions = []
#   for transaction in transactions:
#        if transaction.get('state') == state:
#            filtered_transactions.append(transaction)
#    return filtered_transactions

#def sort_by_date(transactions: Iterable[list[dict[str, Any]]], reverse: bool=True) -> Iterable[list[dict[str, Any]]]:
#    sorted_transactions = sorted(transactions, key=lambda transaction: transaction.get('date'), reverse=True)
#    return sorted_transactions

def sort_by_date(transactions: Iterable[list[dict[str, Any]]], reverse: bool=True) -> Iterable[list[dict[str, Any]]]:
    sorted_transactions = sorted(transactions, key=lambda transaction: transaction['date'], reverse=True)
    return sorted_transactions

#def sort_by_date(transactions, reverse=True):
#    return sorted(transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
