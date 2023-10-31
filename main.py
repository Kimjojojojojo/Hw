import numpy as np
import Huffman as Huffman
length = 1000
p_A = 1/4 # 1이 나올 확률
q_A = 1 - p_A
# 전체 4비트 이진 숫자 리스트 생성
binary_numbers = [format(i, '04b') for i in range(16)]

# 각 숫자에 대한 확률 계산 및 딕셔너리에 추가
probabilities = {}
for binary_number in binary_numbers:
    # 확률을 계산하고 딕셔너리에 추가
    if binary_number.count('1') == 0:
        probabilities[binary_number] = (q_A ** 4)
    if binary_number.count('1') == 1:
        probabilities[binary_number] = (p_A)*(q_A**3)
    if binary_number.count('1') == 2:
        probabilities[binary_number] = ((p_A)**2)*((q_A)**2)
    if binary_number.count('1') == 3:
        probabilities[binary_number] = ((p_A)**3)*((q_A)**1)
    if binary_number.count('1') == 4:
        probabilities[binary_number] = ((p_A) ** 4)

# 결과 출력
print(probabilities)

array_A = np.random.choice([0, 1], size=length, p=[1-p_A, p_A])
chunked_A = np.array([array_A[i:i+4] for i in range(0, len(array_A), 4)])


#Huffman 트리 및 코드 테이블 생성
huffman_tree = Huffman.build_huffman_tree(probabilities)
huffman_codes = Huffman.build_huffman_codes(huffman_tree)
Entropy = Huffman.cal_Entropy((probabilities))
avg = Huffman.avg_bitpersym(huffman_codes,probabilities)

# 결과 출력
for symbol, code in huffman_codes.items():
    print(f"Symbol: {symbol}, Huffman Code: {code}")

print('Entropy of A=',Entropy)
print('compression ratio=',avg)