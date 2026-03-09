MOD = 10**9 + 7


def solve() -> None:
	n = 2025

	# 结论：合法方案数 = 2^floor((n-1)/2)
	# 题目 n=2025，因此指数是 1012。
	ans = pow(2, (n - 1) // 2, MOD)
	print(ans)


if __name__ == "__main__":
	solve()
