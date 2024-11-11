def decode_message(s: str, p: str) -> bool:
    memo = {}
    
    def match(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == len(p):
            return i == len(s)
        
        if i == len(s):
            memo[(i, j)] = p[j] == '*' and match(i, j + 1)
            return memo[(i, j)]
        
        if p[j] == '*':
            memo[(i, j)] = match(i + 1, j) or match(i, j + 1)
        elif p[j] == '?' or p[j] == s[i]:
            memo[(i, j)] = match(i + 1, j + 1)
        else:
            memo[(i, j)] = False
        
        return memo[(i, j)]
    
    return match(0, 0)


print(decode_message("aa", "a"))       
print(decode_message("aa", "*"))       
print(decode_message("cb", "?a"))      
print(decode_message("aa", "a*"))      
