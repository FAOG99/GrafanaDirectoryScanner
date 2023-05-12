# PoC para CVE-2021-43798

Este script de Python es una prueba de concepto (PoC) para explotar la vulnerabilidad CVE-2021-43798 en Grafana.

## Pre-requisitos

- Python 3
- Un sistema con Grafana que sea vulnerable a CVE-2021-43798
- Docker (solo si deseas levantar el laboratorio de pruebas)

## Uso

Para ejecutar este script, primero debes clonar el repositorio y moverte al directorio del proyecto:

```bash
git clone https://github.com/FAOG99/GrafanaDirectoryScanner.git
cd GrafanaDirectoryScanner
```
## Levantar laboratorio de pruebas
Si deseas levantar un laboratorio vulnerable puedes seguir los siguientes pasos:
```bash
cd CVE-2021-43798
docker-compose up -d
```
Despues de que el servidor levante, puedes navegar a http://localhost:3000 para ingresar a la página de login. Para este exploit no se necesitan credenciales.

## Ejecución del exploit

Luego puedes ejecutar el script utilizando Python 3.

Recuerda ejecutar el exploit desde la ruta correcta (si entraste a la carpeta del laboratorio recuerda regresar a la carpeta raiz)

Los argumentos necesarios son `-d` para especificar el dominio o la IP del sitio,
`-p` para especificar el puerto y `-f` para ingresar la ruta del archivo que deseas buscar (si no usas esta opción correra /etc/passwd por defecto). Aquí dejo un ejemplo

```bash
python3 GrafanaDirectoryScanner -d dominio.com -p 80 -f /etc/passwd
```


Si el script encuentra el archivo y puede leerlo, imprimirá el contenido del archivo. Si no puede encontrar el archivo, imprimirá un mensaje de error.

## Ejemplo
![Screenshot_20230512_105018](https://github.com/FAOG99/GrafanaDirectoryScanner/assets/92898049/74b3588b-28ab-4c23-9cca-e2e2201db49f)



