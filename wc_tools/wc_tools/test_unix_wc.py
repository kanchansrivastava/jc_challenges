import unittest
import tempfile, os

from unix_wc import UnixWC


class TestUnixWC(unittest.TestCase):
    def setUp(self):
        self.filename = "sample.txt"
        self.unix_wc = UnixWC(filepath=self.filename)
        return super().setUp()

    def test_count_number_of_bytes(self):
        self.assertEqual(self.unix_wc.count_bytes(), 342190)

    def test_count_words(self):
        self.assertEqual(self.unix_wc.count_words(), 58164)

    def test_count_lines(self):
        self.assertEqual(self.unix_wc.count_lines(), 7145)

    def test_count_number_of_characters(self):
        self.assertEqual(self.unix_wc.count_characters(), 332147)

    def test_default_output_format(self):
        output = str(self.unix_wc)
        parts = output.split()
        self.assertEqual(len(parts), 4)
        self.assertEqual(int(parts[0]), self.unix_wc.count_lines())  # lines
        self.assertEqual(int(parts[1]), self.unix_wc.count_words())  # words
        self.assertEqual(int(parts[2]), self.unix_wc.count_characters())  # characters
        self.assertTrue(parts[3].endswith(os.path.basename(self.filename)))

    def test_empty_file(self):
        empty = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
        empty.close()
        wc_empty = UnixWC(empty.name)
        self.assertEqual(wc_empty.count_lines(), 0)
        self.assertEqual(wc_empty.count_words(), 0)
        self.assertEqual(wc_empty.count_characters(), 0)
        self.assertEqual(wc_empty.count_bytes(), 0)
        os.remove(empty.name)


if __name__ == "__main__":
    unittest.main()
