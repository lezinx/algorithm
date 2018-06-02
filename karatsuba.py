def toEven(x):
    if x % 2 == 0:
        return x;
    else:
        return x + 1;


def karatsuba(x, y):
    """The Karatsuba multiplication algorithm."""
    rozryad_X = int(len(x)/2);
    rozryad_Y = int(len(y)/2);
    if len(str(x)) and len(str(y)) == 1:
        return int(x) * int(y);
    a = int(x[:rozryad_X]);
    c = int(y[:rozryad_Y]);
    b = int(x[rozryad_X:]);
    d = int(y[rozryad_Y:]);
    ac = a*c;
    bd = b*d;
    AplusB = str(a + b);
    CplusD = str(c + d);
    if len(AplusB) != len(CplusD):
        padding = max(toEven(len(str(a + b))), toEven(len(str(c + d))));
        AplusB = str(a+b).zfill(padding);
        CplusD = str(c+d).zfill(padding);
    return pow(10,rozryad_X*2)*ac+pow(10,rozryad_X)*(karatsuba(AplusB,CplusD)-ac-bd)+bd;



def main():
    x = input("x = ");
    y = input("y = ");
    padding = max(toEven(len(str(x))), toEven(len(str(y))));
    print("x*y = ",karatsuba(x.zfill(padding),y.zfill(padding)));
    main();



if __name__ == "__main__":
    main();
