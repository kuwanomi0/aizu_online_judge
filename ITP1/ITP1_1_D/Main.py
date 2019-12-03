# ITP1_1_D
# Watch
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_D
# encode : utf-8
S = int(input())
h = S // 3600
m = (S % 3600) // 60
s = S % 60
print("{}:{}:{}".format(h,m,s))