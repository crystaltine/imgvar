from unittest import TestCase

class LoadTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_computer_not_broken_or_something(self):
        two = 1 + 1
        self.assertEquals(2, two)