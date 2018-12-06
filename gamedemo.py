#!/usr/bin/env python
#coding:utf-8
import random


score = 0     #记录游戏的分数
matix = [[0 for i in range(4)] for i in range(4)]     #初始化生成一个4*4的列表，列表元素全为0



#notzero函数的作用：游戏界面上非零的时候才显示，当为0的时候，让其显示空
def notzero(s):
    return s if s !=0 else ''         #非零的话返回本身，否则返回''


def display():                   #显示界面的函数
    print("\r\
          ┌──┬──┬──┬──┐\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          └──┴──┴──┴──┘" \
          % (notzero(matix[0][0]), notzero(matix[0][1]), notzero(matix[0][2]), notzero(matix[0][3]), \
             notzero(matix[1][0]), notzero(matix[1][1]), notzero(matix[1][2]), notzero(matix[1][3]), \
             notzero(matix[2][0]), notzero(matix[2][1]), notzero(matix[2][2]), notzero(matix[2][3]), \
             notzero(matix[3][0]), notzero(matix[3][1]), notzero(matix[3][2]), notzero(matix[3][3]),)
          )       #



def init():                        #初始化矩阵
    initNumFlag = 0
    while 1:
        k = 2 if random.randrange(0,10) > 1 else 4   #当生成随机数大于1的时候k=2否则k=4 生成2和4的概率为9:1
        s = divmod(random.randrange(0,16),4)         #生成矩阵初始化的下标 比如divmod(15,4)的话，s为(3,3)正好可以作为矩阵下标
        if matix [s[0]][s[1]] == 0:                  #只有当其值不为0的时候才能赋值，避免第二个值重复
            matix[s[0]][s[1]] = k
            initNumFlag += 1
            if initNumFlag ==2:                      #当initNumFlag==2的话表示矩阵力两个随机数都已经生成了，退出循环
                break
        display()


def addRandomNum():              #处理完移动后添加一个新的随机数
    while 1:
        k = 2 if random.randrange(0,10) > 1 else 4
        s = divmod(random.randrange(0,16),4)
        if matix [s[0]][s[1]] == 0:
            matix[s[0]][s[1]] = k
            break
    display()                   #随机数添加完之后就直接调用显示函数，直接显示一下游戏界面


def check():              #检查游戏有没有GG
    for i in range(4):              #按每一排循环4次
        for j in range(3):          #如果矩阵中有0的存在，或者有相邻的数就表示游戏还可以继续运行，否则就GG
            if matix[i][j] == 0 or matix[i][j] == matix[i][j+1] or matix[j+1][i]:
                return True
    else:
        return False


def moveRight():                       #向右移动处理函数
    global score
    for i in range(4):
        for j in range (3, 0, -1):
            for k in range(j-1, -1, -1):
                if matix[i][k] > 0:
                    if matix[i][j] == 0:
                        matix[i][j] = matix[i][k]
                        matix[i][k] = 0
                    elif matix[i][j] == matix [i][k]:
                        matix[i][j] *= 2
                        score += matix[i][j]         #将当前数作为score加上
                        matix[i][k] = 0
                    break
    addRandomNum()


def moveUp():                     #向上
    global score
    for i in range(4):
        for j in range(3):
            for k in range(j + 1, 4):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                        matix[j][i] = matix[k][i]
                        matix[k][i] = 0
                    elif matix[k][i] == matix[j][i]:
                        matix[j][i] *= 2
                        score += matix[j][i]
                        matix[k][i] = 0
                    break
    addRandomNum()





def moveDown():                        #向下
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                        matix[j][i] = matix[k][i]
                        matix[k][i] = 0
                    elif matix[j][i] == matix[k][i]:
                        matix[j][i] *= 2
                        score += matix[j][i]
                        matix[k][i] = 0
                    break
    addRandomNum()


def moveLeft():                  #向左
    global score
    for i in range(4):
        for j in range(3):
            for k in range(1 + j, 4):
                if matix[i][k] > 0:
                    if matix[i][j] == 0:
                        matix[i][j] = matix[i][k]
                        matix[i][k] = 0
                    elif matix[i][j] == matix[i][k]:
                        matix[i][j] *= 2
                        score += matix[i][j]
                        matix[i][k] = 0
                    break
    addRandomNum()




def main():
    print("       \033[33;1mWelcome to the Game of 2048!\033[0m")
    flag = True
    init()
    while flag:                   # 循环的标志
        print('               \033[33;1m You Score:%s\033[0m' % (score))
        d = input('\033[33;1m (↑:w) (↓:s) (←:a) (→:d),q(uit) :\033[0m')  # 不断处理用户输入
        if d == 'a':
            moveLeft()
            if not check():                 # 检查游戏是否GG
                print('GG')
                flag = False                # GG的话直接退出
        elif d == 's':
            moveDown()
            if not check():
                print('GG')
                flag = False
        elif d == 'w':
            moveUp()
        if not check():
            print('GG')
            flag = False
        elif d == 'd':
            moveRight()
            if not check():
                print('GG')
                flag = False
        elif d == 'q':           # 退出
            break
        else:                     # 对用户的其他输入不做处理
            pass

    if __name__ == '__main__':
        main()