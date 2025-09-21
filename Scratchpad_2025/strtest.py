if __name__ == '__main__':
    s = input()
    
    #print(s.isalnum())
    
    for x in s:
        result = 'False'
        if x.isalnum():
            result ='True'
            break
    print(result)

    for x in s:
        result = 'False'
        if x.isalpha():
            result ='True'
            break
    print(result)
        
    for x in s:
        result = 'False'
        if x.isdigit():
            result ='True'
            break
    print(result)
    
    for x in s:
        result = 'False'
        if x.islower():
            result ='True'
            break

    print(result)
    for x in s:
        result = 'False'
        if x.isupper():
            result ='True'
            break

    print(result)   
