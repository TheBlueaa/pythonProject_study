import time
import unittest
import threading


class TestCarts(unittest.TestCase):
    def setUp(self):
        time.sleep(1)

    def test001(self):
        print(threading.current_thread().name + "执行用例",end=":")
        print("测试添加1个商品1个数量到购物车，添加成功")

    def test002(self):
        print(threading.current_thread().name + "执行用例",end=":")
        print("测试添加2个商品1个数量到购物车，添加成功")

    def test003(self):
        
        print("测试添加3个商品1个数量到购物车，添加成功")

    def test004(self):
        
        print("测试添加1个商品99个数量到购物车，添加成功")

    def test005(self):
        
        print("测试添加1个商品100个数量到购物车，添加失败")

    def test006(self):
        
        print("测试添加2个商品99个数量到购物车，添加成功")

    def test007(self):
        
        print("测试添加3个商品99个数量到购物车，添加成功")

    def test008(self):
        
        print("测试添加2个商品100个数量到购物车，添加失败")

    def test009(self):
        
        print("测试添加3个商品100个数量到购物车，添加失败")

    def test010(self):
        
        print("测试未登录时，添加商品到购物车失败")

    def test011(self):
        
        print("测试添加20个商品，每个商品99个到购物车，添加成功")

    def test012(self):
        
        print("测试添加21个商品，每个商品1个到购物车，添加失败")

    def test013(self):
        
        print("测试重复添加同样的商品，从0开始，每次添加1个，重复10次，添加成功")

    def test014(self):
        
        print("测试重复添加同样的商品，从99开始，重复添加1个，添加失败")

    def test015(self):
        
        print("测试购物车商品种类达到20时，继续添加新的商品，添加失败")

    def test016(self):
        
        print("测试修改购物车中的商品数量从99修改到1个，修改成功")

    def test017(self):
        
        print("测试修改购物车中的商品数量从1修改到99个，修改成功")

    def test018(self):
        
        print("测试修改购物车中的商品数量从1修改到100个，修改失败")

    def test019(self):
        
        print("测试修改购物车中的商品数量从1修改到0个，修改失败")

    def test020(self):
        
        print("测试添加0个商品到购物车，添加失败")

    def test021(self):
        
        print("测试添加1个商品，数量为0，添加失败")

    def test022(self):
        
        print("测试添加的商品不存在，添加失败")

    def test023(self):
        
        print("测试添加的商品中有非法字符，添加失败")

    def test024(self):
        
        print("测试添加商品名称为Null的商品，添加失败")

    def test025(self):
        
        print("测试添加1个商品，商品数量是-1，添加失败")

    def test026(self):
        
        print("测试添加1个商品，商品数量是字母a，添加失败")

    def test027(self):
        
        print("测试添加1个商品，商品数量是“.”，添加失败")

    def test028(self):
        
        print("测试添加1个商品，商品数量是Null，添加失败")

    def test029(self):
        
        print("测试添加的商品名称，长度超过了规定，添加失败")

    def test030(self):
        
        print("测试添加的商品名称，长度低于规定，添加失败")

    def test031(self):
        
        print("测试添加的商品名称为空，添加失败")

    def test032(self):
        
        print("测试添加的商品，商品数量为空，添加失败")

    def test033(self):
        
        print("测试删除1个商品，删除成功")

    def test034(self):
        
        print("测试删除1个商品，删除的商品不存在，删除失败")

    def test035(self):
        
        print("测试删除3个商品，删除成功")

    def test036(self):
        
        print("测试删除3个商品，第二个不存在，删除成功，第二个自动忽视")

    def test037(self):
        
        print("测试删除20个商品，全部删除成功")

    def test038(self):
        
        print("测试删除的商品名称长度超过规定，删除成功")

    def test039(self):
        
        print("测试删除的商品名称为Null，删除失败")

    def test040(self):
        
        print("测试删除的商品长度低于规定，删除成功")

    def test041(self):
        
        print("测试未登录添加商品到购物车，添加失败")

    def test042(self):
        
        print("测试未登录修改购物车的商品，修改失败")

    def test043(self):
        
        print("测试未登录删除购物车的商品，删除失败")

    def test044(self):
        
        print("测试未登录查询购物车的商品，查询失败")

    def test045(self):
        
        print("测试查询空购物车，查询成功")

    def test046(self):
        
        print("测试查询购物车中有1个商品，数量为1，查询成功")

    def test047(self):
        
        print("测试查询购物车中有1个商品，数量为99，查询成功")

    def test048(self):
        
        print("测试查询购物车中有3个商品，数量为99，查询成功")

    def test049(self):
        
        print("测试查询购物车中有3个商品，数量为1，查询成功")

    def test050(self):
        
        print("测试查询购物车中有1个商品，商品数量为0，查询失败")

    def test051(self):

        print("测试查询购物车中有3个商品，商品数量为0，查询失败")

    def test052(self):
        
        print("测试查询购物车中的商品名称超过规定长度")

    def test053(self):
        
        print("测试查询购物车中的商品名称低于规定长度")

    def test054(self):
        
        print("测试查询购物车中的商品名称数据内容不符合需求")

    def test055(self):
        
        print("测试查询购物车中的商品名称中有SQL注入代码，查询成功没有影响")

    def test056(self):
        
        print("测试查询购物车中的商品名称中有XSS注入代码，查询成功没有影响")

    def test057(self):
        
        print("测试查询购物车中的商品名称中有色情、暴力等非法信息，查询失败，自动屏蔽")

    def test058(self):
        
        print("测试查询购物车中的商品的价格超过规定")

    def test059(self):
        
        print("测试查询购物车中的商品的价格超过规定，查询成功，正常显示")

    def test060(self):
        
        print("测试查询购物车中的商品的价格是负数，查询成功，正常显示")

    def test061(self):
        
        print("测试查询购物车中的商品的价格是Null，查询成功，正常显示")

    def test62(self):
        
        print("测试查询二十个商品,每个商品99个数量，查询成功")

    def test63(self):
        
        print("测试查询二十个商品,每个商品99个数量，3秒查询成功")

    def test64(self):
        
        print("测试购物车中，1个商品的所有属性值都为空，查询成功")

    def test65(self):
        
        print("并发查询，查询成功")

    def test66(self):
        print("测试添加到购物车的商品下架后，查询成功")
