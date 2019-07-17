"""
------------------------------------
@Time : 2019/7/17 23:02
@Auth : linux超
@File : InvestDatas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class InvestData(object):

    invest_amount_singular = [
        {
            'amount': '1',
            'expect': '请输入10的整数倍'
        },
        {
            'amount': '10.1',
            'expect': '投标金额必须为100的倍数'
        }
    ]

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
            'amount': '100',
            'expect': '购买标的金额不能大于标总金额'
        }
    ]
