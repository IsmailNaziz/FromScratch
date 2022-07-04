import unittest
from main import solution, solution_bonus
from datetime import date


class TestBirthDay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_distinct_birthdays_students = {'Hamza': date(1998, 1, 9),
                                                'Mathieu': date(1996, 5, 7),
                                                'Raphael': date(2001, 8, 24),
                                                'Charles': date(1997, 10, 19)}
        cls.data_same_birthdays_students = {'Hamza': date(1998, 1, 9),
                                            'Mathieu': date(1996, 5, 7),
                                            'Raphael': date(1998, 1, 9),
                                            'Charles': date(1997, 10, 19)}
        cls.data_more_than_two_students_with_same_birthday = {'Hamza': date(1998, 1, 9),
                                                              'Mathieu': date(1998, 1, 9),
                                                              'Raphael': date(2001, 8, 24),
                                                              'Charles': date(1998, 1, 9)}

    def test_distinct_birthday_students(self):
        result = solution(self.data_distinct_birthdays_students)
        self.assertEqual(result, False)

    def test_same_birthdays_students(self):
        result = solution(self.data_same_birthdays_students)
        self.assertEqual(result, True)

    def test_more_than_two_students_with_same_birthday(self):
        result = solution(self.data_more_than_two_students_with_same_birthday)
        self.assertEqual(result, True)


class TestBirthDayBonus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_distinct_birthdays_students = {'Hamza': date(1998, 1, 9),
                                                'Mathieu': date(1996, 5, 7),
                                                'Raphael': date(2001, 8, 24),
                                                'Charles': date(1997, 10, 19)}

        cls.data_same_birthdays_students = {'Hamza': date(1998, 1, 9),
                                            'Mathieu': date(1996, 5, 7),
                                            'Raphael': date(1998, 1, 9),
                                            'Charles': date(1997, 10, 19)}

        cls.data_same_birthdays_students_two_pairs = {'Hamza': date(1998, 1, 9),
                                                      'Mathieu': date(1996, 5, 7),
                                                      'Raphael': date(1998, 1, 9),
                                                      'Charles': date(1997, 10, 19),
                                                      'Lucas': date(1996, 5, 7),
                                                      'David': date(2002, 10, 19), }
        cls.data_more_than_two_students_with_same_birthday = {'Hamza': date(1998, 1, 9),
                                                              'Mathieu': date(1998, 1, 9),
                                                              'Raphael': date(2001, 8, 24),
                                                              'Charles': date(1998, 1, 9)}

    def test_distinct_birthday_students(self):
        result = solution_bonus(self.data_distinct_birthdays_students)
        self.assertEqual(result, [])

    def test_same_birthdays_students(self):
        result = solution_bonus(self.data_same_birthdays_students)
        self.assertEqual(result, [('Hamza', 'Raphael')])

    def test_same_birthdays_students_two_pairs(self):
        result = solution_bonus(self.data_same_birthdays_students)
        self.assertEqual(result, [('Hamza', 'Raphael'), ('Mathieu', 'Lucas')])

    def test_more_than_two_students_with_same_birthday(self):
        result = solution_bonus(self.data_more_than_two_students_with_same_birthday)
        self.assertEqual(result, [('Hamza', 'Raphael', 'Mathieu')])
