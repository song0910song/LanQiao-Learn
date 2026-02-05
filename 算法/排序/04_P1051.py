# 谁拿了最多奖学金

n = int(input())

scholarships = {}
total = 0
for i in range(n):
    name,final_score,class_score,l,w,eassy = input().split()
    if int(final_score) > 80 and int(eassy) >= 1:
        scholarships[name] = scholarships.get(name, 0) + 8000
    if int(final_score) > 85 and int(class_score) > 80:
        scholarships[name] = scholarships.get(name, 0) + 4000
    if int(final_score) > 90:
        scholarships[name] = scholarships.get(name, 0) + 2000
    if int(final_score) > 85 and w=='Y':
        scholarships[name] = scholarships.get(name, 0) + 1000
    if int(class_score) > 80 and l=='Y':
        scholarships[name] = scholarships.get(name, 0) + 850
    
total = sum(scholarships.values())
scholarships_sorted = sorted(scholarships.items(), key=lambda a:a[1], reverse=True)
print(scholarships_sorted[0][0])
print(scholarships_sorted[0][1])
print(total)