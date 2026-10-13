"""Network-free checks for credential handling."""
import unittest
from config import read_credentials


class ConfigTests(unittest.TestCase):
    def test_accepts_both_keys(self):
        self.assertEqual(read_credentials({"OPENAI_KEY": " sk-test ", "TELEGRAM_KEY": " tg-test "}),
                         ("sk-test", "tg-test"))

    def test_missing_openai_key(self):
        with self.assertRaisesRegex(RuntimeError, "OPENAI_KEY"):
            read_credentials({"TELEGRAM_KEY": "tg-test"})

    def test_missing_telegram_key(self):
        with self.assertRaisesRegex(RuntimeError, "TELEGRAM_KEY"):
            read_credentials({"OPENAI_KEY": "sk-test"})

    def test_whitespace_only_key(self):
        with self.assertRaisesRegex(RuntimeError, "TELEGRAM_KEY"):
            read_credentials({"OPENAI_KEY": "sk-test", "TELEGRAM_KEY": "   "})


if __name__ == "__main__":
    unittest.main()
