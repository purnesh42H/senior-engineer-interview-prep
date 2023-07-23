import unittest
import sys

'''
Problem - https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
'''

'''
customers = "YYNY"
             c      yes_customers_after = 3, no_customers_before = 0, minimum_penalty = 3
              c      yes_customers_after = 2, no_customers_before = 0, minimum_penalty = 2
                c      yes_customers_after = 1, no_customers_before = 0, minimum_penalty = 1
                 c      yes_customers_after = 1, no_customers_before = 1, minimum_penalty = 2
                  c      yes_customers_after = 0, no_customers_before = 1, minimum_penalty = 1


'''
class PenaltyCalculator(object):

    def get_minimum_penalty_closing_hour(self, customers):
        if not customers:
            return 0
        
        yes_customers_after = self._get_customers_incoming_counts(customers=customers)
        no_customers_before = 0
        minimum_penalty = sys.maxsize - 1
        hour_of_minimum_penalty = -1

        for i in range(len(customers)):
            if minimum_penalty > yes_customers_after + no_customers_before:
                minimum_penalty = yes_customers_after + no_customers_before
                hour_of_minimum_penalty = i

            if customers[i] == "Y":
                yes_customers_after -= 1

            if customers[i] == "N":
                no_customers_before += 1


        if minimum_penalty > yes_customers_after + no_customers_before:
             minimum_penalty = yes_customers_after + no_customers_before
             hour_of_minimum_penalty = len(customers)

        return hour_of_minimum_penalty

    def _get_customers_incoming_counts(self, customers):
        yes_customers = 0

        for customer in customers:
            if customer == "Y":
                yes_customers += 1

        return yes_customers


class PenaltyCalculatorTest(unittest.TestCase):

    def test_mix_of_yes_and_no(self):
        penaltyCalculator = PenaltyCalculator()
        
        customers = "YYNY"
        self.assertEqual(2, penaltyCalculator.get_minimum_penalty_closing_hour(customers))

        '''
        YNNYYYNY
        c           yes_customers_after = 5, no_customers_before = 0, minimum_penalty = 5
         c          yes_customers_after = 4, no_customers_before = 0, minimum_penalty = 4
          c         yes_customers_after = 4, no_customers_before = 1, minimum_penalty = 5
           c        yes_customers_after = 4, no_customers_before = 2, minimum_penalty = 6
            c       yes_customers_after = 3, no_customers_before = 2, minimum_penalty = 5
             c      yes_customers_after = 2, no_customers_before = 2, minimum_penalty = 4
              c     yes_customers_after = 1, no_customers_before = 2, minimum_penalty = 3
               c    yes_customers_after = 1, no_customers_before = 3, minimum_penalty = 4
                c   yes_customers_after = 0, no_customers_before = 3, minimum_penalty = 3
        '''
        customers = "YNNYYYNY"
        self.assertEqual(6, penaltyCalculator.get_minimum_penalty_closing_hour(customers))

    def test_all_yes(self):
        penaltyCalculator = PenaltyCalculator()

        customers = "YYYYY"
        self.assertEqual(5, penaltyCalculator.get_minimum_penalty_closing_hour(customers))

    def test_all_no(self):
        penaltyCalculator = PenaltyCalculator()

        customers = "NNNNN"
        self.assertEqual(0, penaltyCalculator.get_minimum_penalty_closing_hour(customers))


if __name__ == '__main__':
    unittest.main()