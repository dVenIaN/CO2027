def count_substring(string, sub_string):
    countfinds = 0
    
    start = 0
    end = len(string)
    
    x = len(sub_string)
    print(x)
    
    while end != start:
        print(start)
        start = string.find(sub_string, start)
        print(start)

        if start != -1 :
            countfinds = countfinds + 1
        else :
            break

        start = start + 1
    
    print('countfinds = ' + str(countfinds))
    return countfinds

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
