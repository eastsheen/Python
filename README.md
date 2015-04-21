
Python
========
I love sports and python

目录
一、AppTest
  简单验证Android渠道包，是重复的工作，可以通过自动化来实现
    ● 用adb shell 连接设备
    ● 遍历指定路径下apk包，存放list里
    ● adb shell install依次安装apk包
    ● 安装成功启动app，进行随意monkey测试，截图保存
    ● 卸装app，循环执行list的apk

  代码文件
    ● mainApp.py  --主类管理各个用例
    ● testAppChannelPackages.py  --实现简单验证Android渠道包

二、RequestProject
  主要功能介绍：
    ● Requests  post、get方法运用
    ● Response 响应校验
    ● 常用时间封装
    ● 读写sqlite3、txt文本，便于测试数据读写—未完成
    ● 自动生成html报告—未完成
	
  代码文件
    ● requestsProjectMain.py  --实现接口post请求，验证response、写日志
    ● getCurrentTime.py --提供些时间控件获取方法
    ● testCaseTotal.py  --统计用例执行结果
    ● writelogging.py   --提供写日志方法



***about me***

auther:Eastsheen
email:yangdongxian@gmail.com or QQ:393857608

