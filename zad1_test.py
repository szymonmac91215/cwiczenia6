import zad1
import unittest


class test_z1(unittest.TestCase):
    def test_sum(self):
        op = zad1.Operacje()
        self.assertEqual(op.suma(1, 2, 3), 6)
        self.assertEqual(op.suma(1, 2), 7)
        self.assertEqual(op.suma(1), 10)

        with self.assertRaises(TypeError) as c:
            op.suma()

        op['suma'] = [1, 2]

        self.assertEqual(op.suma(0), 3)

    def test_roznica(self):
        op = zad1.Operacje()
        self.assertEqual(op.roznica(2, 1), 1)
        self.assertEqual(op.roznica(2), -2)
        self.assertEqual(op.roznica(), -1)

        op['roznica'] = [1, 2, 3]

        self.assertEqual(op.roznica(), -1)


if __name__ == '__main__':
    unittest.main()
