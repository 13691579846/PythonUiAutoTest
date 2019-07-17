"""
------------------------------------
@Time : 2019/7/16 9:56
@Auth : linux超
@File : LoginDatas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class LoginData(object):

    login_success_data = [
        {
            'user': '18684720553',
            'pwd': 'python',
            'expect': '我的帐户[python10]'
        }
    ]

    login_format_data = [
        {
            'user': '',
            'pwd': 'python',
            'expect': '请输入手机号'
        },
        {
            'user': '18684720553',
            'pwd': '',
            'expect': '请输入密码'
        },
        {
            'user': '',
            'pwd': '',
            'expect': '请输入手机号'
        },
        {
            'user': '12345678901',
            'pwd': 'python',
            'expect': '请输入正确的手机号'
        }
    ]

    login_account_error_data = [
        {
            'user': '18684720551',
            'pwd': 'python',
            'expect': '帐号或密码错误!'
        },
        {
            'user': '18684720553',
            'pwd': 'pwd_error',
            'expect': '帐号或密码错误!'
        },
        {
            'user': '13691579846',
            'pwd': '123456',
            'expect': '用户不存在!'
        }
    ]


if __name__ == '__main__':
    login = LoginData()
    print(login.login_account_error_data)
