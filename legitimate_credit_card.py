import unittest

'''
Give you a string and you have to find the legitimate card number
    a) Each card number must be 13-16 digits and you need to output with only last 4 digits visible
'''

class CreditCardValidator(object):
    
    
    def get_masked_credit_card_number(self, credit_card_number):
        if not self._is_valid_credit_card_number(credit_card_number=credit_card_number):
            return "invalid"

        return self._get_masked_credit_card_format(credit_card_number=credit_card_number)
    
    def get_masked_credit_card_numbers(self, credit_card_number_list):
        valid_credit_cards_masked = [self._get_masked_credit_card_format(credit_card_number) \
                                     for credit_card_number in credit_card_number_list \
                                        if self._is_valid_credit_card_number(credit_card_number)]
        
        return valid_credit_cards_masked
    
    def _get_masked_credit_card_format(self, credit_card_number):
        return "************" + credit_card_number[12:]
    
    def _is_valid_credit_card_number(self, credit_card_number):
        if not credit_card_number or len(credit_card_number) != 16:
            return False
        
        last_4_chars = credit_card_number[12:]
        if not self._is_all_digits(last_4_chars):
            return False
        
        return True

    def _is_all_digits(self, chars):
        for c in chars:
            if ord(c) > ord('9') or ord(c) < ord('0'):
                return False
            
        return True
    
class CreditCardValidatorTest(unittest.TestCase):

    def test_get_masked_credit_card_number_valid(self):
        creditCardValidator = CreditCardValidator()

        credit_card = "qwerhnjuiols1234"
        self.assertEqual("************1234", creditCardValidator.get_masked_credit_card_number(credit_card_number=credit_card))

    def test_get_masked_credit_card_number_invalid(self):
        creditCardValidator = CreditCardValidator()

        credit_card = "njuiol1234"
        self.assertEqual("invalid", creditCardValidator.get_masked_credit_card_number(credit_card_number=credit_card))

        credit_card = "njuiolfhkjghkhgkjjf1234"
        self.assertEqual("invalid", creditCardValidator.get_masked_credit_card_number(credit_card_number=credit_card))

        credit_card = ""
        self.assertEqual("invalid", creditCardValidator.get_masked_credit_card_number(credit_card_number=credit_card))

        credit_card = "qwerhnjuiols1w34"
        self.assertEqual("invalid", creditCardValidator.get_masked_credit_card_number(credit_card_number=credit_card))
        
    def get_masked_credit_card_numbers(self):
        creditCardValidator = CreditCardValidator()

        credit_cards = ["njuiol1234", "qwerhnjuiols1234", "qwerhnjuiols3467", "njuiolfhkjghkhgkjjf1234", "qwerhnjuiols1w34"]
        
        valid_credit_cards = creditCardValidator.get_masked_credit_card_numbers(credit_card_number_list=credit_cards)
        self.assertEqual(2, valid_credit_cards)
        self.assertEqual("************1234", valid_credit_cards[0])
        self.assertEqual("************3467", valid_credit_cards[1])

if __name__ == "__main__":
    unittest.main()
