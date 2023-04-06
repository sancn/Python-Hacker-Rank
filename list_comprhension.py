if __name__ == '__main__':
    x = int(input("Enter the first num:"))
    y = int(input("Enter the second num:"))
    z = int(input("Enter the third num:"))
    n = int(input("Enter num:"))
    x1=[p for p in range(x+1)]
    y1=[q for q in range(y+1)]
    z1=[r for r in range(z+1)]

    perm=[[i,j,k] for i in x1 for j in y1 for k in z1]
    req=[l for l in perm if sum(l)!=n]
    print(req)