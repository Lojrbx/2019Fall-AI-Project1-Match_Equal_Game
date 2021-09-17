#   火柴棍库
#   各数字的定义（数组），加号减号等于号，
#   由数组得到数字的函数，由数字得到数组的函数，
#   增加火柴棍的函数，减少火柴棍的函数，
#   从等式字符串得到数字和加减号的函数，判断等式是否成立的函数


#   每个数字包括7段，1表示点亮，0表示熄灭，用7位的数组来表示
#   每个符号包括2段，1表示点亮，0表示熄灭，用2位的数组来表示
#   等式数组包含 6 个数字（7位） 1 个运算符号（2位） 1个等号（不变）
#   如：equal = [ [1,1,1,1,1,1,1], [1,1,1,0,0,0,0], [1,1,0,0],
#                        [0,0,0,0,0,0,0], [0,0,0,0,0,0,0],
#                        [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]    ]

num_0 = [1, 1, 1, 1, 1, 1, 0]
num_1 = [0, 1, 1, 0, 0, 0, 0]
num_2 = [1, 1, 0, 1, 1, 0, 1]
num_3 = [1, 1, 1, 1, 0, 0, 1]
num_4 = [0, 1, 1, 0, 0, 1, 1]
num_5 = [1, 0, 1, 1, 0, 1, 1]
num_6 = [1, 0, 1, 1, 1, 1, 1]
num_7 = [1, 1, 1, 0, 0, 0, 0]
num_8 = [1, 1, 1, 1, 1, 1, 1]
num_9 = [1, 1, 1, 1, 0, 1, 1]
num_empty = [0, 0, 0, 0, 0, 0, 0]

sig_add = [1, 1, 0, 0]
sig_minus = [1, 0, 0, 0]
sig_mpl = [0, 0, 1, 1]
sig_empty = [0, 0, 0, 0]


#   从数组得到数字

def get_num(num_array):
    if num_array == num_0:
        return 0
    if num_array == num_1:
        return 1
    if num_array == num_2:
        return 2
    if num_array == num_3:
        return 3
    if num_array == num_4:
        return 4
    if num_array == num_5:
        return 5
    if num_array == num_6:
        return 6
    if num_array == num_7:
        return 7
    if num_array == num_8:
        return 8
    if num_array == num_9:
        return 9
    else:
        return 10




#   从数字/符号得到数组

def get_array(num):
    if num == 0:
        return num_0
    if num == 1:
        return num_1
    if num == 2:
        return num_2
    if num == 3:
        return num_3
    if num == 4:
        return num_4
    if num == 5:
        return num_5
    if num == 6:
        return num_6
    if num == 7:
        return num_7
    if num == 8:
        return num_8
    if num == 9:
        return num_9
    if num == '+':
        return sig_add
    if num == '-':
        return sig_minus
    if num == '*':
        return sig_mpl
    else:
        if len(num) == 7:
            return num_empty
        else:
            if len(num) == 4:
                return sig_empty



#   从数组得到符号

def get_sig(sig):
    if sig == sig_add:
        return '+'
    if sig == sig_minus:
        return '-'
    if sig == sig_mpl:
        return '*'
    else:
        return sig_empty


#   增加数字/符号上火柴棍的函数

def add_match(array, pos):
    if array[pos-1] == 0:
        array[pos-1] = 1
        return 1
    else:
        return 0


#   减少数字/符号上火柴棍的函数

def remove_match(array, pos):
    if array[pos-1] == 1:
        array[pos-1] = 0
        return 1
    else:
        return 0



#   从等式字符串中得到数字的函数
#   返回1 转换成功    返回0 转换失败
#   使用前需要初始化equal

def trans_string(eq_str, equal):
    #   先得到字符串的长度
    len_str = len(eq_str)
    #   先判断等号的个数
    count_eq = 0
    for i in range (len_str):
        if eq_str[i] == "=":
            count_eq += 1
    if count_eq != 1:
        return 0

    #   再判断运算符号的个数
    count_sig = 0
    for i in range (len_str):
        if (eq_str[i] == '+') | (eq_str[i] == '-') | (eq_str[i] == '*'):
            count_sig += 1
    if count_sig != 1:
        return 0


    ##################SEGMENTLINE##############
    #   如果字符串长度超过8或小于5，则不能转换成为等式
    if (len_str > 8) | (len_str < 5):
        return 0
    #   如果长度为5，则3个数字均为1位数
    if len_str == 5:
        #   先判断第4位是不是等于号，若不是，则无法生成等式直接返回error(0)
        if eq_str[3] != '=':
            return 0
        else:
            #   equal的前两位为第一个数，
            equal[0] = num_empty
            equal[1] = get_array(int(eq_str[0]))
            #   equal的第三个元素为符号
            if eq_str[1] == '+':
                equal[2] = sig_add
            else:
                if eq_str[1] == '-':
                    equal[2] = sig_minus
                else:
                    if eq_str[1] == '*':
                        equal[2] = sig_mpl
                    else:
                        #   如果长度为5，且第二位不为运算符，则等式的字符串无法转换为等式，返回error(0)
                        return 0
            #   equal的第四位第五位为第二个1位数
            equal[3] = num_empty
            equal[4] = get_array(int(eq_str[2]))
            #   等式已经验证过
            #   equal的第六第七位为等式右边的数字
            equal[5] = num_empty
            equal[6] = get_array(int(eq_str[4]))
            #   长度为5情况完成
            return 1
    #   长度为6的情形，三个数字中可能有一个为2位数
    if  len_str == 6:
        #   如果等号出现在第4位或第5位，才有可能转换为等式
        if (eq_str[3] != '=') & (eq_str[4] != '='):
            return 0
        #   如果等号出现在第4位
        #   则说明等号前两个数字都为1位数
        if eq_str[3] == '=':
            #   等式的前两个元素为第一位数
            equal[0] = num_empty
            equal[1] = get_array(int(eq_str[0]))
            #   equal的第三个元素为符号
            if eq_str[1] == '+':
                equal[2] = sig_add
            else:
                if eq_str[1] == '-':
                    equal[2] = sig_minus
                else:
                    if eq_str[1] == '*':
                        equal[2] = sig_mpl
                    else:
                        #   如果第二位不为运算符，则等式的字符串无法转换为等式，返回error(0)
                        return 0
            #   equal的第四个元素第五个元素为第二个1位数
            equal[3] = num_empty
            equal[4] = get_array(int(eq_str[2]))
            #   eqaul的第六第七个元素为等号右边的2位数
            equal[5] = get_array(int(eq_str[4]))
            equal[6] = get_array(int(eq_str[5]))
            #   等号出现在第4位的情况完成
            return 1
        #   如果等号出现在第5位
        if  eq_str[4] == '=':
            #   则说明运算符左边或右边的数字为2位数
            #   因此先判断运算符的位置

            #   case 1 运算符在第二位（第二个数字为2位数）
            if (eq_str[1] == '+') | (eq_str[1] == '-') | (eq_str[1] == '*'):
                #   equal前两个元素为第一个数字
                equal[0] = num_empty
                equal[1] = get_array(int(eq_str[0]))
                #   equal第三个元素为运算符
                if eq_str[1] == '+':
                    equal[2] = sig_add
                else:
                    if eq_str[1] == '-':
                        equal[2] = sig_minus
                    else:
                        if eq_str[1] == '*':
                            equal[2] = sig_mpl
                        else:
                            return 0
                #   equal第四五两个元素为运算符后面的两位数
                equal[3] = get_array(int(eq_str[2]))
                equal[4] = get_array(int(eq_str[3]))
                #   equal第六七两个元素为等号后面的一位数
                equal[5] = num_empty
                equal[6] = get_array(int(eq_str[5]))
                #   case1完成
                return 1
            #   case 2 运算符在第三位（第一个数字为2位数）
            if  (eq_str[2] == '+') | (eq_str[2] == '-') | (eq_str[2] == '*'):
                #   equal前两个元素为第一个数字
                equal[0] = get_array(int(eq_str[0]))
                equal[1] = get_array(int(eq_str[1]))
                #   equal第三个元素为运算符
                if eq_str[2] == '+':
                    equal[2] = sig_add
                else:
                    if eq_str[2] == '-':
                        equal[2] = sig_minus
                    else:
                        if eq_str[2] == "*":
                            equal[2] = sig_mpl
                        else:
                            return 0
                #   equal第四五个元素是第二个数字（1位数）
                equal[3] = num_empty
                equal[4] = get_array(int(eq_str[3]))
                #   equal第六七个元素是等号右边的1位数
                equal[5] = num_empty
                equal[6] = get_array(int(eq_str[5]))
                #   case 2完成
                return 1

    #   长度为7的情形 有两个2位数
    if len_str == 7:
        #   只有等号位于第五位或第六位才可能转换为等式
        if (eq_str[4] != '=') & (eq_str[5] != '='):
            return 0
        #   等号出现在第五位时，等号左边有两种情况
        #   根据运算符的位置划分
        if eq_str[4] == '=':
            #   第一种，第一个数为1位
            if (eq_str[1] == '+') | (eq_str[1] == '-') | (eq_str[1] == '*'):
                #   equal的前两个元素为第一个数字
                equal[0] = num_empty
                equal[1] = get_array(int(eq_str[0]))
                #   equal的第三个元素为运算符
                if eq_str[1] == '+':
                    equal[2] = sig_add
                else:
                    if eq_str[1] == '-':
                        equal[2] = sig_minus
                    else:
                        if eq_str[1] == '*':
                            equal[2] = sig_mpl
                        else:
                            return 0
                #   equal的第四第五个元素为第二个数字（2位）
                equal[3] = get_array(int(eq_str[2]))
                equal[4] = get_array(int(eq_str[3]))
                #   equal的第六第七个元素为等式右边的数字（2位）
                equal[5] = get_array(int(eq_str[5]))
                equal[6] = get_array(int(eq_str[6]))
                #   第一种情况完成
                return 1

            #   第二种，第二个数为1位
            if (eq_str[2] == '+') | (eq_str[2] == '-') | (eq_str[2] == '*'):
                #   equal的前两个元素为第一个数字
                equal[0] = get_array(int(eq_str[0]))
                equal[1] = get_array(int(eq_str[1]))
                #   equal的第三个元素为运算符
                if eq_str[2] == '+':
                    equal[2] = sig_add
                else:
                    if eq_str[2] == '-':
                        equal[2] = sig_minus
                    else:
                        if eq_str[2] == '*':
                            equal[2] = sig_mpl
                        else:
                            return 0
                #   equal的第四第五个元素为第二个数（1位）
                equal[3] = num_empty
                equal[4] = get_array(int(eq_str[3]))
                #   equal的第六第七个元素为等号右边的数字（2位）
                equal[5] = get_array(int(eq_str[5]))
                equal[6] = get_array(int(eq_str[6]))
                #   第二种情况完成
                return 1
        #   等号出现在第六位时
        if  eq_str[5] == '=':
            #   只有一种情况，1位数出现在等号右边
            #   equal的前两元素表示第一个2位数
            equal[0] = get_array(int(eq_str[0]))
            equal[1] = get_array(int(eq_str[1]))
            #   equal的第三个元素为运算符
            if eq_str[2] == '+':
                equal[2] = sig_add
            else:
                if eq_str[2] == '-':
                    equal[2] = sig_minus
                else:
                    if eq_str[2] == '*':
                        equal[2] = sig_mpl
                    else:
                        return 0
            #   equal的第四第五元素表示第二个2位数
            equal[3] = get_array(int(eq_str[3]))
            equal[4] = get_array(int(eq_str[4]))
            #   equal的第六第七元素表示等式右边的1位数
            equal[5] = num_empty
            equal[6] = get_array(int(eq_str[6]))
            #   等号出现在第六位的情况完成
            return 1
    #   长度为8的情形，只有一种情况，三个数字都为2位数
    if len_str == 8:
        #   只有等号出现在第6位才有可能转换为等式
        if eq_str[5] != '=':
            return 0
        #   前两个元素为第一个两位数
        equal[0] = get_array(int(eq_str[0]))
        equal[1] = get_array(int(eq_str[1]))
        #   equal的第三个元素为运算符
        if eq_str[2] == '+':
            equal[2] = sig_add
        else:
            if eq_str[2] == '-':
                equal[2] = sig_minus
            else:
                if eq_str[2] == '*':
                    equal[2] = sig_mpl
                else:
                    return 0
        #   equal的第四第五元素表示第二个2位数
        equal[3] = get_array(int(eq_str[3]))
        equal[4] = get_array(int(eq_str[4]))
        #   equal的第六第七元素表示等式右边的2位数
        equal[5] = get_array(int(eq_str[6]))
        equal[6] = get_array(int(eq_str[7]))
        #   长度为8的情况完成
        return 1


#   判断等式是否成立的函数

def judge_equal(equal):
    #   先考虑一些简单的一定不能成立的情况
    #   每个数字的第二位如果为empty，一定不能成立
    if (equal[1] == num_empty) | (equal[4] == num_empty) |  (equal[6] == num_empty):
        return 0

    #   从字符串转换得到的等式，运算符和等号一定在恰当位置，且有恰当个数，可以转换成数字算式
    else:
        #   设定两个运算数字cal_1 cal_2，和一个结果cal_outcome，以及等式右边的数字cal_3

        #   先对数字进行转换
        #   数字第一位不为空，则为2位数
        if equal[0] != num_empty:
            cal_1 = (get_num(equal[0]))*10 + get_num(equal[1])
        else:
            cal_1 = get_num(equal[1])
        if equal[3] != num_empty:
            cal_2 = (get_num(equal[3]))*10 + get_num(equal[4])
        else:
            cal_2 = get_num(equal[4])
        if equal[5] != num_empty:
            cal_3 = (get_num(equal[5]))*10 + get_num(equal[6])
        else:
            cal_3 = get_num(equal[6])
        #   数字转换完成

        #   根据运算符来进行运算
        if equal[2] == sig_add:
            cal_outcome = cal_1 + cal_2
        else:
            if equal[2] == sig_minus:
                cal_outcome = cal_1 - cal_2
            else:
                if equal[2] == sig_mpl:
                    cal_outcome = cal_1 * cal_2
                else:
                    return 0

        #   判断运算结果与等式右边的数字是否相同
        if cal_3 == cal_outcome:
            return 1
        else:
            return 0
        #   函数结束



def equal2str(equal):
    str = ''
    for i in range(7):
        if i != 2:
            if i == 5:
                str += '='
            if equal[i] == num_0:
                str += '0'
            if equal[i] == num_1:
                str += '1'
            if equal[i] == num_2:
                str += '2'
            if equal[i] == num_3:
                str += '3'
            if equal[i] == num_4:
                str += '4'
            if equal[i] == num_5:
                str += '5'
            if equal[i] == num_6:
                str += '6'
            if equal[i] == num_7:
                str += '7'
            if equal[i] == num_8:
                str += '8'
            if equal[i] == num_9:
                str += '9'
        if i == 2:
            if equal[i] == sig_add:
                str += '+'
            if equal[i] == sig_minus:
                str += '-'
            if equal[i] == sig_mpl:
                str += '*'
    return str






