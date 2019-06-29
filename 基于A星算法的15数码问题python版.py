#import
import numpy as np
import copy
import matplotlib.pyplot as plt

operation={'right':[0,1],'left':[0,-1],'up':[-1,0],'down':[1,0]}

#逆序数求解
def reverse(arr):
    p=0
    global size
    for i in range(size*size):
        for j in range(1,size*size):
            if arr[0,i] > arr[0,j]:
                p += 1
    return p

# 可解性判断
def solvable_judge(init_state,goal_state):
    m=init_state.reshape((1,-1))
    n=np.argwhere(goal_state == 0)-np.argwhere(init_state == 0)
    m_rev=reverse(m)+sum(n[0])
    if m_rev%2 == 0:
        return 
    else:
        return True

# 在不在opened or closed表中
def inTable(item, table):
    it = item[2]
    for t in table:
        t2 = t[2]
        if (t2 == it).all():
            return True
    return False

#用于元素交换
def swap(direct,table):
    index_1=np.argwhere(table == 0)
    index_2=np.argwhere(table == 0)+operation[direct]
    if index_2[0,0]>3 or index_2[0,0]<0 or index_2[0,1]>3 or index_2[0,1]<0:
        flag = 0
        temp=0
    else:
        flag = 1
        temp=table[index_2[0,0],index_2[0,1]]
        table[index_2[0,0],index_2[0,1]]=0
        table[index_1[0,0],index_1[0,1]]=temp
    return flag,table,temp



# 基于曼哈顿距离的估价函数
def valuation(state_1,goal_state):
    val=0
    global size
    for k in range(1,size*size):
        n = np.argwhere(goal_state == k)
        m = np.argwhere(state_1 == k)
        if k == goal_state[0,0]:
            val += (abs(m[0,0]-n[0,0])+abs(m[0,1]-n[0,1]))*1.5
        elif k == goal_state[1,0] or k == goal_state[0,1]:
            val += (abs(m[0,0]-n[0,0])+abs(m[0,1]-n[0,1]))*1.3
        elif k == goal_state[1,1] or k == goal_state[0,2] or  k == goal_state[2,0]:
            val += (abs(m[0,0]-n[0,0])+abs(m[0,1]-n[0,1]))*1.1
        else:
            val += abs(m[0,0]-n[0,0])+abs(m[0,1]-n[0,1])*1
    return val

# A*算法
def Astar_search(init_item,goal_state):
    opened = []
    closed = []
    opened.append(init_item)
    while len(opened):  # opened表的长度不为0
        current = opened[0]  # 第一个元素
        del opened[0]  # 从opened中删除
        closed.append(current)  # 移动到closed
        print(current[2],"\n vluation:",current[1],"layer:",current[0],"fathet_node:",current[3],"\n")
        if (current[2] == goal_state).all():  # 已经找到目标，直接返回，目标已经插入到closed
            return closed
        #0点移动
        for direct in operation:
            cur = copy.deepcopy(current)
            flag2,new_table,it=swap(direct,cur[2])
            if flag2 == 1:
                son = [current[0] + 1, valuation(new_table, goal_state), cur[2], len(closed)-1]
                if not inTable(son, closed):
                    if not inTable(son, opened):
                        # insert into opened,方法是按step值小的在前排序插入
                        if len(opened) == 0:  # 如果表长度为0，直接插入表中
                            opened.append(son)
                        else:
                            for i in range(len(opened)):
                                if opened[i][1] > son[1]:
                                    opened.insert(i, son)
                                    break
                                elif i == len(opened) - 1:  # 如果表中的元素step值都比son1］小，插入到表最后
                                    opened.append(son)
                                    break
                    else:  # 已经在opened中
                        for i in range(len(opened) - 1):  # 选择layer值小的保留到opened中
                            if (opened[i][2] == son[2]).all():
                                if opened[i][0] > son[0]:
                                    opened[i] = son
                                    break


if __name__ == '__main__':
    #input
    init=np.loadtxt('init_data.txt')
    goal=np.loadtxt('goal_data.txt')
    if init.shape == goal.shape:
        size=init.shape[1]
    #judgement
    flag=solvable_judge(init,goal)
    if flag == 0:
        print("该15数码问题无解")
    else:
        # item = [layer:int,step:int,self:[3:3],father:int]
        init_item = [0,valuation(init, goal),init,-1]  # -1 not father
        closed=Astar_search(init_item,goal)
        print() 
        # 回溯过程
        f = len(closed)-1
        f_list=[]
        while f != -1:
            f_list.append(f)
            f = closed[f][3]
        #打印结果
        for q in range(len(f_list))[::-1]:
            print("第",len(f_list)-q,"步:\n",closed[f_list[q]][2])
        print("综上，一共需要",len(f_list),"步变换为目标状态")