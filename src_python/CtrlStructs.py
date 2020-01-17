# Declare variables
number1 = 100
string1 = 'ashok'
list1 = ['ashok','ariful','allen','vaseem']
tuple1 = ('ashok',28,'allen', 40)
set1 = {'pear', 'orange', 'banana', 'apple', 'duplicate', 'duplicate'}
dict1 = {'pear':'unknown', 'orange':'orange', 'banana':'yellow', 'apple':'red', 'duplicate':'unknown', 'duplicate':'unknown'}

if (number1*10==1000):
    print('true number')

if(string1[0]=='a'):
    print('string has a in it')

if('ashoka' not in list1):
    print('true list')

if('apple' in set1):
    print('true set')

if(dict1['apple']=='red'):
    print('true dictionary')
    
listnum = [1,2,3,4,5,6,7,8,9]

i = iter(listnum)

for n in i:
    print(n)


