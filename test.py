from servicio import CatalogoPeliculas
from dominio import Pelicula
import os

menu = True
while menu:
    print('CATALOGO PELICULAS'.center(40,'-'))
    print('1) Agregar')
    print('2) Listar')
    print('3) Eliminar archivo')
    print('4) Salir')
    op = input('Ingresar opcion: ')
    print()
    
    catalogo = CatalogoPeliculas()
    
    if op == '1':
        nombre = input('Ingrese nombre de la pelcula: ')
        pelicula = Pelicula(nombre)
        try:
            catalogo.agregar_pelicula(pelicula)
        except Exception as e:
            print('Error al ingresar titulo --> {e}')
        else:
            print('Titulo agregado exitosamente')
        finally:
            print('*'.center(40,'*'))
        
    elif op == '2':
        print('Listado de peliculas:\n')
        try:
            catalogo.listar_peliculas()
        except Exception as e:
            print(f'Error --> {e}')
        finally:
            print('*'.center(40,'*'))
            
    elif op == '3':
        print('Eliminando Catalogo...')
        try:
            catalogo.eliminar()
        except Exception as e:
            print('Error al eliminar catalogo --> {e}')
        else:
            print('Catalogo eliminado')
        finally:
            print('Proceso finalizado')
            print('*'.center(40,'*'))

    elif op == '4':
        menu = False

    else:
        print('Opcion incorrecta...')




