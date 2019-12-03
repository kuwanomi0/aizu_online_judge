# ITP1_2_D
# Circle in a Rectangle
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_D
# encode : utf-8
W, H, x, y, r = map(int, input().split())
if r <= x <= (W-r) and r <= y <= (H-r):
    print('Yes')
else :
    print('No')