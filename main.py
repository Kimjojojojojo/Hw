import numpy as np
import Huffman_encoding as Huffman_e
import Huffman_decoding as Huffman_d

length = 1000
p_A = 1/4 # 1이 나올 확률
q_A = 1 - p_A

# 전체 4비트 이진 숫자 리스트 생성
binary_numbers = [format(i, '04b') for i in range(16)]
array_A = np.random.choice([0, 1], size=length, p=[1-p_A, p_A])
chunked_A = np.array([array_A[i:i+4] for i in range(0, len(array_A), 4)])
string_A = ''.join(map(str, array_A))


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


#Huffman 트리 및 코드 테이블 생성
huffman_tree = Huffman_e.build_huffman_tree(probabilities)
huffman_codes = Huffman_e.build_huffman_codes(huffman_tree)

Entropy = Huffman_e.cal_Entropy((probabilities))
avg = Huffman_e.avg_bitpersym(huffman_codes, probabilities)

###code book##
# for symbol, code in huffman_codes.items():
#     print(f"Symbol: {symbol}, Huffman Code: {code}")

enocoded_Huffman = Huffman_e.huffman_encode(string_A, huffman_codes)

###decoding##
decoded_Huffman = Huffman_d.huffman_decode(enocoded_Huffman, huffman_tree)

###ratio###
comp_ratio = (len(string_A)-len(enocoded_Huffman))/len(string_A) * 100
###results##


print('Entropy of A=',Entropy)
print('compression ratio=',avg)

print("Origin data :","length = ", len(string_A) ,"\n", string_A)
print("Encoded data :","length = ", len(enocoded_Huffman), "\n", enocoded_Huffman)
print("Decoded code :","length = ", len(decoded_Huffman),"\n", decoded_Huffman)

print("Compresstion ratio =",comp_ratio,"%")

if string_A == decoded_Huffman:
    print("Perfect reconstruction")
else :
    print("no perfect reconstruction")

Huffman_e.visualize_huffman_tree(huffman_tree)