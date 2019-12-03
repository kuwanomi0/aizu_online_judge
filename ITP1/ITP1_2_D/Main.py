# ITP1_2_D
# Circle in a Rectangle
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_D
# encode : utf-8
numberList = list(map(int, input().split()))
numberList.sort()
print("{0[0]} {0[1]} {0[2]}".format(numberList))