bread = 97
count = 3
maxCount = bread // count
print('빵을 나누어 줄 수 있는 학생 수 : ', maxCount)
rest = bread % count
print('남은 빵 개수 : ', rest)

print('-------------------------------------------------------')

strawberry_bread = int(input('딸기빵의 개수: '))
counting = int(input('1인당 돌아가는 딸기빵의 개수: ' ))
maxCounting = strawberry_bread // counting
print('딸기빵을 나누어 줄 수 있는 학생 수 : ', maxCounting)
rests = strawberry_bread % counting
print('남은 딸기빵의 개수 : ', rests)
