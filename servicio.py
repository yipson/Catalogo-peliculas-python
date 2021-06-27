from dominio import Pelicula
import os # operating system - trae el metodo de eliminar archivos

class CatalogoPeliculas:
    ruta_archivo = 'catalogo.txt'
    
    @classmethod # se usa para accedes a los atributos estaticos
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod # se usa para accedes a los atributos estaticos
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(archivo.read())    
        
    @classmethod # se usa para accedes a los atributos estaticos
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print('Catalogo eliminado')
        

if __name__ == '__main__':
    pelicula = Pelicula('cars')
    catalogo = CatalogoPeliculas()
    
    catalogo.agregar_pelicula(pelicula)
    catalogo.listar_peliculas()
    
    catalogo.eliminar()