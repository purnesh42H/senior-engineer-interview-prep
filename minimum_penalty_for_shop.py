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

    def get_penalty(self, customers, closing_time):
        return self._get_yes_customers_after_closing_time(customers, closing_time) \
            + self._get_no_customers_before_closing_time(customers, closing_time)
    
    def get_minimum_penalty_closing_hour(self, customers):
        if not customers:
            return 0
        
        yes_customers_after = self._get_yes_customers_after_closing_time(customers, 0)
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
    
    def _get_no_customers_before_closing_time(self, customers, closing_time):
        no_before_closing_time = 0

        for i in range(0, closing_time):
            if customers[i] == "N":
                no_before_closing_time += 1

        return no_before_closing_time
    
    def _get_yes_customers_after_closing_time(self, customers, closing_time):
        yes_after_closing_time = 0

        for i in range(closing_time, len(customers)):
            if customers[i] == "Y":
                yes_after_closing_time += 1

        return yes_after_closing_time

class PenaltyCalculatorTest(unittest.TestCase):

    def test_mix_of_yes_and_no(self):
        penaltyCalculator = PenaltyCalculator()
        
        customers = "YYNY"
        self.assertEqual(2, penaltyCalculator.get_minimum_penalty_closing_hour(customers))
        self.assertEqual(2, penaltyCalculator.get_penalty(customers, 1))

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
        self.assertEqual(5, penaltyCalculator.get_penalty(customers, 2))

    def test_all_yes(self):
        penaltyCalculator = PenaltyCalculator()

        customers = "YYYYY"
        self.assertEqual(5, penaltyCalculator.get_minimum_penalty_closing_hour(customers))
        self.assertEqual(2, penaltyCalculator.get_penalty(customers, 3))

    def test_all_no(self):
        penaltyCalculator = PenaltyCalculator()

        customers = "NNNNN"
        self.assertEqual(0, penaltyCalculator.get_minimum_penalty_closing_hour(customers))
        self.assertEqual(3, penaltyCalculator.get_penalty(customers, 3))

if __name__ == '__main__':
    unittest.main()