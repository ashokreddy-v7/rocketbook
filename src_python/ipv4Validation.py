from collections import defaultdict

def validateIpv4(ipv4):

    if ipv4==None or len(ipv4.strip())==0:
        return False
    
    splitLt=ipv4.split(":")

    if len(splitLt)!=4:
        return False
    try:
        for i in splitLt:
            if not i.isdigit():
                return False
            elif int(i)<0 or int(i)>255 or str(int(i))!=i:
                return False
    except Exception as e:
        return False
    return True

print(validateIpv4('1+1:2:3:255'))
print(validateIpv4('-1:2:3:255'))
print(validateIpv4('192:2:3:255'))
print(validateIpv4('001:2:3:255'))
print(validateIpv4('100:2:3:255'))
print(validateIpv4('1abd:2:3:def'))
print(validateIpv4('-1'))
print(validateIpv4('+1'))
print(validateIpv4('100:2:3:'))
print(validateIpv4('100:2:3'))








