# Q1. 5
num = int(input())
print(num)

# Q2. 2 5
num1, num2 = map(int, input().split())
print(num1, num2)

# Q3. 1 2 3
num1, num2, num3 = map(int, input().split())
print(num1, num2, num3)

# Q4. word1 word2 word3
words = []
usr_input = input().split()
for elm in usr_input:
    words.append(elm)
print(*words)

# Q5. 1 2 3 4 5
numbers = []
usr_input = map(int, input().split())
for elm in usr_input:
    numbers.append(elm)
print(*numbers)

# Q6. -10 10
a, b = map(int, input().split())
print(a, b)

# Q7. a b c d e
characters = []
usr_input = input().split()
for elm in usr_input:
    characters.append(elm)
print(*characters)

# Q8. 3 17 1 39 8 41 2 32 99 2
usr_input = map(int, input().split())
numbers = list(usr_input)
print(*numbers)

# Q9. 1 4 0 10 2 3 9
usr_input = map(int, input().split())
numbers = list(usr_input)
print(*numbers)