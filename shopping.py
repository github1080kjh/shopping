

shopping_list = {'apple':10,
                 'banana':20,
                 'book':50}

def show_shopping():   #  shopping show
    n = 0
    print('----------------shopping store----------------\n'
          'welcome shopping store!!!!\n'
          'this is my store all shopping!\n'
          '----------------------------------------------')
    for shopping in shopping_list:

        print('%d  --->  %s,%d' % (n,shopping,shopping_list[shopping]))
        n+=1
# show_shopping()   the test
# your_all_money -= shopping_list[your_choice]
# print('you have %d yuan now, and you purchase one %d' % (your_all_money,your_choice))


# 需要再次购买
def buy_again():
    global flag
    buy_again = input('you want to buy again:')
    if buy_again == 'yes':
        show_shopping()
        main()
    else:
        print('wlcome again!')
        flag = False
    return flag
# 主函数
def main():
    # 调用全局变量
    global your_all_money
    global flag
    while flag == True:
        exit = input('exit now:')
        if exit == 'yes':
            print('welcome again')
            flag = False
        else:
            show_shopping()   # show
            your_choice= input('please enter you want to buy commodity:')
            if your_choice in shopping_list:
                print('you need pay %d yuan !!' % shopping_list[your_choice])
                pay_choice = input('make sure to pay:')
                if pay_choice == 'yes':
                    your_all_money -= shopping_list[your_choice]
                    print('you have %d yuan now, and you purchase one %s' % (your_all_money,your_choice))

                    flag = buy_again()

                else:

                    flag = buy_again()
            else:
                print('please enter again!')
                main()
flag = True    # 控制直接退出程序
your_all_money = int(input('your all money:'))
main()
