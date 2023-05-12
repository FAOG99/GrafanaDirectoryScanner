# PoC para CVE-2021-43798

Este script de Python es una prueba de concepto (PoC) para explotar la vulnerabilidad CVE-2021-43798 en Grafana.

## Pre-requisitos

- Python 3
- Un sistema con Grafana que sea vulnerable a CVE-2021-43798

## Uso

Para ejecutar este script, primero debes clonar el repositorio y moverte al directorio del proyecto:

```bash
git clone <URL del repositorio>
cd <directorio del proyecto>
```

Luego puedes ejecutar el script utilizando Python 3. Los argumentos necesarios son `-d` para especificar el dominio o la IP del sitio,\n `-p` para especificar el puerto y `-f` para seleccionar el archivo que quieres buscar. Aquí tienes un ejemplo:

```bash
python3 script.py -d dominio.com -p 80 -f 1
```

Los archivos disponibles para buscar son los siguientes:

1 - /etc/passwd\n
2 - /etc/shadow\n
3 - /etc/ssh/sshd_config\n
4 - /var/log/auth.log\n
5 - /var/www\n
  

Por ejemplo, si quieres buscar el archivo `/etc/passwd`, debes usar `-f 1`.

Si el script encuentra el archivo y puede leerlo, imprimirá el contenido del archivo. Si no puede encontrar el archivo, imprimirá un mensaje de error.

