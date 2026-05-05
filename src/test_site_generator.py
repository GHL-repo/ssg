import unittest

from site_generator import extract_title


class TestSiteGenerator(unittest.TestCase):
    def test_extract_title(self):
        title1 = extract_title("# I am the Walrus")
        title2 = extract_title("# I am the Black Wizards")

        self.assertEqual(title1, "I am the Walrus")
        self.assertNotEqual(title2, "# I am the Black Wizards")
        with self.assertRaises(Exception):
            extract_title("#I am therefore")
