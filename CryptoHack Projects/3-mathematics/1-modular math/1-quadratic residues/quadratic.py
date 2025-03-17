targets = {14, 6, 11}
for i in range(1,29):
 sq = i ** 2 % 29
  if sq in targets:
  print(sq, " has square root ", i)
