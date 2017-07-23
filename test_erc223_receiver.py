
import unittest
from ethereum import utils, opcodes
from ethereum.tools import tester
from viper import parser


def assert_tx_failed(erc20_tester, function_to_test):
    """ Ensure that transaction fails, reverting state (to prevent gas exhaustion) """
    initial_state = erc20_tester.s.snapshot()
    erc20_tester.assertRaises(tester.TransactionFailed, function_to_test)
    erc20_tester.s.revert(initial_state)

class TestERC223_RECEIVER(unittest.TestCase):
    def setUp(self):
        # Initialize tester, contract and expose relevant objects
        self.t = tester
        self.s = self.t.Chain()
        from viper import compiler
        self.t.languages['viper'] = compiler.Compiler()
        # c1 is token contract, c2 is the receiver contract
        self.c1 = self.s.contract(open('erc223.v.py').read(),args =['GasHoleToken','GHT'] ,language = 'viper')
        self.c2 = self.s.contract(open('erc223_receiver.v.py').read(), language = 'viper')


    def test_tokenFallback(self):
        print("Testing tokenFallback Function")
        self.assertEqual(self.c1.balanceOf(self.c2.address),0)
        self.assertTrue(self.c1.deposit(value=5, sender=self.t.k1))
        self.assertEqual(self.c1.balanceOf(self.t.a1),5)
        print("here")
        print(self.c2.translator.function_data)
        # print(parser.mk_full_signature(self.c2))
        # print(parser.get_function_signature(self.c2.tokenFallback))
        # Sending from c1, from a1 address to contract c2, with random data

        # self.c2.tokenFallback(self.t.a1, 2, self.c2.address ,sender = self.c1.address)


if __name__ == '__main__':
    unittest.main()
