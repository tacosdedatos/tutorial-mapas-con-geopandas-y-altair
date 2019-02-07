## Funciones útiles para el proyecto en mano

def arbol(directorio):
    print(f'+ {directorio}')
    for ruta in sorted(directorio.rglob('*')):
        profundidad = len(ruta.relative_to(directorio).parts)
        espacio = '    ' * profundidad
        print(f'{espacio}+ {ruta.name}')