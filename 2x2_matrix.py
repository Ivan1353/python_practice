def matrix_mult(a, b):
    c = [[],[]]
    c[0].append(a[0][0]*b[0][0] + a[0][1]*b[1][0])
    c[0].append(a[0][0] * b[0][1] + a[0][1] * b[1][1])
    c[1].append(a[1][0] * b[0][0] + a[1][1] * b[1][0])
    c[1].append(a[1][0] * b[0][1] + a[1][1] * b[1][1])
    return c