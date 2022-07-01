def ch(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)

def swap_case(s):
    
    return''.join(map(ch,s))
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)