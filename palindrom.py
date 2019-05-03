##sevl02
def Palindrom(string):
    for i in range(1, len(string)):
        if string[i].lower() == string[-(i+1)].lower():
            return True
        else:
            return False


