s = 'K1KA5CB7'
number = 0
counter = defaultdict(int)
for char in s:
    if char.isnumeric():
        number += int(char)
    else:
        counter[char] += 1
answer = ''
for ascii_code in range(65, 90):
    char = chr(ascii_code)
    answer += char * counter[char]
print(answer + str(number))