import allure


class Test_002:

    def test_add_png(self):
        """添加一张abc.png截图到测试报告"""

        with open("G:\\tools\\heima就业班\\APP练习\\app_day08\\scripts\\abc.png", "rb") as f:
            # 添加图片内容到测试报告，以附件的方式
            allure.attach("截图", f.read(), allure.attach_type.PNG)
