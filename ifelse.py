'''
#循环
for i in range(1, 9):
    for j in range(1, i + 1):
        print("%s*%s=%s" % (j, i, i * j), end=" ")
    print()

for j in range(2,5):
    print(j)

total = 0
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" + ")
    total += i
print(" = %s" % total)

'''
'''
#密码锁程序
pw = "123"
while True:
    pwd = input("请输入初始密码：")
    if not pwd:
        break
    zaiciqueren = input("请再次输入你的密码")
    if pwd == zaiciqueren:
        pw = pwd
        break
    else:
        print("两次输入的密码不一致")
print("你的初始密码为："+pw)
print("正在进入开锁程序")
while True:
    shurumima = input("请输入密码")
    if shurumima in pw:
        print("密码正确")
        break
    else:
        print("密码错误请重试")
'''
