# 🚀 Instrucciones Rápidas - Genera Tu Catálogo en 3 Pasos

## Resumen
Este proyecto crea catálogos automáticos en **3 formatos diferentes** desde tu archivo Excel:
- 📄 **PDF Profesional** - Para imprimir o enviar
- - 📋 **Excel Formateado** - Para compartir con clientes
  - - 🖥️ **HTML Interactivo** - Para publicar en web o email
   
    - ---

    ## Paso 1: Preparar Tu Archivo Excel

    ### Requisitos:
    Tu archivo Excel debe tener EXACTAMENTE estas columnas:

    | Column | Ejemplo |
    |--------|----------|
    | **Item** | 123625, 179904, 191554 |
    | **Pack** | 1, 2, 3 |
    | **Size** | EMPTY, #VAR, 200CT |
    | **Descripción** | BUTTER YOGURT, TURKEY BREAST, KRAFT BAG |

    ### Acción:
    1. Abre tu archivo Excel con tus productos
    2. 2. Asegúrate de tener exactamente esas 4 columnas
       3. 3. Guarda el archivo como **`productos.xlsx`**
          4. 4. Coloca el archivo en la carpeta **`datos/`** del proyecto
            
             5. ---
            
             6. ## Paso 2: Instalar Dependencias (Una Sola Vez)
            
             7. 1. Abre **PowerShell** en la carpeta del proyecto
                2.    - Haz click derecho en la carpeta → "Open PowerShell here"
                  
                      -    2. Ejecuta este comando:
                           3.    ```
                                    pip install -r requirements.txt
                                    ```

                                 3. Espera a que termine (2-3 minutos)
                             
                                 4. ---
                             
                                 5. ## Paso 3: Genera Tu Catálogo
                             
                                 6. ### Opción A: Catálogo PDF
                                 7. En PowerShell, escribe:
                                 8. ```
                                    python scripts/generar_catalogos.py
                                    ```

                                    Crea: `output/Catalogo_Productos_DD_MM_YYYY.pdf`

                                    ### Opción B: Catálogo Excel
                                    En PowerShell, escribe:
                                    ```
                                    python scripts/generar_excel.py
                                    ```

                                    Crea: `output/Catalogo_Productos_DD_MM_YYYY.xlsx`

                                    ### Opción C: Catálogo HTML (Con Búsqueda)
                                    En PowerShell, escribe:
                                    ```
                                    python scripts/generar_word_avanzado.py
                                    ```

                                    Crea: `output/Catalogo_Productos.html` - «BreAbre en navegador o comparte por email!

                                    ---

                                    ## ✅ ¡Listo!

                                    Tus archivos están en la carpeta `output/`:
                                    - Puedes descargarlos
                                    - - Compartirlos con clientes
                                      - - Subirlos a tu sitio web
                                        - - Imprimirlos (PDF)
                                         
                                          - ---

                                          ## 🔠 Reutilizar Con Nuevos Productos

                                          Para generar nuevos catálogos:
                                          1. Reemplaza `datos/productos.xlsx` con tu nuevo archivo
                                          2. 2. Ejecuta el mismo comando
                                             3. 3. ¡Listo! Tu nuevo catálogo se genera en segundos
                                               
                                                4. ---
                                               
                                                5. ## 🚧 Troubleshooting
                                               
                                                6. **Problema:** "No se encuentra productos.xlsx"
                                                7. - **Solución:** Verifica que tu archivo se llama exactamente `productos.xlsx` y está en la carpeta `datos/`
                                                  
                                                   - **Problema:** "Columnas faltantes"
                                                   - - **Solución:** Asegúrate de que tu Excel tiene exactamente estas 4 columnas: Item, Pack, Size, Descripción
                                                    
                                                     - **Problema:** "ModuleNotFoundError"
                                                     - - **Solución:** Ejecuta `pip install -r requirements.txt` nuevamente
                                                      
                                                       - ---

                                                       ## 📚 Para Más Detalles
                                                       Ver `GUIA_COMPLETA.md`
