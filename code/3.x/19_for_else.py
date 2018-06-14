def primer(n):
    for i in range(2, n):
        for j in range(2, n):
            if i % j == 0:
                print("%d equals %d * %d" % (i, j, i / j))
                break
        else:
            print("%d is a prime number" % i)


primer(100)
