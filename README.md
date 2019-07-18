# PythonUiAutoTest

项目目录

    1.cases: 测试用例存放目录
    2.Cases->unit_test->unit_test.py: 所有用例均继承此文件中的自定义unittest
    3.common: 项目公共方法
    4.Config->config.py：存放项目所有目录的路径信息
    5.Datas：存放了测试用例所需的测试数据，两种形式：1.py文件保存2.excel文件保存
    6.libs：存放对源码或者第三方模块修改后的模块
    7.pages: 根据page object 设计模式，本目录存放被测项目每个页面的元素操作及业务流程
    8.Pages->base ->base.py: 对selenium webdriver api部分功能的二次封装(所有页面的通用方法)
    9.Pages->locator.ini: ui对象库，存放所有页面的操作元素定位表达式
    10.log：自动生成目录及生成项目执行日志
    11.report：自动生成目录及生成项目测试HTML报告(报告包含用例统计饼图及失败用例的截图)
ui对象库

    Locator.ini
    使用配置文件作为UI对象库，存放被测项目中的元素定位方式及定位表达式，方便项目维护，做到定位与代码分离，
    元素变动时只需修改对应定位方式及表达式即可，不用修改代码逻辑
测试数据

    *Datas.py
    Test_cases.xlsx
    项目使用两种存放与读取测试数据的方式
    1.使用excel表存放数据，对不同测试内容设计不同的数据表，每条用例关联对应测试数据，读取较麻烦，但做到了代码与数据的分离，更能体现数据驱动的思想
    2.使用普通py文件管理数据，读取方便，个人认为UI测试使用这种方式更加简单
    3.本项目中登录用例采用的excel存储数据，投资用例采用的py文件存放数据
项目设计

    1.使用selenium 3自动化测试工具对测试页面的操作
    2.结合python unittest单元测试框架编辑及组织测试用例
    3.通过ddt数据驱动测试框架，实现同一个测试用例执行不同的测试数据，提高测试覆盖率，测试准确性，及减少部分测试代码
    4.项目整个结构使用Page Object设计模式，把元素和方法按照页面抽象出来，分离成一定的对象，为每个页面的属性和操作构建模型，增加代码复用性，增强代码结构，当对数据或者元素修改时不会影响业务的流程及用例的执行
    5.测试执行过程中自动生成测试日志及HTML测试报告
测试环境

    1.Windows 10 
    2.Python 3.6
    3.Selenium3 
    4.Openpyxl
    5.Firefox或Chrome浏览器
项目执行

    1.Cd PythonUiAutoTest
    2.Python run_test.py
测试结果
    报告展示
用例进度

    1.登录功能测试用例已经完成
    2.投资功能用例只完成了异常情况用例
TODO

    1.优化代码
    2.完成剩余用例设计
博客地址

    https://www.cnblogs.com/linuxchao/