#This file is part of emailvalid. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Unit test for emailvalid
'''

import unittest
import emailvalid

EMAILS = (
    ('username@domain.com, anotheruser@domain.com', True),
    ('username@domain.com; anotheruser@domain.com', True),
    ('username@domain.com;anotheruser@domain.com', True),
    ('username@domain', False),
    ('another,user@domain.com', False),
    ('another;user@domain.com', False),
)


class BankNumberTest(unittest.TestCase):
    '''
    Test Case for emailvalid
    '''

    def test_emails(self):
        '''
        Test eMails
        '''
        for email, result in EMAILS:
            if result:
                test = self.assert_
            else:
                test = self.assertFalse
            test(emailvalid.check_email(email))

if __name__ == '__main__':
    unittest.main()
