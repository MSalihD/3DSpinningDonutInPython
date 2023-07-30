from math import *
import sys,time
def floatRange(a,b,c):
    r = []
    i = a
    while i < b:
        r.append(i)
        i += c
    return r
printf = lambda a,*b:sys.stdout.write(a % b)
putchar = lambda a:printf("%c",a)
usleep = lambda a:time.sleep(a / 1000000)
def main():
    A,B = 0.0,0.0
    i,j = 0.0,0.0
    k = 0
    z = [0.0 for u in range(1760)]
    b = ["\x00" for u in range(1760)]
    printf("\x1b[2J")
    while 1:
        b = [" " for u in range(1760)]
        z = [0.0 for u in range(1760)]
        for j in floatRange(0,6.28,0.07):
            for i in floatRange(0,6.28,0.02):
                c = sin(i)
                d = cos(j)
                e = sin(A)
                f = sin(j)
                g = cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = cos(i)
                m = cos(B)
                n = sin(B)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y= int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if 22 > y and y > 0 and x > 0 and 80 > x and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
        printf("\x1b[H")
        for k in range(1761):   
            putchar(b[k] if k % 80 else 10) 
            A += 0.00004
            B += 0.00002
        
        #usleep(30000)
main()
