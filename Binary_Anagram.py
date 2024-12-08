def are_binary_anagrams(num1, num2):
    binary1 = bin(num1)[2:]
    binary2 = bin(num2)[2:]
    
    return sorted(binary1) == sorted(binary2)