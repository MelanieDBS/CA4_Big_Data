# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:21:08 2018

@author: melan
"""

from Perform_Analysis import get_commits, read_file


#Testing the code
import unittest

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('C:\\Users\\melan\\OneDrive\\Documents\\CA4_10390914\\changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual('Jimmy', commits[420].author)
        
        

if __name__ == '__main__':
    unittest.main()