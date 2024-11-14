import os
import urllib.request

dir_download = "../src/rd/dbc/"
os.makedirs(dir_download, exist_ok=True)

ano = "20"
mes = "01"

URL_BASE = "ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/"
URL = f"Dados/RDRJ{ano}{mes}.dbc"
URL = URL_BASE + URL

path_arquivo = os.path.join(dir_download, f"RDRJ{ano}{mes}.dbc")

try:
    response = urllib.request.urlopen(URL, timeout=10)
    urllib.request.urlretrieve(URL, path_arquivo)
except urllib.error.URLError as e:
    print(f"Failed to retrieve the file: {e.reason}")
