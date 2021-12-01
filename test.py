def test(x):
    if x > 0:
        print('x is positive')
    else:
        print('x is negative')


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print(test(j))