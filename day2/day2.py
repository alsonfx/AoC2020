passwords = open("passwords.txt", 'r')

valid1, valid2 = 0, 0
for line in passwords:
    limits, letter, password = line.split(' ')
    low, high = map(int, limits.split('-'))
    letter = letter[0]
    password = password.rstrip()

    valid1 += (low <= password.count(letter) <= high)

    valid2 += (password[low - 1] == letter) ^ (password[high - 1] == letter)

passwords.close()
print(f"Part 1 Valid Passwords: {valid1}")
print(f"Part 2 Valid Passwords: {valid2}")
