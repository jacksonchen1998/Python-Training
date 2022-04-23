"""
C(m,n) = m!/n!(m=n)!

"""

m = int(input("m : "))
n = int(input("n : "))
fm = 1

for num in range(1, m+1):
    fm *= num
fn = 1

for num in range(1, n+1):
    fn *= num

fn_m = 1
for num in range(1, m - n + 1):
    fn_m *= num

print("C(m, n) = %d" % (fm // fn // fn_m) )

"""
Using function to implement

"""
def factor(m):
    num = 1
    for i in range(1, m + 1):
        num *= i
    return num

print("C(m, n) = %d" % (factor(m) // factor(n) // factor(m-n)))
