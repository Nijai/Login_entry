from pid_entry import show_time_of_pid
import unittest
class TestFirst_code(unittest.TestCase):
	def test_basic(self):
		testcase = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
		expected = "Jul 6 14:01:23 pid:29440"
		self.assertEqual(show_time_of_pid(testcase),expected)
	def test_empty(self):
		testcase = " "
		expected = " "
		self.assertEqual(show_time_of_pid(testcase),expected)
	def test_other_month(self):
		testcase = "Sept 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
		expected = "Sept 6 14:01:23 pid:29440"
		self.assertEqual(show_time_of_pid(testcase),expected)
	
	def test_other(self):
		testcase = "Sept 10 14:01:23 computer.name CRON[29440]: USER (good_user)"
		expected = "Sept 10 14:01:23 pid:29440"
		self.assertEqual(show_time_of_pid(testcase),expected)
unittest.main()