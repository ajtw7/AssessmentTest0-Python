import unittest

from pkg.Hello import Hello


class HelloTest(unittest.TestCase):
    def test_hello(self) -> None:
        # Given
        expected = "Hello, World!"
        # When
        pkg = Hello()
        result = pkg.hello_world()
        # Then
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
