# Guia Completa - Generador Automatico de Documentos

## Inicio Rapido (3 Pasos)

### 1. Abre Terminal en la carpeta del proyecto

**Windows:**
- Click derecho en la carpeta
- "Abrir terminal aqui" o "Abrir PowerShell aqui"

**Mac/Linux:**
- Abre Terminal
- cd /ruta/a/documento-automatizado

### 2. Instala dependencias (primera vez)

```bash
pip install -r requirements.txt
```

### 3. Ejecuta un script

**Generar catalogos en Word:**
```bash
python scripts/generar_catalogos.py
```

**Procesar Excel:**
```bash
python scripts/generar_excel.py
```

---

## Archivos del Proyecto

### Datos
- `datos/productos_ejemplo.csv` - Archivo de ejemplo con 20 productos
- `datos/productos.xlsx` - Tu archivo a procesar (renombra o usa este nombre)

### Scripts
- `scripts/generar_catalogos.py` - Crea documento Word por cada producto
- `scripts/generar_excel.py` - Procesa Excel y agrega calculos
- `scripts/generar_word_avanzado.py` - Opcion avanzada con mas formatos

### Configuracion
- `requirements.txt` - Librerias necesarias
- `.gitignore` - Archivos ignorados por git
- `README.md` - Documentacion breve

---

## Como Usar Con Tu Archivo

1. **Prepara tu Excel:**
   - Debe tener columnas: `Nombre`, `Precio`, `Descripcion`
      - Guarda como `datos/productos.xlsx`

      2. **Ejecuta:**
         ```bash
            python scripts/generar_catalogos.py
               ```

               3. **Resultados en:** carpeta `output/`

               ---

               ## Formatos Soportados

               - **Excel:** .xlsx, .csv
               - **Salida Word:** .docx (1 por fila del Excel)
               - **Salida Excel:** .xlsx procesado con calculos

               ---

               ## Troubleshooting

               | Problema | Solucion |
               |----------|----------|
               | python no encontrado | Instala Python 3.9+ desde python.org |
               | ModuleNotFoundError | Ejecuta: pip install -r requirements.txt |
               | Archivo no encontrado | Verifica que esten en las carpetas correctas |
               | Excel corrupto | Abre con LibreOffice o Microsoft Excel |

               ---

               ## Ejemplos Practicos

               ### Ejemplo 1: 100 Catalogos
               1. Crea Excel con 100 productos
               2. Ejecuta: python scripts/generar_catalogos.py
               3. Obtendras 100 archivos .docx en output/

               ### Ejemplo 2: Procesar Datos
               1. Coloca tu Excel en datos/productos.xlsx
               2. Ejecuta: python scripts/generar_excel.py
               3. Se genera productos_procesados.xlsx con calculos

               ---

               ## Customizacion

               ### Cambiar Nombre de Carpetas
               Edita en los scripts:
               ```python
               # Cambiar entrada
               archivo = 'mi_carpeta/datos.xlsx'

               # Cambiar salida
               os.makedirs('mi_salida', exist_ok=True)
               ```

               ### Agregar Mas Columnas
               En generar_excel.py, agrega al section "Columnas calculadas":
               ```python
               datos['Nueva_Columna'] = datos['Precio'] * 2
               ```

               ---

               ## Soporte

               - GitHub: https://github.com/lalcala4444-lgtm/documento-automatizado
               - Reporta problemas en Issues

               
