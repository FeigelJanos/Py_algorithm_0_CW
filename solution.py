def square_digits(num):

    numArr = [int(x) for x in str(num)]
    sqrArr = []
    
    for num in numArr:
        e = num ** 2
        sqrArr.append(e)
        
        res = int("".join(map(str, sqrArr))) 
      
    return res 
