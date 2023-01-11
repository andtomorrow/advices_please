# import sys
# sys.stdin = open('python_swea_02/input.txt', 'r')

# Q1. 공백으로 구분된 정수
print(*map(int, input().split()))

# Q2. 공백으로 구분된 문자열
print(*input().split())

# Q3. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
T = int(input())
for t in range(1, T+1):
    lines_num = int(input())
    for ln in range(lines_num):
        print(int(input()))

# Q4. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
T = int(input())
for t in range(1, T+1):
    lines_num = int(input())
    for ln in range(lines_num):
        print(*map(int, input().split()))

# Q5. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.
T = int(input())
for t in range(1, T+1):
    lines_num = int(input())
    for ln in range(lines_num):
        print(*input().split())

# Q6. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
T = int(input())
for t in range(1, T+1):
    lines_num = int(input())
    for ln in range(lines_num):
        print(*map(int, input().split()))

# Q7. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
T, lines_num = map(int, input().split())
for t in range(1, T+1):
    for ln in range(lines_num):
        print(int(input()))

# Q8. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
T, lines_num = map(int, input().split())
for t in range(1, T+1):
    for ln in range(lines_num):
        print(*map(int, input().split()))

# Q9. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
T, lines_num = map(int, input().split())
for t in range(1, T+1):
    for ln in range(lines_num):
        print(*map(int, input().split()))