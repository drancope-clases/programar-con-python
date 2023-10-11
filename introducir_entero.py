while True:
    a = input()
    error = 0 #esto significa que al principio no hay ningún error.
    for i in range(len(a)):  # len(a) es la longitud de a.
        if i==0 and a[0] =='-': # Esto solo se hace la primera letra
            continue
        if a[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            continue
        else:
            error = 1
    if error == 1:
        print("Había que introducir un número.")
        print("Volvamos a intentarlo")
    else:
        break
int(a)
