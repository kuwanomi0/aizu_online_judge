# ITP1_2_A
# Small, Large, or Equal
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A
# encode : utf-8
a, b = map(int, input().split())
if a < b :
    print('a < b')
elif a > b :
    print('a > b')
elif a == b :
    print('a == b')