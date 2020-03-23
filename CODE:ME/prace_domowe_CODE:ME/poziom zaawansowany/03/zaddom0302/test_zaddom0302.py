import unittest
import hashlib
from zaddom0302 import unique_ip_addresses


class Etap1(unittest.TestCase):
    def setUp(self):
        self.expected = ['66.249.73.135', '86.1.76.62', '81.220.24.207', '46.105.14.53', '207.241.237.228',
                         '207.241.237.227', '50.16.19.13', '50.150.204.184', '74.125.40.20', '121.107.188.202',
                         '91.177.205.119', '93.114.45.13', '200.49.190.101', '200.49.190.100', '198.46.149.143',
                         '24.236.252.67', '207.241.237.225', '123.125.71.35', '209.85.238.199', '207.241.237.220',
                         '207.241.237.101', '108.174.55.234', '83.149.9.216', '87.169.99.232', '218.30.103.62',
                         '66.249.73.185', '67.214.178.190', '71.212.224.97', '110.136.166.128', '1.2.3.4']
        self.result = unique_ip_addresses()

    def test_was_apache_log_modified(self):
        file = open('apache_logs', mode='r')
        content = file.read()
        computed_hash = hashlib.md5(content.encode()).digest()
        original_hash = b'E\x074y\x1a\xfd\xe8\x9d\xb4>\xb4\x1f\x97C\x89/'
        self.assertEqual(original_hash, computed_hash)
        file.close()

    def test_returned_type(self):
        self.assertTrue(isinstance(self.result, list))
        if len(self.result):
            self.assertTrue(isinstance(self.result[0], str))

    def test_result_is_correct(self):
        self.assertEqual(set(self.expected), set(self.result))

    def test_duplicates_are_removed(self):
        self.assertEqual(len(self.expected), len(self.result))


if __name__ == '__main__':
    unittest.main()
