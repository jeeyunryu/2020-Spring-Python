def fibo(n):
    if n == 2:
        return[1, 1]
    else:
        list = fibo(n-1)
        vn = list[-1] + list[-2]
        list.append(vn)
        return list

print(fibo(10))
