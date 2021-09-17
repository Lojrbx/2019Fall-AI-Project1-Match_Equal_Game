import Match as mt
import copy
class NumberNode:
    #   初始化函数
    def __init__(self, num_array, Order):
        self.array = num_array
        self.node_data = mt.get_num(num_array)
        self.order = Order  #用于存储在equal数组中的序号，变换后可以填回
        self.flag_change = 0
        self.flag_add = 0
        self.flag_remove = 0
        #   保存移动后可变成的状态
        self.next_add_state = []
        self.next_remove_state = []
        self.next_change_state = []
        #   计数
        self.count_change = 0
        self.count_add = 0
        self.count_remove = 0
        self.find_next_state()
        return

    #   函数，根据当前数字判断进行一根火柴棍的操作后可以变成的数字
    def find_next_state(self):

        if self.node_data == 0:
            self.next_add_state.append(8)
            return
        if self.node_data == 1:
            self.next_add_state.append(7)
            return
        if self.node_data == 2:
            self.next_change_state.append(3)
            return
        if self.node_data == 3:
            self.next_change_state.append(2)
            self.next_change_state.append(5)
            self.next_add_state.append(9)
            return
        if self.node_data == 4:
            return
        if self.node_data == 5:
            self.next_change_state.append(3)
            self.next_add_state.append(6)
            self.next_add_state.append(9)
            return
        if self.node_data == 6:
            self.next_add_state.append(8)
            self.next_change_state.append(9)
            self.next_remove_state.append(5)
            return
        if self.node_data == 7:
            self.next_remove_state.append(1)
            return
        if self.node_data == 8:
            self.next_remove_state.append(0)
            self.next_remove_state.append(9)
            self.next_remove_state.append(6)
            return
        if self.node_data == 9:
            self.next_remove_state.append(5)
            self.next_remove_state.append(3)
            self.next_add_state.append(8)
            self.next_change_state.append(6)
            return

    #   函数，检查是否完成对当前nunbernode所有change的搜索
    def check_change(self):
        if self.count_change == len(self.next_change_state):
            self.flag_change = 1
        return
    #   函数，检查是否完成对当前nunbernode所有add的搜索
    def check_add(self):
        if self.count_add == len(self.next_add_state):
            self.flag_add = 1
        return
    #   函数，检查是否完成对当前nunbernode所有remove的搜索
    def check_remove(self):
        if self.count_remove == len(self.next_remove_state):
            self.flag_remove = 1
        return
    #   函数，移动火柴棍
    def change_stick(self):
        self.node_data = self.next_change_state[self.count_change]
        self.count_change += 1
        return
    #   函数，增加火柴棍
    def add_stick(self):
        self.node_data = self.next_add_state[self.count_add]
        self.count_add += 1
        return
    #   函数，减少火柴棍
    def remove_stick(self):
        self.node_data = self.next_remove_state[self.count_remove]
        self.count_remove += 1
        return

    #   函数，清零所有的flag count next_state
    def clear_all(self):
        self.flag_change = 0
        self.flag_add = 0
        self.flag_remove = 0
        #self.next_add_state = []
        #self.next_remove_state = []
        #self.next_change_state = []
        self.count_change = 0
        self.count_add = 0
        self.count_remove = 0
        self.node_data = mt.get_num(self.array)
        return


class SigNode:
    #   初始化函数
    def __init__(self, sig_array, Order):
        self.array = sig_array
        self.node_data = mt.get_sig(sig_array)
        self.order = Order
        self.flag_change = 0    #变两根的时候可能用到
        self.flag_add = 0
        self.flag_remove = 0
        #   保存移动后可变成的状态
        self.next_add_state = []
        self.next_remove_state = []
        self.next_change_state = [] #change只在变两根的时候用到
        #   计数
        self.count_change = 0
        self.count_add = 0
        self.count_remove = 0
        self.find_next_state()
        return

    #   函数，根据当前数字判断进行一根火柴棍的操作后可以变成的数字
    def find_next_state(self):

        if self.node_data == '-':
            self.next_add_state.append('+')
            self.next_change_state.append('*')
            return
        if self.node_data == '+':
            self.next_remove_state.append('-')
            self.next_change_state.append('*')
            return
        if self.node_data == '*':
            self.next_change_state.append('-')
            self.next_change_state.append('+')
            return


    #   函数，检查是否完成对当前signode所有change的搜索
    def check_change(self):
        if self.count_change == len(self.next_change_state):
            self.flag_change = 1


    #   函数，检查是否完成对当前signode所有add的搜索
    def check_add(self):
        if self.count_add == len(self.next_add_state):
            self.flag_add = 1
        return 1

    #   函数，检查是否完成对当前nunbernode所有remove的搜索
    def check_remove(self):
        if self.count_remove == len(self.next_remove_state):
            self.flag_remove = 1
        return

    #   函数，移动火柴棍
    def change_stick(self):
        self.node_data = self.next_change_state[self.count_change]
        self.count_change += 1
        return

    #   函数，增加火柴棍
    def add_stick(self):
        self.node_data = self.next_add_state[self.count_add]
        self.count_add += 1
        return

    #   函数，减少火柴棍
    def remove_stick(self):
        self.node_data = self.next_remove_state[self.count_remove]
        self.count_remove += 1
        return

    #   函数，清零所有的flag count next_state
    def clear_all(self):
        self.flag_change = 0
        self.flag_add = 0
        self.flag_remove = 0
        #self.next_add_state = []
        #self.next_remove_state = []
        #self.next_change_state = []
        self.count_change = 0
        self.count_add = 0
        self.count_remove = 0
        self.node_data = mt.get_sig(self.array)
        #self.find_next_state()
        return




#   搜索算法（只移动一根火柴棍的情况）
#   原始的equal，复制一个进行修改操作，从其中转换出一个[],储存各个节点，并复制一个进行修改操作。
#   首先考虑change的情况，只对NumNode能进行change操作，然后从[]按顺序取出，
#   取出后对每个节点进行所有的change操作，每进行一次，就把值读入equal，判定是否为等式，不为等式要把initial的复制回去,

#   再考虑remove的情形，从[]中按顺序取出，取出后，对被取出的进行remove，然后修改复制的equal，
#   再从[]中除已被取出的元素外取新的结点进行add操作，add后存入复制的equal，然后判定，不为等式要把节点和equal都恢复，但要保留remove已完成的标记，清除add已完成的标记

#   最终返回的是[1/0(有无解)，equal等式]
def search_solution(equal_initial):
    #   先判定等式是否成立，如果成立就不需要再变换
    if mt.judge_equal(equal_initial):
        return [0,equal_initial]
    equal = copy.deepcopy(equal_initial)
    #   将等式取出到list
    Nlist_initial = []
    for i in range(len(equal_initial)):
        if (equal_initial[i] != mt.num_empty) & (i != 2):
            Nlist_initial.append(NumberNode(equal_initial[i], i))
        else:
            if i ==2 :
                Nlist_initial.append(SigNode(equal_initial[i], i))
    #   复制一个Nlist
    Nlist = copy.deepcopy(Nlist_initial)
    #   先考虑change操作
    for i in range(len(Nlist_initial)):
        #   change操作只能对数字节点（移动一根火柴棍时）
        if isinstance(Nlist_initial[i],NumberNode):
            # 循环 直到该节点完成全部change操作
            while True:
                #   先检查数字节点是否已经完成了全部的change操作：
                Nlist[i].check_change()
                if Nlist[i].flag_change != 1:
                    #   对取出的数字节点进行change
                    #   这里操作的都是复制品
                    Nlist[i].change_stick()
                    #   将change后的数字填入原等式中
                    equal[Nlist[i].order] = mt.get_array(Nlist[i].node_data)
                    #   判定是否为1
                    if mt.judge_equal(equal) == 1:
                        #return 1
                        return [1, equal]
                    else:
                        #   不为1，要恢复原来的equal,此时虽然数字节点的值变了，但change的下一个状态没变。
                        equal = copy.deepcopy(equal_initial)
                else:
                    Nlist[i].clear_all()
                    break
    #   再考虑remove + add操作
    for i in range(len(Nlist_initial)):
        #   先按顺序取出，这里SigNode也可以取出
        while True:
            Nlist[i].check_remove()
            #   当前取出的节点没有完成全部的remove操作
            if Nlist[i].flag_remove != 1:
                #   则对当前节点进行remove
                Nlist[i].remove_stick()
                #   remove后的数字填入原等式，然后进入add
                equal[Nlist[i].order] = mt.get_array(Nlist[i].node_data)
                for j in range(len(Nlist_initial)):
                    #   对除了本身之外的所有节点进行add操作
                    if i != j:
                        while True:
                            Nlist[j].check_add()
                            #  如果当前节点没有完成全部的add操作
                            if Nlist[j].flag_add != 1:
                                #   则对当前节点进行add操作
                                Nlist[j].add_stick()
                                #   将add后的数字填入原等式中
                                equal[Nlist[j].order] = mt.get_array(Nlist[j].node_data)
                                #   判定是否为1
                                if mt.judge_equal(equal) == 1:
                                    #return 1
                                    return [1, equal]
                                else:
                                    #   不为1，把add改变的equal中的元素恢复
                                    equal[Nlist[j].order] = copy.deepcopy(equal_initial[Nlist[j].order])
                            #   如果当前节点完成了全部的add操作
                            else:
                                Nlist[j].clear_all()
                                break
                #   全部其他节点都遍历完add了，但是没有等式解出现
                #   把remove改变的equal中的节点恢复
                equal = copy.deepcopy(equal_initial)
            else:
                Nlist[i].clear_all()
                break

    return [0,equal_initial]


#   寻找等式的解
def equal_solution(equal_initial):
    #   计数迭代次数
    count = 0
    #   这里无需判断原来是否是等式
    equal = copy.deepcopy(equal_initial)
    #   将等式取出到list
    Nlist_initial = []
    for i in range(len(equal_initial)):
        if (equal_initial[i] != mt.num_empty) & (i != 2):
            Nlist_initial.append(NumberNode(equal_initial[i], i))
        else:
            if i ==2 :
                Nlist_initial.append(SigNode(equal_initial[i], i))
    #   复制一个Nlist
    Nlist = copy.deepcopy(Nlist_initial)
    #   先考虑change操作
    for i in range(len(Nlist_initial)):
        #   change操作只能对数字节点（移动一根火柴棍时）
        if isinstance(Nlist_initial[i],NumberNode):
            # 循环 直到该节点完成全部change操作
            while True:
                #   先检查数字节点是否已经完成了全部的change操作：
                Nlist[i].check_change()
                if Nlist[i].flag_change != 1:
                    #   对取出的数字节点进行change
                    #   这里操作的都是复制品
                    Nlist[i].change_stick()
                    count += 1
                    #   将change后的数字填入原等式中
                    equal[Nlist[i].order] = mt.get_array(Nlist[i].node_data)
                    #   判定是否为1
                    if mt.judge_equal(equal) == 1:
                        #return 1
                        return [1, equal, count]
                    else:
                        #   不为1，要恢复原来的equal,此时虽然数字节点的值变了，但change的下一个状态没变。
                        equal = copy.deepcopy(equal_initial)
                else:
                    Nlist[i].clear_all()
                    break
    #   再考虑remove + add操作
    for i in range(len(Nlist_initial)):
        #   先按顺序取出，这里SigNode也可以取出
        while True:
            Nlist[i].check_remove()
            #   当前取出的节点没有完成全部的remove操作
            if Nlist[i].flag_remove != 1:
                #   则对当前节点进行remove
                count += 1
                Nlist[i].remove_stick()
                #   remove后的数字填入原等式，然后进入add
                equal[Nlist[i].order] = mt.get_array(Nlist[i].node_data)
                for j in range(len(Nlist_initial)):
                    #   对除了本身之外的所有节点进行add操作
                    if i != j:
                        while True:
                            Nlist[j].check_add()
                            #  如果当前节点没有完成全部的add操作
                            if Nlist[j].flag_add != 1:
                                #   则对当前节点进行add操作
                                count += 1
                                Nlist[j].add_stick()
                                #   将add后的数字填入原等式中
                                equal[Nlist[j].order] = mt.get_array(Nlist[j].node_data)
                                #   判定是否为1
                                if mt.judge_equal(equal) == 1:
                                    #return 1
                                    return [1, equal, count]
                                else:
                                    #   不为1，把add改变的equal中的元素恢复
                                    equal[Nlist[j].order] = copy.deepcopy(equal_initial[Nlist[j].order])
                            #   如果当前节点完成了全部的add操作
                            else:
                                Nlist[j].clear_all()
                                break
                #   全部其他节点都遍历完add了，但是没有等式解出现
                #   把remove改变的equal中的节点恢复
                equal = copy.deepcopy(equal_initial)
            else:
                Nlist[i].clear_all()
                break

    return [0,equal_initial, count]





