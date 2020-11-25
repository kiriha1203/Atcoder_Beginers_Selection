## 入力
# N
# A1 A2 ... AN

# Aの値がすべて偶数であるとき 2で割ったものと置き換えれる。　最大で何回操作を行えるか。

n = input()
a = list(map(int, input().split()))
cnt = 0

while all(i%2==0 for i in a):
  a = [i/2 for i in a]
  cnt += 1

print(cnt)