import unittest
import tokenizer


class TestGenSalt(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(tokenizer.gen_salt(5)), str)

    def test_size(self):
        self.assertEqual(len(tokenizer.gen_salt(10)), 10)
        self.assertEqual(len(tokenizer.gen_salt(5)), 5)
        self.assertEqual(len(tokenizer.gen_salt(15)), 15)
        for i in range(100):
            self.assertEqual(len(tokenizer.gen_salt(i)), i)


class TestHash(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(tokenizer.get_hash('dqs', 'ih')), str)


class TestPasswordChecker(unittest.TestCase):
    def test_length(self):
        self.assertEqual(tokenizer.check_password_security('87'), '3')

    def test_set(self):
        self.assertEqual(tokenizer.check_password_security('11114444'), '4')


if __name__ == '__main__':
    unittest.main()
