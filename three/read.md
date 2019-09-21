## 级联操作

## three里在定义好Model，准备生成迁移文件时，执行python manage.py makemigrations出错了，后来
测试 runserver时也会报错，显示 没有pymysql模块，开始以为是库的问题，后来查出来是，运行python命令时，没有切换合适的环境

