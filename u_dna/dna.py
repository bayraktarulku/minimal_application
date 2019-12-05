def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def text_to_DNA(text):
    out = ''
    for char in text:
        bits = text_to_bits(char)
        pairs = map(''.join, zip(*[iter(bits)] * 2))
        res = ''
        for b in pairs:
            if b == '00':
                res += 'A'
            elif b == '01':
                res += 'C'
            elif b == '10':
                res += 'G'
            elif b == '11':
                res += 'T'
        out += res
    return (out)


def DNA_to_text(dna):
    abytes = map(''.join, zip(*[iter(dna)] * 4))
    bout = []
    bytelen = 0
    res = ''
    bcount = 0
    for a in abytes:
        for b in a:
            if b == 'A':
                res += '00'
            elif b == 'C':
                res += '01'
            elif b == 'G':
                res += '10'
            elif b == 'T':
                res += '11'
        bcount += 1
        if res[0] == '0':
            bytelen = 1
        elif res[0:3] == '110':
            bytelen = 2
        elif res[0:4] == '1110':
            bytelen = 3
        elif res[0:6] == '11110':
            bytelen = 4

        if bcount == bytelen:
            bout.append(res)
            res = ''
            bcount = 0
        else:
            pass
    out = ''
    for chb in bout:
        ch = text_from_bits(chb)
        out += ch
    return(out)

if __name__ == '__main__':
    text = input('Enter text (Please): ')
    dna_text = text_to_DNA(text)
    print(DNA_to_text(dna_text))
    print('I\'m the DNA of your sentence.')
    print(text_to_DNA(text))
