# Test = 'My', 'Name', 'Is', 'You', 'die', '18'
# print("\t".join(Test))
# print(Test.count('die'))
# print(Test.index('g'))

'''这是包含某公司所有销售人员第一季度销售业绩的元组，单位是万元，
其中的每一个元素对应一个销售 人员的信息，人员信息也是一个元组，
包括姓名和业绩，业绩又是一个元组，按照顺序分别是1、2、3 月份的销售额。
需求:找出总销售额最高的那个员工，并将TA的名字和总销售额输出。'''
sales = (
    ("Peter", (78, 70, 65)),
    ("John", (88, 80, 85)),
    ("Tony", (90, 99, 95)),
    ("Henry", (80, 70, 55)),
    ("Mike", (95, 90, 95)),
)

champion = ''
max_amount = 0
for name, quarter_amount in sales:
    total_amount = sum(quarter_amount)
    if total_amount > max_amount:
        champion, max_amount = name, total_amount
print("第一季度的销冠是%s, TA的总销售额是%d万元" % (champion, max_amount))

a =list('I love cake')
a.sort()
print(a)