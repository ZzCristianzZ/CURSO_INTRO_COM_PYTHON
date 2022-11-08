def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

nombre_completo('David','Lopez')
nombre_completo('David', 'Lopez', inverso=True)
nombre_completo(apellido='Lopez', nombre='David')


