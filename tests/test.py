import zstd
import sys


import unittest
import os

class TestZSTD(unittest.TestCase):

    def test_random(self):
      DATA = os.urandom(128 * 1024)  # Read 128kb
      self.assertEqual(DATA, zstd.loads(zstd.dumps(DATA)))

    def test_raw(self):
      DATA = b"abc def"
      self.assertEqual(DATA, zstd.decompress(zstd.compress(DATA)))

if __name__ == '__main__':
    unittest.main()

