def resolve_equation(Ax, Ay, Bx, By, targetx, targety):
    det = (Ax * By) - (Ay * Bx)
    deta = (targetx * By) - (targety * Ay)
    detb = (targety * Ax) - (targetx * Bx)

    #print('deter:',det,' deta: ',deta,' detb: ',detb)

    if det != 0:
        a = deta // det
        b = detb // det
        if a>=0 and b>=0:
            cost = 3 * a + b
            print(a, b)
        else:
            cost = 0
    else:
        cost = 0
    return cost

print(resolve_equation(94, 34, 22, 67, 8400, 5400))