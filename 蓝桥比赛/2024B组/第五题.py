import sys


def solve() -> None:
	input = sys.stdin.readline
	t = int(input())
	answers = []

	for _ in range(t):
		n = int(input())
		if n % 3 == 0:
			answers.append(str(2 * n))
		else:
			answers.append(str(n))

	sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
	solve()
