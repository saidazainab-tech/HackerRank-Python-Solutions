# HackerRank Python Solutions — All 36 Questions
# ================================================
# Kaggle-friendly version with hardcoded inputs

# ============================================
# Day 0: Hello World
# ============================================
print("=== Day 0: Hello World ===")
print("Hello, World!")

# ============================================
# Day 1: Data Types
# ============================================
print("\n=== Day 1: Data Types ===")
i = 4 + 12
d = 4.0 + 4.32
s = 'HackerRank ' + 'is the best place to learn and practice coding!'
print(i)
print(d)
print(s)

# ============================================
# Day 2: Operators
# ============================================
print("\n=== Day 2: Operators ===")
meal_cost = 12.00
tip_percent = 20
tax_percent = 8
tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total = meal_cost + tip + tax
print(round(total))

# ============================================
# Day 3: Conditional Statements
# ============================================
print("\n=== Day 3: Conditional Statements ===")
for n in [3, 4, 6, 22]:
    if n % 2 == 1:
        print(f"n={n}: Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print(f"n={n}: Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print(f"n={n}: Weird")
    else:
        print(f"n={n}: Not Weird")

# ============================================
# Day 4: Class vs Instance
# ============================================
print("\n=== Day 4: Class vs Instance ===")
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1

p = Person(15)
p.amIOld()
for _ in range(3):
    p.yearPasses()
p.amIOld()

# ============================================
# Day 5: Loops
# ============================================
print("\n=== Day 5: Loops ===")
n = 3
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))

# ============================================
# Day 6: Let's Review
# ============================================
print("\n=== Day 6: Let's Review ===")
for s in ["Hacker", "Rank"]:
    print(s[0::2] + " " + s[1::2])

# ============================================
# Day 7: Arrays
# ============================================
print("\n=== Day 7: Arrays ===")
arr = [1, 4, 3, 2]
print(*arr[::-1])

# ============================================
# Day 8: Dictionaries and Maps
# ============================================
print("\n=== Day 8: Dictionaries and Maps ===")
phone_book = {"sam": "99912222", "tom": "11122222", "harry": "12299933"}
for name in ["sam", "edward", "harry"]:
    if name in phone_book:
        print(name + "=" + phone_book[name])
    else:
        print("Not found")

# ============================================
# Say Hello World
# ============================================
print("\n=== Say Hello World ===")
print("Hello, World!")

# ============================================
# Python If-Else
# ============================================
print("\n=== Python If-Else ===")
for n in [3, 4, 6, 22]:
    if n % 2 == 1:
        print(f"n={n}: Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print(f"n={n}: Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print(f"n={n}: Weird")
    else:
        print(f"n={n}: Not Weird")

# ============================================
# Arithmetic Operators
# ============================================
print("\n=== Arithmetic Operators ===")
a, b = 10, 3
print(a + b)
print(a - b)
print(a * b)

# ============================================
# Division
# ============================================
print("\n=== Division ===")
a, b = 10, 3
print(a // b)
print(a / b)

# ============================================
# Loops
# ============================================
print("\n=== Loops ===")
n = 5
for i in range(n):
    print(i ** 2)

# ============================================
# Write a Function
# ============================================
print("\n=== Write a Function ===")
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

for year in [1990, 2000, 2100, 2024]:
    print(f"{year}: {is_leap(year)}")

# ============================================
# Print Function
# ============================================
print("\n=== Print Function ===")
n = 5
result = ""
for i in range(1, n+1):
    result += str(i)
print(result)

# ============================================
# List Comprehensions
# ============================================
print("\n=== List Comprehensions ===")
x, y, z, n = 1, 1, 1, 2
result = [[i,j,k] for i in range(x+1)
                   for j in range(y+1)
                   for k in range(z+1)
                   if i+j+k != n]
print(result)

# ============================================
# Find the Runner-Up Score
# ============================================
print("\n=== Find the Runner-Up Score ===")
arr = sorted(set([2, 3, 6, 6, 5]))
print(arr[-2])

# ============================================
# Nested Lists
# ============================================
print("\n=== Nested Lists ===")
students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
grades = sorted(set([s[1] for s in students]))
second_lowest = grades[1]
result = sorted([s[0] for s in students if s[1] == second_lowest])
for name in result:
    print(name)

# ============================================
# Finding The Percentage
# ============================================
print("\n=== Finding The Percentage ===")
student_marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
query = "Krishna"
avg = sum(student_marks[query]) / len(student_marks[query])
print("{:.2f}".format(avg))

# ============================================
# Lists
# ============================================
print("\n=== Lists ===")
lst = []
commands = [
    ["insert", 0, 5], ["insert", 1, 10], ["insert", 0, 15],
    ["print"], ["append", 9], ["sort"], ["print"], ["pop"],
    ["reverse"], ["print"]
]
for cmd in commands:
    if cmd[0] == 'insert': lst.insert(cmd[1], cmd[2])
    elif cmd[0] == 'print': print(lst)
    elif cmd[0] == 'append': lst.append(cmd[1])
    elif cmd[0] == 'sort': lst.sort()
    elif cmd[0] == 'pop': lst.pop()
    elif cmd[0] == 'reverse': lst.reverse()

# ============================================
# Tuples
# ============================================
print("\n=== Tuples ===")
t = tuple([1, 2, 3])
print(hash(t))

# ============================================
# sWAP cASE
# ============================================
print("\n=== sWAP cASE ===")
def swap_case(s):
    return s.swapcase()
print(swap_case("HackerRank"))

# ============================================
# String Split and Join
# ============================================
print("\n=== String Split and Join ===")
def split_and_join(line):
    return "-".join(line.split())
print(split_and_join("this is a string"))

# ============================================
# What's Your Name?
# ============================================
print("\n=== What's Your Name? ===")
def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")
print_full_name("Harry", "Potter")

# ============================================
# Mutations
# ============================================
print("\n=== Mutations ===")
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
print(mutate_string("abracadabra", 5, 'k'))

# ============================================
# Find a String
# ============================================
print("\n=== Find a String ===")
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count
print(count_substring("ABCDCDC", "CDC"))

# ============================================
# String Validators
# ============================================
print("\n=== String Validators ===")
s = "qA2"
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

# ============================================
# Text Alignment
# ============================================
print("\n=== Text Alignment ===")
thickness = 5
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1+i) + c + (c*i).ljust(thickness-1+i))
for i in range(thickness+1):
    print('  ' + (c*thickness) + ' '*(thickness*3) + (c*thickness))
for i in range(thickness):
    print('  ' + c*(thickness*5-thickness))
for i in range(thickness+1):
    print('  ' + (c*thickness) + ' '*(thickness*3) + (c*thickness))
for i in range(thickness):
    print((' '*(thickness-1-i)) + (c*(2*i+1)).center(thickness) + (' '*(thickness-1-i)))

# ============================================
# Text Wrap
# ============================================
print("\n=== Text Wrap ===")
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))

# ============================================
# Designer Door Mat
# ============================================
print("\n=== Designer Door Mat ===")
n, m = 7, 21
for i in range(1, n//2 + 1):
    pattern = '.|.' * (2*i - 1)
    print(pattern.center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n//2, 0, -1):
    pattern = '.|.' * (2*i - 1)
    print(pattern.center(m, '-'))

# ============================================
# String Formatting
# ============================================
print("\n=== String Formatting ===")
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),
              hex(i)[2:].upper().rjust(width),
              bin(i)[2:].rjust(width))
print_formatted(5)

# ============================================
# Alphabet Rangoli
# ============================================
print("\n=== Alphabet Rangoli ===")
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    rows = []
    for i in range(size):
        letters = '-'.join(alpha[i:size])
        row = letters[::-1] + letters[1:]
        rows.append(row.center(4*size-3, '-'))
    pattern = rows[::-1] + rows[1:]
    print('\n'.join(pattern))
print_rangoli(3)

# ============================================
# Capitalize
# ============================================
print("\n=== Capitalize ===")
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
print(solve("hello world"))

# ============================================
# The Minion Game
# ============================================
print("\n=== The Minion Game ===")
def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin += (n - i)
        else:
            stuart += (n - i)
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
minion_game("BANANA")

# ============================================
# Merge the Tools!
# ============================================
print("\n=== Merge the Tools! ===")
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        seen = []
        for c in part:
            if c not in seen:
                seen.append(c)
        print(''.join(seen))
merge_the_tools("AABCAAADA", 3)
