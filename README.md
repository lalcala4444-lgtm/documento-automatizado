# Generador Automatico de Documentos

Herramienta para crear automaticamente documentos Word, Excel y catalogos digitales a partir de datos.

## Caracteristicas

- Generar documentos Word (.docx)
- Generar hojas Excel (.xlsx)
- Procesar datos masivos (miles de registros)
- Scripts Python faciles de usar
- Personalizable segun tus necesidades

## Estructura del Proyecto

```
documento-automatizado/
-- README.md
-- requirements.txt
-- .gitignore
-- datos/              # Carpeta para archivos Excel
-- templates/          # Plantillas Word
-- scripts/            # Scripts Python
-- ejemplos/           # Ejemplos de salida
```

## Inicio Rapido

### 1. Clonar repositorio

```bash
git clone https://github.com/lalcala4444-lgtm/documento-automatizado.git
cd documento-automatizado
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar scripts

```bash
python scripts/generar_catalogos.py
```

## Dependencias

- python-docx: Para crear documentos Word
- openpyxl: Para trabajar con Excel
- pandas: Para procesar datos
- jinja2: Para plantillas

## Ejemplos de Uso

Ver la carpeta `ejemplos/` para ver casos de uso listos.

## Licencia

MIT License
