emso = [2, 1, 1, 2, 9, 9, 8, 5, 0, 5, 9, 3, 6]
if emso[5] > 2:
    year_of_birth = 1000 + emso[4] * 100 + emso[5] * 10 + emso[6]

else:
    year_of_birth = 2000 + emso[4] * 100 + emso[5] * 10 + emso[6]

print(year_of_birth)