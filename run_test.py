"""
------------------------------------
@Time : 2019/7/11 10:21
@Auth : linux超
@File : run_test.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest

from common.record_log import logger
from common.create_dirs import CreateDir
from config.config import REPORT_DIR, LOG_DIR, ENVIRONMENT
from libs.HTMLTestRunner_cn import HTMLTestRunner


def cases_suite():
    """测试套件"""
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover('.', 'test_*.py')
    suite.addTest(discover)
    return suite


def main():
    CreateDir.create_dir(LOG_DIR)
    report_dir = CreateDir.create_dir(REPORT_DIR)
    report_filename = CreateDir.generate_filename('html')
    report_path = report_dir + '/' + report_filename
    try:
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    description=ENVIRONMENT,
                                    title='Ui自动化测试报告',
                                    tester='linux超',
                                    verbosity=2)
            runner.run(cases_suite())
    except Exception as e:
        logger.error("执行测试套件错误{}".format(e))
    else:
        logger.info("所用用例执行完成, 并生成测试报告:{}".format(report_path))


if __name__ == '__main__':
    main()
