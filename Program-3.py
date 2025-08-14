def patterned_series(n):
    result = []
    if n % 2 == 0:
        limit = n - 1
    else:
        limit = n
    i = 1
    while i <= limit * 2 - 1:  
        result.append(i)
        i += 2 
    return result
print("Output:", patterned_series(6)) 
