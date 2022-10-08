my = int(input('정기예금 넣을 액수 : '))
rate = float(input('이자액(%): '))
my += my * rate
my += my * rate
my += my * rate
my += my * rate
my += my * rate

print('5년후 총 수령액: ', int(my), '원')
