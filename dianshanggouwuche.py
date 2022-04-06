#商品：名称 价格 折扣
#购物车：商品 商品的数量

class goods:
    '''商品类'''
    id_cout = 0
    #装饰器
    #装饰器写法，classmethod用来定义类方法
    @classmethod
    def generate_id(cls):
        cls.id_cout += 1
        return cls.id_cout
    def __init__(self, name , price,discount =1):
        self.id = str(self.generate_id()).zfill(5)
        self.name = name
        self.price = price
        self.discount = discount
    def calc_price(self):
        '''计算商品后打折的价格'''
        return self.price * self.discount
g1 = goods('iphone 11', 7000 ,0.9)
g2 = goods('huawei', 9999)
g3 = goods('xiaomi', 1000 ,0.1)
print("商品1的名字是{name},他的价格是{price},他的折扣是{discount},打折后的价格是{salc}".\
format(name = g1.name,price = g1.price,discount = g1.discount,salc =g1.calc_price()))
print("商品2的名字是{name},他的价格是{price},他的折扣是{discount},打折后的价格是{salc}".\
format(name = g2.name,price = g2.price,discount = g2.discount,salc =g2.calc_price()))
print("商品3的名字是{name},他的价格是{price},他的折扣是{discount},打折后的价格是{salc}".\
format(name = g3.name,price = g3.price,discount = g3.discount,salc =g3.calc_price()))
class Cart:
    '''购物车'''
    def __init__(self):
        self.cart = {}
        self.goods_list = []
    def add(self,goods, num = 1):
        '''在购物车里面添加商品'''
        if goods in self.goods_list:
            self.cart[goods.id] += num
        else:
            self.goods_list.append(goods)
            self.cart[goods.id] = num
    def remove(self, goods ,num = 1):
        '''从购物车里面删除商品'''
        if goods in self.goods_list:
            self.cart[goods.id] -= num
        else:
            print("已经没有商品了")
        if self.cart[goods.id] <= 0:
            del self.cart[goods]
            self.goods_list.remove(goods)

cart = Cart()
cart.add(g1)
cart.add(g2,3)
cart.add(g3,2)

