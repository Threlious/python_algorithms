import hashlib

string = 'abс'

sum_substring = set()

for i in range(len(string)):  # в цикле постепенно идем по строке слева и сужаем её справа
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) - 1} различных подстрок в строке {string}')  # -1 чтобы не учитвать строку целиком
