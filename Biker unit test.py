import unittest
from unittest.mock import patch
import tkinter as tk

from Data import validate_zipcode, button_clicked, create_placeholder


class TestValidateZipcode(unittest.TestCase):

    def test_valid_zipcodes(self):
        valid_zipcodes = [
            "1234",
            "1234AB",
            "1234A",
            "0000AA",
            "",
            "123",
        ]

        for code in valid_zipcodes:
            with self.subTest(code=code):
                self.assertTrue(validate_zipcode(code))

    def test_invalid_zipcodes(self):
        invalid_zipcodes = [
            "12345",       # too long
            "12A4",        # letter in digit part
            "123AB",       # missing digit
            "1234ABC",     # too many letters
            "!234",        # invalid char
            "12 34",       # space not allowed
        ]

        for code in invalid_zipcodes:
            with self.subTest(code=code):
                self.assertFalse(validate_zipcode(code))


class TestButtonClicked(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Prevent GUI window
        self.entries = []

    def make_entry(self, value):
        entry = tk.Entry(self.root)
        entry.insert(0, value)
        self.entries.append(entry)
        return entry

    @patch("Data.messagebox.showerror")
    @patch("Data.messagebox.showinfo")
    def test_missing_fields(self, mock_info, mock_error):
        # Second field empty → should trigger error
        txt_first = self.make_entry("John")
        txt_last = self.make_entry("")      # empty on purpose
        txt_addr = self.make_entry("Street 1")
        txt_zip = self.make_entry("1234AB")
        txt_email = self.make_entry("mail@mail.com")
        txt_phone = self.make_entry("0612345678")
        bike_type = self.make_entry("Heren fiets")

        button_clicked(txt_first, txt_last, txt_addr,
                       txt_zip, txt_email, txt_phone, bike_type)

        mock_error.assert_called_once()
        mock_info.assert_not_called()

    @patch("Data.messagebox.showerror")
    @patch("Data.messagebox.showinfo")
    def test_all_fields_filled(self, mock_info, mock_error):
        txt_first = self.make_entry("John")
        txt_last = self.make_entry("Doe")
        txt_addr = self.make_entry("Street 1")
        txt_zip = self.make_entry("1234AB")
        txt_email = self.make_entry("mail@mail.com")
        txt_phone = self.make_entry("0612345678")
        bike_type = self.make_entry("Heren fiets")

        button_clicked(txt_first, txt_last, txt_addr,
                       txt_zip, txt_email, txt_phone, bike_type)

        mock_info.assert_called_once()
        mock_error.assert_not_called()


class TestCreatePlaceholder(unittest.TestCase):

    def test_create_placeholder_canvas(self):
        root = tk.Tk()
        root.withdraw()

        canvas = create_placeholder(root, "Testfiets")

        self.assertIsInstance(canvas, tk.Canvas)
        self.assertEqual(canvas["width"], "120")
        self.assertEqual(canvas["height"], "90")
        self.assertEqual(canvas["bg"], "grey")


if __name__ == "__main__":
    unittest.main()
