import unittest
from unittest.mock import patch
import tkinter as tk
from Data import validate_zipcode, button_clicked, create_placeholder


class TestData(unittest.TestCase):

    # 1️⃣ Test valid ZIP codes
    def test_validate_zipcode_valid(self):
        valid_codes = ["1234AB"]
        for code in valid_codes:
            with self.subTest(code=code):
                self.assertTrue(validate_zipcode(code))

    # 2️⃣ Test invalid ZIP codes
    def test_validate_zipcode_invalid(self):
        invalid_codes = ["12345", "12A4", "123AB", "1234ABC", "!234", "12 34"]
        for code in invalid_codes:
            with self.subTest(code=code):
                self.assertFalse(validate_zipcode(code))

    # Helper for Entry widgets
    def make_entry(self, root, value):
        entry = tk.Entry(root)
        entry.insert(0, value)
        return entry

    # 3️⃣ Test button_clicked → missing fields → showerror
    @patch("Data.messagebox.showerror")
    @patch("Data.messagebox.showinfo")
    def test_button_clicked_missing_fields(self, mock_info, mock_error):
        root = tk.Tk()
        root.withdraw()

        fields = [
            self.make_entry(root, "John"),
            self.make_entry(root, ""),   # EMPTY FIELD
            self.make_entry(root, "Street 1"),
            self.make_entry(root, "1234AB"),
            self.make_entry(root, "test@mail.com"),
            self.make_entry(root, "0612345678"),
            self.make_entry(root, "Heren fiets")
        ]

        button_clicked(*fields)

        mock_error.assert_called_once()
        mock_info.assert_not_called()

    # 4️⃣ Test button_clicked → all fields filled → showinfo
    @patch("Data.messagebox.showerror")
    @patch("Data.messagebox.showinfo")
    def test_button_clicked_all_filled(self, mock_info, mock_error):
        root = tk.Tk()
        root.withdraw()

        fields = [
            self.make_entry(root, "John"),
            self.make_entry(root, "Doe"),
            self.make_entry(root, "Street 1"),
            self.make_entry(root, "1234AB"),
            self.make_entry(root, "test@mail.com"),
            self.make_entry(root, "0612345678"),
            self.make_entry(root, "Heren fiets")
        ]

        button_clicked(*fields)

        mock_info.assert_called_once()
        mock_error.assert_not_called()

    # 5️⃣ Test create_placeholder returns valid canvas
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
