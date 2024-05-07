import re

### operator function

# fungsi tambah (+)
def tambah(x, y):
	return x + y
	
# fungsi kurang (-)
def kurang(x, y):
	return x - y
	
# fungsi kali (*)
def kali(x, y):
	return x * y
	
# fungsi bagi (/)
def bagi(x, y):
	return x / y

#intro

print("""
=================================================================

title : simple python one-line calculator
by    : gilanggp

ex : [    try : 12+3    ]        //empty will return error 
     [        = 15      ]        //still on perfection

==================================================================
""")

pemilahan = 0
while True:
    val = input("try : ")
    try:
        val = str(val)
    except:
        print ("gajelas !!!")
    else:
        break
		
pemilahan = 0
### penyaringan input 
split = re.compile("([0.0-9.0]+)([-,+,*,/]+)([0.0-9.0]+)")
res = split.match(val).groups()

n1 = float(res[0])
op = res[1]
n2 = float(res[2])

'''
print ("")
print (val)
print ("")
print (res)
print ("")
print (n1)
print ("")
print (n2)
print ("")
print (op)
'''

try:
    op = str(op)
finally:
    if op == '+':
        print("    = ", tambah(n1,n2))
    elif op == '*':
        print("    = ", kali(n1,n2))
    elif op == '/':
        print("    = ", bagi(n1,n2))
    elif op == '-':
        print("    = ", kurang(n1,n2))
    else:
        print("")
