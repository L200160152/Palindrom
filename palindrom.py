##sevl02
def Palindrom(string):
    a = 0
    a = a+1
    for i in range(a, len(string)):
        if string[i].lower() == string[-(i+1)].lower():
            
            return True
            
        else:
            return False


