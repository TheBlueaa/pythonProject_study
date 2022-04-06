import unittest
import time
import threading

class TestGoodsDetail(unittest.TestCase):
    def setUp(self):
        print(threading.current_thread().name + "执行用例",end=":")

        time.sleep(1)

    def test001(self):
        print("测试获取普通商品的商品详情")

    def test002(self):
        print("测试获取活动商品的商品详情")

    def test003(self):
        print("测试获取金币商品的商品详情")

    def test004(self):
        print("测试显示id为1的商品详情")

    def test005(self):
        print("测试显示id为2的商品详情")

    def test006(self):
        print("测试显示id为100的商品详情")

    def test007(self):
        print("测试商品名称长度超过规定的商品详情")

    def test008(self):
        print("测试商品名称长度小于规定的商品详情")

    def test009(self):
        print("测试商品名称为空的商品详情")

    def test010(self):
        print("测试商品名称为Null的商品详情")

    def test011(self):
        print("测试商品名称为包括字母数字特殊字符的商品详情")

    def test012(self):
        print("测试商品类型为服饰的商品详情")

    def test013(self):
        print("测试商品类型为食品的商品详情")

    def test014(self):
        print("测试商品类型为手机的商品详情")

    def test015(self):
        print("测试商品类型为奢侈品的商品详情")

    def test016(self):
        print("测试商品图片为空的商品详情")

    def test017(self):
        print("测试商品图片URL是文字的商品详情")

    def test018(self):
        print("测试商品图片URL是linux命令的商品详情")

    def test019(self):
        print("测试已下架商品的商品详情")

    def test020(self):
        print("测试已过期商品的商品详情")

    def test021(self):
        print("测试已删除商品的商品详情")

    def test022(self):
        print("测试不存在的商品的商品详情")

    def test023(self):
        print("测试商品价格是负数的商品详情")

    def test024(self):
        print("测试商品价格是0的商品详情")

    def test025(self):
        print("测试商品价格是null的商品详情")

    def test026(self):
        print("测试商品价格是空的商品详情")

    def test027(self):
        print("测试商品日期是空的商品详情")

    def test028(self):
        print("测试商品日期是null的商品详情")

    def test029(self):
        print("测试商品备注的长度超过规定的商品详情")

    def test030(self):
        print("测试商品备注的长度等于规定的商品详情")

    def test031(self):
        print("测试商品备注的长度小于规定的商品详情")

    def test032(self):
        print("测试商品规格不正确时的商品详情")

    def test033(self):
        print("测试商品规格长度超过规定的商品详情")

    def test034(self):
        print("测试商品市场价超过规定的商品详情")

    def test035(self):
        print("测试商品市场价低于规定的商品详情")

    def test036(self):
        print("测试商品体积格式不正确时的商品详情")

    def test037(self):
        print("测试商品体积大小超过规定的商品详情")

    def test038(self):
        print("测试商品类型不存在的商品详情")

    def test039(self):
        print("测试商品状态不存在的商品详情")

    def test040(self):
        print("测试商品状态已锁定的商品详情")

    def test041(self):
        print("测试商品状态已删除的商品详情")

    def test042(self):
        print("测试热门商品的商品详情")

    def test043(self):
        print("测试热门商品为空的商品详情")

    def test044(self):
        print("测试商品分类的长度超过规定的商品详情")

    def test045(self):
        print("测试商品分类的长度小于规定的商品详情")

    def test046(self):
        print("测试商品分类的为空小于规定的商品详情")

    def test047(self):
        print("测试商品分类的为null小于规定的商品详情")

    def test048(self):
        print("测试热门商品为null的商品详情")

    def test049(self):
        print("测试商品状态为空的商品详情")

    def test050(self):
        print("测试商品状态为null的商品详情")

    def test051(self):
        print("测试商品类型为空的商品详情")

    def test052(self):
        print("测试商品类型为null的商品详情")

    def test053(self):
        print("测试商品类型字段值是代码的商品详情")

    def test054(self):
        print("测试商品名称字段值是代码的商品详情")

    def test055(self):
        print("测试商品规格字段值是代码的商品详情")

    def test056(self):
        print("测试商品日期字段值是代码的商品详情")

    def test057(self):
        print("测试商品价格字段值是代码的商品详情")

    def test058(self):
        print("测试商品关键字字段值是代码的商品详情")

    def test059(self):
        print("测试商品市场价字段值是代码的商品详情")

    def test060(self):
        print("测试商品权重字段值是代码的商品详情")

    def test061(self):
        print("测试商品权重字段值空的商品详情")

    def test62(self):
        print("测试商品权重字段值是负数的商品详情")

    def test63(self):
        print("测试商品详情查询1秒完成")

    def test64(self):
        print("测试并发查询商品详情")

    def test65(self):
        print("测试商品详情日期非法2月有30天的商品详情")

    def test66(self):
        print("测试商品详情日期非法填写的不是日期的商品详情")

