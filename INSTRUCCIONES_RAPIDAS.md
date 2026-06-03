# Instrucciones Rapidas - Ejecuta Todo En 3 Pasos

## Paso 1: Abre Terminal (CMD o PowerShell)

En Windows:
- Click derecho en la carpeta del proyecto
- - Selecciona "Abrir terminal aqui" o "Abrir PowerShell aqui"
 
  - ## Paso 2: Instala Dependencias (UNA SOLA VEZ)
 
  - Escribe esto en la terminal:
  - ```
    pip install -r requirements.txt
    ```

    Espera a que termine (toma 1-2 minutos)

    ## Paso 3: Ejecuta el Script

    Escribe esto:
    ```
    python scripts/generar_catalogos.py
    ```

    ¡LISTO!

    Los catalogos se crean en la carpeta "output/"

    ---

    ## Si Quieres Procesar TU Excel

    1. Coloca tu archivo en: carpeta/datos/
    2. 2. Llamalo: productos.xlsx
       3. 3. Que tenga estas columnas: Nombre | Precio | Descripcion
          4. 4. Ejecuta: python scripts/generar_catalogos.py
            
             5. ---
            
             6. ## Problemas?
            
             7. - Error "python no encontrado": Instala Python desde python.org
                - - Error "requirements": Asegurate de estar en la carpeta correcta
                  - - Error al leer Excel: Verifica que el archivo se llame productos.xlsx
                   
                    - ---

                    ## Archivos Importantes

                    - datos/productos_ejemplo.xlsx -> Excel de ejemplo
                    - - scripts/generar_catalogos.py -> Script principal
                      - - output/ -> Donde se guardan los documentos
                        - 
