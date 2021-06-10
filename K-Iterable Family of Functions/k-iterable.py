def arrow(a, b, n):
if n == 1:
		return reduce(lambda x, y: x * y, [a] * b)
	return reduce(lambda x, y: arrow(y, x, n - 1), [a] * b)


def iterate(x, n):
  total = n
  for num in range(0,x):
      total += arrow(total,total, total)
  return total
