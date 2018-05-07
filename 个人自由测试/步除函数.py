def 跳步法(denominator,quotient,remainder):
    "使用跳步法，找出余为0的除数"
    global 总步长,N
    步长 = (quotient - remainder) // ((denominator + remainder) % quotient)
    
    quotient_new = quotient - 步长
    denominator_new,remainder_new = divmod(N,quotient_new)
    
    总步长 += 步长
    # print("大数=%d,小数=%d，余=%d" % (denominator_new, quotient_new,remainder_new))
    # print("步长=%d" % 总步长)
    
    return denominator_new, quotient_new, remainder_new


def 跨步法(denominator,quotient,remainder):
    global 总步长,N
    
    quotient_new = quotient - 1

    denominator_new,remainder_new = divmod(N,quotient_new)
   
    总步长 += 1
    # print("大数=%d,小数=%d，余=%d" % (denominator_new, quotient_new,remainder_new))
    # print("步长=%d" % 总步长)
    return denominator_new, quotient_new, remainder_new

import math

N = 50097840248975052365

小数 =  int(math.sqrt(N))
余,大数 = divmod(N,小数)
总步长=0
小步长=0

for i in range(1,100):
    if 余 !=0 :
        if 总步长-小步长 >= 4:
            大数,小数,余=跳步法(大数,小数,余)
        else:
            大数,小数,余=跨步法(大数,小数,余)
        小步长 += (总步长-小步长)
    else:
        print("大数=%d，小数=%d，余=%d，总步长=%d" % (大数,小数,余,总步长))

               
