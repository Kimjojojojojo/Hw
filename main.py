import numpy as np
import heapq
from collections import defaultdict

length = 1000
P_A = 1/4 # 1이 나올 확률
# 전체 4비트 이진 숫자 리스트 생성
binary_numbers = [format(i, '04b') for i in range(16)]

# 각 숫자에 대한 확률 계산 및 딕셔너리에 추가
probabilities = {}
for binary_number in binary_numbers:
    # 확률을 계산하고 딕셔너리에 추가 (예시로 0.1로 설정)
    if binary_number.count('1') == 1:
        probabilities[binary_number] = 1 / 4
    else:
        probabilities[binary_number] = 3 / 4

# 결과 출력
print(probabilities)

array_A = np.random.choice([0, 1], size=length, p=[1-P_A, P_A])
chunked_A = np.array([array_A[i:i+4] for i in range(0, len(array_A), 4)])

count_ones = np.count_nonzero(array_A == 1)

# print(array_A)
# print(chunked_A)



# 주어진 확률 분포 (예: 0이 나올 확률이 3/4, 1이 나올 확률이 1/4)
probabilities = {0: 3 / 4, 1: 1 / 4}


# 노드 클래스 정의



# Huffman 트리 및 코드 테이블 생성
# huffman_tree = build_huffman_tree(probabilities)
# huffman_codes = build_huffman_codes(huffman_tree)
#
# # 결과 출력
# for symbol, code in huffman_codes.items():
#     print(f"Symbol: {symbol}, Huffman Code: {code}")