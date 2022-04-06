import time
import unittest
import threading

class TestGoodsList(unittest.TestCase):
    def setUp(self):
        print(threading.current_thread().name + "执行用例",end=":")
        time.sleep(1)

    def test001(self):
        print("测试商品列表的排序规则")

    def test002(self):
        print("测试商品列表没有商品")

    def test003(self):
        print("测试商品列表有1个商品")

    def test004(self):
        print("测试商品列表有10个商品")

    def test005(self):
        print("测试商品列表第2页没有商品")

    def test006(self):
        print("测试商品列表第2页有1个商品")

    def test007(self):
        print("测试商品列表第2页有10个商品")

    def test008(self):
        print("测试商品列表第分页规则")

    def test009(self):
        print("测试商品列表查询速度3秒完成")

    def test010(self):
        print("测试10并发查询商品列表")

    def test011(self):
        print("测试商品数目不足以分页时的商品列表")

    def test012(self):
        print("测试商品数目刚好可以分2页时的商品列表")

    def test013(self):
        print("测试商品列表中，商品名称的长度超过规定")

    def test014(self):
        print("测试商品列表中，商品名称的长度小于规定")

    def test015(self):
        print("测试商品列表中，有商品名称为空")

    def test016(self):
        print("测试商品列表中，有商品名称为null")

    def test017(self):
        print("测试商品列表中，有商品价格为空")

    def test018(self):
        print("测试商品列表中，有商品价格为null")

    def test019(self):
        print("测试商品列表中，有商品价格为负数")

    def test020(self):
        print("测试商品列表中，有商品价格有特殊字符")

    def test021(self):
        print("测试商品列表中，有商品名称有特殊字符")

    def test022(self):
        print("测试商品列表中，冻结的商品显示")

    def test023(self):
        print("测试商品列表中，下架的商品显示")

    def test024(self):
        print("测试商品列表中，过期的商品显示")

    def test025(self):
        print("测试商品列表中，按照时间排列")

    def test026(self):
        print("测试商品列表中，按照权重排列")

    def test027(self):
        print("测试商品列表中，按照商品名称排序")

    def test028(self):
        print("测试商品列表中，按照价格排序")

    def test029(self):
        print("测试商品列表中，按照id排序")

    def test030(self):
        print("测试商品列表中，按照分类排序")

    def test031(self):
        print("测试商品列表中，图片为空的商品展示")

    def test032(self):
        print("测试商品列表中，图片为null")

    def test033(self):
        print("测试商品列表中，图片写的是特殊字符")

    def test034(self):
        print("测试商品列表中，图片写的是SQL注入代码")

    def test035(self):
        print("测试商品列表中，图片写的是XSS注入代码")

    def test036(self):
        print("测试商品列表中，图片URL长度超过设定")

    def test037(self):
        print("测试商品列表中，图片URL格式与需求规定不符")

    def test038(self):
        print("测试商品列表中，图片太大")

    def test039(self):
        print("测试商品列表中，图片分辨率不符合需求规定")

    def test040(self):
        print("测试商品列表中，图片使用的是在线图片")

    def test041(self):
        print("测试未登录查询商品列表")

    def test042(self):
        print("测试商品列表的热门商品")

    def test043(self):
        print("测试商品列表的活动商品")

    def test044(self):
        print("测试商品列表的金币商品")

    def test045(self):
        print("测试商品列表的优惠商品")

    def test046(self):
        print("测试商品列表的团购商品")

    def test047(self):
        print("测试商品列表的秒杀商品")

    def test048(self):
        print("测试商品列表的限时抢购商品")

    def test049(self):
        print("测试商品列表显示10000个商品")

    def test050(self):
        print("商品列表显示新加的商品")

    def test051(self):
        print("商品列表其他元素1的为空")

    def test052(self):
        print("商品列表其他元素1的为null")

    def test053(self):
        print("商品列表其他元素1的为长度超过规定")

    def test054(self):
        print("商品列表其他元素1的为长度小于规定")

    def test055(self):
        print("商品列表其他元素1的有字母数字特殊字符")

    def test056(self):
        print("商品列表其他元素1的SQL注入")

    def test057(self):
        print("商品列表其他元素1的XSS注入")

    def test058(self):
        print("商品列表其他元素1的敏感信息")

    def test059(self):
        print("商品列表其他元素1的值重复")

    def test060(self):
        print("商品列表其他元素1的规定值1，如状态")

    def test061(self):
        print("商品列表其他元素1的规定值2，如状态")

    def test62(self):
        print("商品列表其他元素1的规定值以外的值，如状态")

    def test63(self):
        print("商品列表其他元素1的布尔类型为true")

    def test64(self):
        print("商品列表其他元素1的布尔类型为false")

    def test65(self):
        print("商品列表其他元素1的日期为非法日期")

    def test66(self):
        print("商品列表其他元素1的数字为非法数字")

