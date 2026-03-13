import sys
from collections import defaultdict


def solve() -> None:
	input = sys.stdin.readline
	n, m = map(int, input().split())

    # 斜对角线上的数值相同的 unordered pair 的数量
	main_diag = defaultdict(int)
	# 反斜对角线上的数值相同的 unordered pair 的数量
	anti_diag = defaultdict(int)
	unordered_pairs = 0

	for i in range(n):
		row = list(map(int, input().split()))
		for j, value in enumerate(row):
			# 斜对角线上的 key 是 (i - j, value)，反斜对角线上的 key 是 (i + j, value)
			key1 = (i - j, value)
			key2 = (i + j, value)
			unordered_pairs += main_diag[key1]
			unordered_pairs += anti_diag[key2]
			main_diag[key1] += 1
			anti_diag[key2] += 1

	print(unordered_pairs * 2)


if __name__ == "__main__":
	solve()
