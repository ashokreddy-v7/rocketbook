class BlackBoard:
    def add(self, a, b):
        return a+b

    def factorial(self, num):
        if num < 2:
            return 1
        else:
            return num * self.factorial(num-1)

    def intreverse(self, num):
        if num >= 2**31-1 or num <= -2**31:
            return 0
        else:
            numstr = str(num)
            if num >= 0:
                revstr = numstr[::-1]
            else:
                temp = numstr[1:]
                temp2 = temp[::-1]
                revstr = "-"+temp2
            if int(revstr) >= 2**16-1 or int(revstr) <= -2**16:
                return 0
            else:
                return int(revstr)

    def intpalindrome(self, num):
        if num <= 0:
            return False
        else:
            numstr = str(num)
            l = len(numstr)
            if l % 2 == 0:
                if numstr[:int(l/2)][::-1] == numstr[int(l/2):]:
                    return True
            else:
                if numstr[:int(l/2)][::-1] == numstr[int(l/2)+1:]:
                    return True
            return False

    def romantoint(self, input):
        if not input:
            return -2
        input = input.upper()
        rdict = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}
        if input in rdict:
            return rdict[input]
        for i in input:
            if i not in rdict:
                return -1
        out = 0
        temp = 0
        for i in range(len(input)):

            if i == len(input)-1:
                out = out+rdict[input[i]]
                break

            if rdict[input[i]] >= rdict[input[i+1]]:
                temp = rdict[input[i]]
                out = out+temp
            else:
                temp = rdict[input[i]]
                out = out-temp
        return out

    def listoperations(self, lt, opt):
        if "".join(map(str, lt)).isalnum():
            return -1
        else:
            if str(opt).upper() == 'MAX':
                return (max(lt))
            if str(opt).upper() == 'MIN':
                return (min(lt))
        return 0

    def longestPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        minStr = strs[0]
        maxStr = strs[-1]
        prefix = ""
        for i in range(len(minStr)):
            if minStr[i] != maxStr[i]:
                break
            else:
                prefix = prefix+minStr[i]
        return prefix

    def isValidParan(self, strs):
        if len(strs) == 0:
            return False
        if not strs:
            return False
        if len(strs) % 2 != 0:
            return False
        stack = []
        pdict = {"(": ")", "[": "]", "{": "}"}
        for paran in strs:
            if paran in pdict:
                stack.append(paran)
            else:
                if len(stack) == 0:
                    return False
                if paran != pdict[stack.pop()]:
                    return False
        return len(stack) == 0

    def removeDups(self,srtLt):
        for i in range(len(srtLt)-1,0,-1):
            if srtLt[i]==srtLt[i-1]:
                del srtLt[i]
        return len(srtLt)
    
    def removeElement(self,lt,val):
        i=0
        while i<len(lt):
            if lt[i]==val:
                lt.remove(val)
            else:
                i=i+1
        return len(lt)
    def findNeedle(self,haystack,needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

    def findPosition(self,strLt,target):
        if len(strLt)==0 or target<strLt[0]:
            return 0
        if target>strLt[len(strLt)-1]:
            return len(strLt)
        low=0
        high=len(strLt)
        while low<high:
            mid=low+high//2
            if target>strLt[mid]:
                low=mid+1
            else:
                high=mid
        return low
        
    def countAndSay(self):
        return 0

obj = BlackBoard()
# print(obj.add(2,5))
# print(obj.factorial(1))
# print(obj.intreverse(-12345))
# print(obj.intpalindrome(11))
# print(obj.romantoint("LVIII"))
# print(obj.listoperations(['a','b','c','d'],'max'))
# print(obj.longestPrefix(["testomg","test123","testm","rsm"]))
#print(obj.isValidParan("{[]}"))
#print(obj.removeElement([0,1,2,2,3,0,4,2],2))
#print(obj.findNeedle("hello",'o'))
print(obj.findPosition([1,3,5,6], 10))

