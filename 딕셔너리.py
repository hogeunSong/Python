scores={'c/c++':'A', 'Java':'B+', 'mobile':'C','secure':'a+', 'haking':'F','system':'C+'}

print('일부과목조회')

print(scores['Java'])
print(scores['system'])

print('파이썬, OS과목 삽입')

scores['python']='A'
scores['OS']='A+'

print(scores)

print('Java와 system의 성적을 수정')

scores['Java']='F'
scores['system']='A'

print(scores)


print('최종성적표 출력')
for key in scores.keys():
    print(key, ':', scores[key])
