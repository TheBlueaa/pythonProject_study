#电话号码异常数据分析

yidong = '13 15 17 18 19'
guding = '010 021 022 025 0888 0555'

while True:
    #提示用户输出一个电话号码
    num = input("请输入一个电话号码：")
    if num.strip() == 'exit':
        break
    #判断用户电话号码不能为空
    if not num:
        print("电话号码不能为空")
        continue
    # 排除用户误输入空格的情况
    num  = num.strip()
    # 排除用户输入非中文的情况
    if not num.isdigit():
        print("您输入的是一个无效的电话号码")
        continue
    #如果判断用户是否输入的移动电话号码
    if num[:2] in yidong and len(num) == 11:
        print("您输入的是一个移动的电话号码")
        continue
    #判断用户是否输入的固定电话号码
    if num.startswith('0') :
        if num[:3] in guding and len(num) == 11 or (num[:4] in guding and len(num)) ==12:
                print("这是一个固定电话")
                continue
    #判断用户输入的是否是 广告电话
    if num.startswith('400') and len(num) ==10:
        print("这是一个广告电话")
        continue
    print("无法识别这个电话")

print("退出程序")
