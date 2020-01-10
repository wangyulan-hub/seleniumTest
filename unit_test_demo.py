import unittest
import HTMLTestRunner
import time


class UserTestCase(unittest.TestCase):

    def setUp(self):
        print("==setUp==")
        self.name = "王玉兰"
        self.age = 25

    def tearDown(self):
        print("==tearDown==")
        # self.assertEqual('foo'.isupper(),'FOO')

    def test_one(self):
        print("==test_one==")
        self.assertEqual(self.name,"王玉兰",msg="名字不对")

    def test_two(self):
        print("==test_two==")
        self.assertFalse("wangyulan".isupper(),msg="是大写")

    def test_three(self):
        print("==test_three==")
        self.assertEqual(self.age,25)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_three"))
    suite.addTest(UserTestCase("test_one"))
    suite.addTest(UserTestCase("test_two"))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    file_prefix = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print(file_prefix)
    fp = open("./" + file_prefix + "_result.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="xdclass",description="用例执行情况")
    runner.run(suite)
    fp.close()


