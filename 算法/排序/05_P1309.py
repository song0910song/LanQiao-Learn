# 瑞士轮
n, r, q = map(int, input().split())

scores = list(map(int, input().split()))
m = list(map(int, input().split()))

players = [[scores[i], m[i], i+1] for i in range(2*n)]
players.sort(key=lambda a:(-a[0], a[2]))

for _ in range(r):
    winners = []
    losers = []
    temp = [0] * 2*n

    for i in range(0, 2*n, 2):
        p1 = players[i]
        p2 = players[i+1]

        if p1[1] > p2[1]:
            winners.append(i)
            losers.append(i+1)
        else:
            winners.append(i+1)
            losers.append(i)
        
    for i in range(n):
        idx = winners[i]
        players[idx][0] += 1
    
    i=j=k=0

    while i < n and j < n:
        winner = winners[i]
        loser = losers[j]

        if (players[winner][0] > players[loser][0]) or (players[winner][0] == players[loser][0] and players[winner][2] < players[loser][2]):
            temp[k] = players[winner]
            i += 1
            k += 1
        else:
            temp[k] = players[loser]
            j += 1
            k += 1
        
    while i < n:
        temp[k] = players[winners[i]]
        i += 1
        k += 1
    
    while j < n:
        temp[k] = players[losers[j]]
        j += 1
        k += 1
    
    for i in range(2*n):
        players[i] = temp[i]

print(players[q-1][2])



