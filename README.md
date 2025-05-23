# Taller 3 - Ingeniería de Datos

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/CQuarkH/taller3-datos.git
```

2. Navega a la carpeta del proyecto

```bash
cd taller3-datos
```

3. Crea un entorno virtual dentro de la carpeta del proyecto
```bash
python -m venv .venv
```

4. Activa el entorno virtual
- En Windows:
```bash
.venv\Scripts\activate
```
- En Linux/Mac:
```bash
source .venv/bin/activate
```

5. Instala las dependencias
```bash
pip install -r requirements.txt
```

## Uso
1. Asegurarse de tener los archivos de datos en la carpeta `data/`.

2. Ejectuta la aplicación
```bash
python src/app.py
```

3. Los resultados procesados se guardarán en la carpeta data/processed_data.csv

### Estructura del proyecto
- src/: Código fuente de la aplicación.
- data/: Archivos de datos de entrada y salida.
- notebooks/: Notebooks de Jupyter para análisis exploratorio.
- documentation/: Documentación adicional.
