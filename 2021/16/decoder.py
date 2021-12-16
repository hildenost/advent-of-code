""" Advent of Code 2021. Day 16: Packet Decoder """
hex_string = "E054831006016008CF01CED7CDB2D495A473336CF7B8C8318021C00FACFD3125B9FA624BD3DBB7968C0179DFDBD196FAE5400974A974B55C24DC580085925D5007E2D49C6579E49252E28600B580272379054AF57A54D65E1586A951D860400434E36080410926624D25458890A006CA251006573D2DFCBF4016919CC0A467302100565CF24B7A9C36B0402840002150CA3E46000042621C108F0200CC5C8551EA47F79FC28401C20042E0EC288D4600F42585F1F88010C8C709235180272B3DCAD95DC005F6671379988A1380372D8FF1127BDC0D834600BC9334EA5880333E7F3C6B2FBE1B98025600A8803F04E2E45700043E34C5F8A72DDC6B7E8E400C01797D02D002052637263CE016CE5E5C8CC9E4B369E7051304F3509627A907C97BCF66008500521395A62553A9CAD312A9CCCEAF63A500A2631CCD8065681D2479371E4A90E024AD69AAEBE20002A84ACA51EE0365B74A6BF4B2CC178153399F3BACC68CF3F50840095A33CBD7EF1393459E2C3004340109596AB6DEBF9A95CACB55B6F5FCD4A24580400A8586009C70C00D44401D8AB11A210002190DE1BC43872C006C45299463005EC0169AFFF6F9273269B89F4F80100507C00A84EB34B5F2772CB122D26016CA88C9BCC8BD4A05CA2CCABF90030534D3226B32D040147F802537B888CD59265C3CC01498A6B7BA7A1A08F005C401C86B10A358803D1FE24419300524F32AD2C6DA009080330DE2941B1006618450822A009C68998C1E0C017C0041A450A554A582D8034797FD73D4396C1848FC0A6F14503004340169D96BE1B11674A4804CD9DC26D006E20008747585D0AC001088550560F9019B0E004080160058798012804E4801232C0437B00F70A005100CFEE007A8010C02553007FC801A5100530C00F4B0027EE004CA64A480287C005E27EEE13DD83447D3009E754E29CDB5CD3C"

bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def parse_hex(hexpacket):
    return "".join(bits[h] for h in hexpacket)

def parse_version_type(binary):
    return int(binary[:3], 2), int(binary[3:6], 2), binary[6:]

def parse_literal(binary):
    number = ""
    while binary[0] == "1":
        number += binary[1:5]
        binary = binary[5:]
    # Last group in subpacket
    number += binary[1:5]
    return int(number, 2), binary[5:]

def get_length(binary):
    l = 11 if binary[0] == "1" else 15
    if l == 11:
        return None, int(binary[1:l+1], 2), binary[l+1:]
    elif l == 15:
        return int(binary[1:l+1], 2), None, binary[l+1:]

def parse_packet(binary, n=None):
    version_sum = 0
    counter = 0
    while binary and not all(b == "0" for b in binary):
        version, t, binary = parse_version_type(binary)
        version_sum += version
        
        if t == 4:
            number, binary = parse_literal(binary)
        else:
            sub_p_len, n_p, binary = get_length(binary)
            subpackets, b = parse_packet(binary[:sub_p_len], n_p)
            if sub_p_len is not None:
                binary = binary[sub_p_len:]
            else:
                binary = b
            version_sum += subpackets
        counter += 1
        if counter == n and n is not None:
            return version_sum, binary
    return version_sum, binary

print("Part 1:\t", parse_packet(parse_hex(hex_string))[0])

import math
op = {
        0: lambda x: sum(x),
        1: lambda x: math.prod(x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1]),
 }
# Part 2
def parse(binary):
    version, t, binary = parse_version_type(binary)

    if t == 4:
        number, binary = parse_literal(binary)
        return number, binary

    sub_p_len, n_p, binary = get_length(binary)
    if n_p is None:
        values = []
        temp_bin = binary[:sub_p_len]
        while temp_bin:
            value, temp_bin = parse(temp_bin)
            values.append(value)
        binary = binary[sub_p_len:]
    else:
        values = []
        for n in range(n_p):
            value, binary = parse(binary)
            values.append(value)
    value = op[t](values)
    return value, binary

print("Part 2:\t", parse(parse_hex(hex_string))[0])
