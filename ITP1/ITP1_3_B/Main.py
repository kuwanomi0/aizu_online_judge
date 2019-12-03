# ITP1_3_B
# Print Test Cases
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_B
# encode : utf-8
numlist = []
while (1) :
    x = int(input())
    if x == 0 :
        break
    numlist.append(x)
case = 1
for x in numlist :
    print('Case {0}: {1}'.format(case, x))
    case += 1