class Node:
    def __init__(self, symbol, prob):
        self.symbol = symbol
        self.prob = prob
        self.left = None
        self.right = None

def huffman_decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if current_node.symbol is not None:
            decoded_data += current_node.symbol
            current_node = huffman_tree

    return decoded_data



# Huffman 코드 생성 (예시)
huffman_codes = {'A': '00', 'B': '01'}

# Huffman 코드를 이진 문자열로 변환 (예시)
encoded_data = "000100"

# Huffman 디코딩 수행
