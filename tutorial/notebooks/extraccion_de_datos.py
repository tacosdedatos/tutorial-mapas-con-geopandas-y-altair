## Extrae los archivos comprimidos .zip en  ../datos/en_bruto/ a ../datos/interinos/

from pathlib import Path
from zipfile import ZipFile

ruta_datos_en_bruto = Path("../datos/en_bruto/")
ruta_datos_interinos = Path("../datos/interinos/")

for archivo_zip in ruta_datos_en_bruto.glob("*.zip"):
    archivo = ZipFile(archivo_zip)
    print(f"Extrayendo archivo {archivo_zip.name}")
    archivo_interino_con_ruta = (ruta_datos_interinos / archivo_zip.stem)
    archivo.extractall(archivo_interino_con_ruta)
    print(f"Contenido extraído a: {archivo_interino_con_ruta}")