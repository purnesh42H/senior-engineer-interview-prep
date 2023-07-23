import sys
import unittest

from collections import defaultdict

'''
Problem - https://leetcode.com/problems/optimal-account-balancing/description/
'''

class Transaction(object):

    def __init__(self, payee, borrower, amount):
        self.payee = payee
        self.borrower = borrower
        self.amount = amount

class OptimalAccountBalancer(object):
    def __init__(self, transactions) -> None:
        self.transactions = transactions

    '''
    transactions = [[0, 1, 10], [2, 0, 5]]

    borrower_debts = {1: +10, 0: +5}
    payeee_debts = {0: -10, 2: -5}

    debts = +10, +5, -10, -5, requires 2 transactions atleast to settle

    transactions = [[0, 1, 2], [2, 0, 1], [1, 3, 1]

    borrower_debts = {1: +2, 0: +1, 3: +1}
    payeee_debts = {0: -2, 2: -1, 1: -1}, requires 3 transactions

    0, 0, 0, 0, 0, 0, 

    
    [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]

    debts => 
    0: [-10, +1, +5] => -4
    1: [+10, -1, -5] => +4
    2: [+5, -5] => 0

    '''
    def minimum_transactions_to_settle_debts(self):
        if not self.transactions:
            return 0
        
        remaining_debts = self._get_remaing_non_zero_debts()

        return self._settle_debts(0, remaining_debts)

    def _get_remaing_non_zero_debts(self):
        if not self.transactions:
            return []
         
        debt_map = defaultdict(int)
        for transaction in self.transactions:
            debt_map[transaction.payee] -= transaction.amount
            debt_map[transaction.borrower] += transaction.amount

        return [x for x in debt_map.values() if x != 0]
    
    def _settle_debts(self, current_person, debts):
        while current_person < len(debts) and debts[current_person] == 0:
            current_person += 1

        if current_person >= len(debts):
            return 0
        
        min_transactions = sys.maxsize - 1
        
        for person in range(current_person + 1, len(debts)):
            if debts[current_person] * debts[person] < 0:
                debts[person] += debts[current_person]

                min_transactions = min(min_transactions, 1 + self._settle_debts(current_person + 1, debts))

                debts[person] -= debts[current_person]

        return min_transactions
        
class TestOptimalAccountBalancer(unittest.TestCase):
    
    def test_case_individual_settlement(self):
        # test case 1
        accountBalancer = OptimalAccountBalancer([Transaction(0, 1, 10), Transaction(2, 0, 5)])
        min_transactions = accountBalancer.minimum_transactions_to_settle_debts()
        self.assertEqual(2, min_transactions)

    def test_case_shared_settlement(self):
        # test case 1
        accountBalancer = OptimalAccountBalancer([Transaction(0, 1, 1), Transaction(2, 1, 1), Transaction(1, 3, 1)])
        min_transactions = accountBalancer.minimum_transactions_to_settle_debts()
        self.assertEqual(2, min_transactions)

        # test case 2
        accountBalancer = OptimalAccountBalancer([Transaction(0, 1, 10), Transaction(1, 0, 1), Transaction(2, 0, 5), Transaction(1, 2, 5)])
        min_transactions = accountBalancer.minimum_transactions_to_settle_debts()
        self.assertEqual(1, min_transactions)


if __name__ == '__main__':
    unittest.main()