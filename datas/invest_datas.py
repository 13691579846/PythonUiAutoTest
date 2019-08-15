"""
------------------------------------
@Time : 2019/7/17 23:02
@Auth : linux超
@File : invest_datas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class InvestData(object):
    """投资功能测试数据"""

    # 正确的用户名和密码
    user_password = {
            'phone': '****',
            'pwd': '****'
        }

    # 测试金额非100倍数
    invest_amount_singular = [
        {
            'amount': '1',
            'expect': '请输入10的整数倍'
        },
        {
            'amount': '10.1',
            'expect': '请输入10的整数倍'
        },
        {
            'amount': '-1',
            'expect': '请输入10的整数倍'
        },
        {
            'amount': '101',
            'expect': '请输入10的整数倍'
        },
    ]

    # 测试金额为0，小于100整数，及大于标的剩余金额
    invest_amount_error = [
        {
            'amount': '0',
            'expect': '请正确填写投标金额'
        },
        {
            'amount': '10',
            'expect': '投标金额必须为100的倍数'
        },
        {
            'amount': ' ',
            'expect': '请正确填写投标金额'
        }
    ]

    invest_success = [
        {
            'amount': 100,
            'expect': '投标成功！'
        }
    ]
