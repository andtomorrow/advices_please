# # 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.
# 단, index() / find() 메서드는 사용하지마세요.

usr_input = input('문자열을 입력하세요 > ')
if 'e' not in usr_input:
    e_index = -1

else:
    for i in range(len(usr_input)):
        if usr_input[i] == 'e':
            e_index = i
            break

print(e_index)

# ###
# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1
# 출력 예시 2
# 문자열을 입력하세요 > hEllo hypergrowth # 사용자 입력
# 9
# 출력 예시 3
# 문자열을 입력하세요 > java # 사용자 입력
# -1
# #####
# # 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

usr_input = input('문자열을 입력하세요 > ').split()
words = list(dict.fromkeys(usr_input))
summary = {}
for elm in usr_input:
    if elm not in summary.keys():
        summary[elm] = 1
    else:
        summary[elm] += 1
for k, v in summary.items():
    print(k, v)

# ###
# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# hello 1
# 출력 예시 2
# 문자열을 입력하세요 > hello hypergrowth # 사용자 입력
# hello 1
# hypergrowth 1
# 출력 예시 3
# 문자열을 입력하세요 > apple apple banana grape # 사용자 입력
# apple 2
# banana 1
# grape 1
# #####
# # 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

usr_input = input('문자열을 입력하세요 > ')

if 'e' not in usr_input:
    modified_str = usr_input
else:
    e_indexes = []
    modified_str = ''
    for i in range(len(usr_input)):
        if usr_input[i] == 'e':
            e_indexes.append(i)
    remain_indexes = set(range(len(usr_input))) - set(e_indexes)
    remain_indexes = list(remain_indexes)
    for i in remain_indexes:
        modified_str += usr_input[i]
print(modified_str)

# ###
# 출력 예시 1
# 문자열을 입력하세요 > apple # 사용자 입력
# appl
# 출력 예시 2
# 문자열을 입력하세요 > hello # 사용자 입력
# hllo
# 출력 예시 3
# 문자열을 입력하세요 > hEllo # 사용자 입력
# hEllo
# #####
# # 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

usr_input = input('문자열을 입력하세요 > ').split()
word = usr_input[0]
letter = usr_input[1]

if letter not in word:
    letter_cnt = 0
else:
    letter_cnt = 0
    for char in word:
        if char == letter:
            letter_cnt += 1
print(letter_cnt)

# ###
# 출력 예시 1
# 문자열을 입력하세요 > apple p # 사용자 입력
# 2
# 출력 예시 2
# 문자열을 입력하세요 > hello o # 사용자 입력
# 1
# 출력 예시 3
# 문자열을 입력하세요 > hEllo a # 사용자 입력
# 0
# #####
# # 문제 5
# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

usr_input = input('문자열을 입력하세요 > ').split() # list
print(*usr_input, sep='-')

# 출력 예시
# 문자열을 입력하세요 > 010 1234 5678 # 사용자 입력
# 010-1234-5678
# #####
# # 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

usr_input = int(input('양의 정수를 입력하세요 > ')) # 244
if usr_input < 0:
    nums_sum = -1
else:
    nums_sum = 0
    ten_cube_n = 0
    while usr_input // (10 ** ten_cube_n) > 0:
        nums_sum += usr_input % (10 ** (ten_cube_n+1)) // (10 ** ten_cube_n) # 4, 4, 2
        ten_cube_n += 1
print(nums_sum)

# ###
# 출력 예시 1
# 문자열을 입력하세요 > 244 # 사용자 입력
# 10
# 출력 예시 2
# 문자열을 입력하세요 > 1 # 사용자 입력
# 1
# 출력 예시 3
# 문자열을 입력하세요 > -10 # 사용자 입력
# -1