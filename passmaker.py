import random

passs=[]

print("\n Script create passwords (digit) without duplucated\n")
print("          L  A  Y  A  N\n\n")
print("            &&&   &&& ")
print("           &&&&& &&&&&")
print("            &&&&&&&&&")
print("             &&&&&&&")
print("               &&&")
print("                &\n\n\n\n")


def j(y,z):
    for i in range(y):
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        pas = ''.join([random.choice(numbers) for i in range(z)])
        if pas not in passs:
            passs.append(str(pas))
            print(str(pas))
        else:
            continue

while True:
    x = int(input("how many character you want?: "))
    p = int(input("how many pass you want?: "))
    j(p,x)