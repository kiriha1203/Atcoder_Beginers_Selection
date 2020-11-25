## 入力
# a b

#積が奇数なら Odd と、 偶数なら Even と出力せよ。

a,b = map(int, input().split())

if (a * b % 2 == 0):
  print('Even')
else :
  print('Odd')
