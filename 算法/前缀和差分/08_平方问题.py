'''
tb 给了 fc 一个数组 A 。

随后， tb 对 fc 进行了 q 次询问，每次询问给出一个整数 x ，
需要 fc 给出包含了 x 位置且区间和为完全平方数的连续子数组个数。


完全平方数：存在正整数 t ，满足 t^2 = x 的数 x 。 
'''

# 方法：前缀和 + 差分（怎么会没想到差分呢😭）
import sys
from math import isqrt


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	it = iter(data)
	n = next(it)
	q = next(it)
	arr = [next(it) for _ in range(n)]

	# diff[i] 表示位置 i 的贡献增量（1-based）
	diff = [0] * (n + 1)

	for l in range(n):
		s = 0
		for r in range(l, n):
			s += arr[r]
			rt = isqrt(s)
			if rt * rt == s:
				diff[l] += 1
				diff[r + 1] -= 1

	
	for pos in range(1, n + 1):
		diff[pos] += diff[pos - 1]

	diff.pop()  # 去掉最后一个元素，保持与 arr 长度一致

	out: list[str] = []
	for _ in range(q):
		x = next(it)
		out.append(str(diff[x-1]))

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	solve()

