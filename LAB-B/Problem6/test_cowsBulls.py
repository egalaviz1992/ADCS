import unittest
from cowsBulls import *

class UnitCowsBulls(unittest.TestCase):
    def test_any_repeated_digit1(self):
         self.assertEqual(any_repeated_digit("1123"),True)
    def test_any_repeated_digit2(self):
         self.assertEqual(any_repeated_digit("1234"),False)
    def test_any_repeated_digit3(self):
         self.assertEqual(any_repeated_digit("4444"),True)

    
    def test_verify_num1(self):
        self.assertEqual(verify_num("1234"),True)
    def test_verify_num2(self):
        self.assertEqual(verify_num(""),False)
    def test_verify_num3(self):
        self.assertEqual(verify_num("12345"),False)
    def test_verify_num4(self):
        self.assertEqual(verify_num("1111"),False)   

    def test_count_cows_bulls1(self):   
        self.assertEqual(count_cows_bulls("1234","1234"),(4,0))
    def test_count_cows_bulls2(self):   
        self.assertEqual(count_cows_bulls("4321","1234"),(0,4))
    def test_count_cows_bulls3(self):   
        self.assertEqual(count_cows_bulls("1234","5678"),(0,0))
    def test_count_cows_bulls4(self):   
        self.assertEqual(count_cows_bulls("1256","1265"),(2,2))
    def test_count_cows_bulls5(self):   
        self.assertEqual(count_cows_bulls("1234","1111"),None)
    def test_count_cows_bulls6(self):   
        self.assertEqual(count_cows_bulls("",""),None)
                     
    def test_gen_num_with_verify_num100times(self):
        for i in range(1,100):
            self.assertEqual(verify_num(gen_num()),True)
            
    def test_gen_num__size100times(self):
        for i in range(1,100):
        
            self.assertEqual(len(gen_num()),4)
    def test_gen_num__nonRepeated100times(self):
        for i in range(1,100):
            self.assertEqual(any_repeated_digit(gen_num()),False)
            
    def test_play1(self):        
        self.assertEqual(play(["1234","2341","5432"],"1231"),-1)    
    def test_play2(self):        
        self.assertEqual(play([""],"1231"),-1)
    def test_play3(self):        
        self.assertEqual(play(["1234","2341","5432"],"123"),-1)    
    def test_play4(self):        
        self.assertEqual(play(["1234","2341","5432"],"5432"),3)
    def test_play5(self):        
        self.assertEqual(play(["1234","2341","543","1","8765","1235"],"1235"),4)


if __name__ == '__main__':
    unittest.main
    