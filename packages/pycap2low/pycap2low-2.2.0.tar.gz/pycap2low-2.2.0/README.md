# pycap2low
Aplicación para convertir los nombres de archivos y directorios a minúsculas.

# Requisitos
Intérprete de python3

# Instalación
> pip3 install pycap2low

# Uso
La aplicación recibe como primer parámetro la ruta del directorio a renombrar.
> pycap2low /ruta/directorio/renombrar

## Argumentos
> -r --recursive Indicador para renombrar todos los subdirectorios.
--str-camel-case Cadena a usar en caso de notacion camelCase.
--excepts Ruta a fichero contenedor de rutas de excepción.
    Las rutas dentro del fichero admiten atributos. Por el momento el atributo reconocido es -r.
    El formato es el siguiente:
    -r /ruta/directorio/exceptuar/recursivamente
    - /ruta/directorio/exceptuar

# Ayuda
> pycap2low -h | --help

# Créditos
Idea original y desarrollo: 
Alexis Torres Valdes (alexisdevsol@gmail.com).

