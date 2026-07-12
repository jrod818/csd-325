# Jose Rodriguez
# 7/13/2026
# CSD 325 Module 7.2 Test Cases

# Description: Tests the city_country function.

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()