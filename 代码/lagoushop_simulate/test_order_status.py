import time
import unittest
import threading


class TestOrderStatus(unittest.TestCase):
    def setUp(self):
        print(threading.current_thread().name + "执行用例",end=":")
        time.sleep(1)


    def test001(self):
        print("测试联查看订单状态成功")

    def test002(self):
        print("测试移动订单状态成功")

    def test003(self):
        print("测试电信订单状态成功")

    def test004(self):
        print("测试长度超过11位订单状态失败")

    def test005(self):
        print("测试长度超过11位订单状态失败")

    def test006(self):
        print("测试长度小于11位订单状态失败")

    def test007(self):
        print("测试没有注册的订单状态失败")

    def test008(self):
        print("测试中有数字、字母特殊字符订单状态失败")

    def test009(self):
        print("测试在中输入超工长度的字符订单状态失败")

    def test010(self):
        print("测试已注册邮箱订单状态成功")

    def test011(self):
        print("测试未注册邮箱订单状态失败")

    def test012(self):
        print("测试邮箱格式不正确订单状态失败")

    def test013(self):
        print("测试邮箱长度超过规定长度订单状态失败")

    def test014(self):
        print("测试邮箱长度低于规定长度订单状态失败")

    def test015(self):
        print("测试邮箱中输入Null订单状态失败")

    def test016(self):
        print("测试中输入Null订单状态失败")

    def test017(self):
        print("测试未获取验证码，订单状态失败")

    def test018(self):
        print("测试验证码填写错误，订单状态失败")

    def test019(self):
        print("测试验证码位数超过指定位数，订单状态失败")

    def test020(self):
        print("测试验证码位数低于指定位数，订单状态失败")

    def test021(self):
        print("测试验证码错误五次以上，订单状态失败")

    def test022(self):
        print("测试验证码已失效，订单状态失败")

    def test023(self):
        print("测试已订单状态成功的验证码，再次重复使用订单状态失败")

    def test024(self):
        print("测试不输入，订单状态失败")

    def test025(self):
        print("测试不输入邮箱，订单状态失败")

    def test026(self):
        print("测试不输入验证码，订单状态失败")

    def test027(self):
        print("测试输入的验证码有特殊字符，订单状态失败")

    def test028(self):
        print("测试输入的密码错误，订单状态失败")

    def test029(self):
        print("测试输入的密码长度超过规定，订单状态失败")

    def test030(self):
        print("测试输入的密码长度小于规定，订单状态失败")

    def test031(self):
        print("测试密码错误次数超过5次，订单状态失败")

    def test032(self):
        print("测试密码字符中包括了需求规定以外的符号如括号，订单状态失败")

    def test033(self):
        print("测试输入超工长度的密码，订单状态失败")

    def test034(self):
        print("测试输入超工长度的验证码，订单状态失败")

    def test035(self):
        print("测试的SQL注入代码")

    def test036(self):
        print("测试密码的SQL注入代码")

    def test037(self):
        print("测试验证码的SQL注入代码")

    def test038(self):
        print("测试的XSS注入代码")

    def test039(self):
        print("测试密码的XSS注入代码")

    def test040(self):
        print("测试验证码的XSS注入代码")

    def test041(self):
        print("测试被冻结账号的订单状态失败")

    def test042(self):
        print("测试未激活账号的订单状态失败")

    def test043(self):
        print("测试验证码输入Null订单状态失败")

    def test044(self):
        print("测试密码输入Null订单状态失败")

    def test045(self):
        print("测试用户13888888888订单状态成功后，138..888用户订单状态次数统计数+1")

    def test046(self):
        print("测试相同用户，不同IP的订单状态，统计订单状态次数是否正确")

    def test047(self):
        print("测试相同用户，相同IP的订单状态，统计订单状态次数是否正确")

    def test048(self):
        print("测试不同用户，不同IP的订单状态，统计订单状态次数是否正确")

    def test049(self):
        print("测试IP被锁定的用户订单状态失败")

    def test050(self):
        print("测试首次订单状态密码错误，第二次订单状态触发极验成功")

    def test051(self):
        print("测试异地订单状态失败")

    def test052(self):
        print("测试添加异地记录后，订单状态成功")

    def test053(self):
        print("测试开启设备锁后，在不同设备订单状态失败")

    def test054(self):
        print("测试开启设备锁后，在不同设备订单状态失败")

    def test055(self):
        print("测试开启设备锁后，添加设备后订单状态成功")

    def test056(self):
        print("测试开启设备锁后关闭设备锁，不同设备订单状态成功")

    def test057(self):
        print("测试开启异地订单状态后，关闭异地订单状态验证，异地订单状态成功")

    def test058(self):
        print("测试开启异地订单状态后，关闭异地订单状态验证，异地订单状态成功")

    def test059(self):
        print("测试数据埋点，订单状态后，成功采集到用户信息")

    def test060(self):
        print("测试用户3秒内订单状态成功")

    def test061(self):
        print("测试同样的用户3并发订单状态时，只有一个用户订单状态成功，其他用户订单状态失败")

    def test62(self):
        print("测试同样的用户，1秒内订单状态十次成功，没有其他异常")

    def test63(self):
        print("测试第三方微信授权订单状态成功")

    def test64(self):
        print("测试第三方QQ授权订单状态成功")

    def test65(self):
        print("测试第三方支付宝订单状态成功")

    def test66(self):
        print("测试本机手机免密订单状态成功")
