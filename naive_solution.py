def generate_binary_numbers(n):
    result = []
    for i in range(2 ** n):
        binary = bin(i)[2:].zfill(n)
        result.append(binary)
    invalid = 0
    not_valid = 0    
    for ele in result:
        count = 0
        for i in ele:
            if i == '0':
                count += 1
            else:
                count = 0
        
        if count >= 4:
            invalid += 1
        elif ele[-1] == '0':
            not_valid += 1
        
    pos_ways_att_cls = len(result) - invalid - 1
    pos_mis_cer = pos_ways_att_cls - not_valid -1
    
    # print(result)
    # print(pos_ways_att_cls)
    # print(not_valid)
    # print(pos_mis_cer)
    
    return f"{pos_mis_cer}/{pos_ways_att_cls}"

n = int(input("Enter the value of n: "))
binary_numbers = generate_binary_numbers(n)
print(binary_numbers)
