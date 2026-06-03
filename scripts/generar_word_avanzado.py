#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Catálogo HTML Digital
"""

import os
import pandas as pd
from datetime import datetime

def generar_catalogo_html(archivo_entrada='datos/productos.xlsx'):
        if not os.path.exists(archivo_entrada):
                    print(f"Error: No se encuentra {archivo_entrada}")
                    return

        datos = pd.read_excel(archivo_entrada)
        columnas_requeridas = ['Item', 'Pack', 'Size', 'Descripción']
        columnas_faltantes = [col for col in columnas_requeridas if col not in datos.columns]

    if columnas_faltantes:
                print(f"Error: Columnas faltantes: {columnas_faltantes}")
                return

    os.makedirs('output', exist_ok=True)
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    nombre_html = f"output/Catalogo_Productos.html"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Catálogo de Productos</title>
                    <style>
                            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                                    body {{ font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
                                            .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); padding: 40px; }}
                                                    h1 {{ color: #1f4788; margin-bottom: 10px; }}
                                                            .info {{ color: #666; margin-bottom: 30px; }}
                                                                    .search {{ margin-bottom: 20px; }}
                                                                            .search input {{ width: 100%; padding: 10px; font-size: 1em; border: 2px solid #ddd; border-radius: 5px; }}
                                                                                    table {{ width: 100%; border-collapse: collapse; }}
                                                                                            th {{ background-color: #1f4788; color: white; padding: 12px; text-align: left; }}
                                                                                                    td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
                                                                                                            tr:nth-child(even) {{ background-color: #f9f9f9; }}
                                                                                                                    tr:hover {{ background-color: #f0f0f0; }}
                                                                                                                            .footer {{ margin-top: 30px; text-align: center; color: #666; border-top: 2px solid #eee; padding-top: 20px; }}
                                                                                                                                </style>
                                                                                                                                </head>
                                                                                                                                <body>
                                                                                                                                    <div class="container">
                                                                                                                                            <h1>📒 Catálogo de Productos</h1>
                                                                                                                                                    <div class="info">Actualizado: {fecha} | Total de productos: {len(datos)}</div>
                                                                                                                                                            <div class="search">
                                                                                                                                                                        <input type="text" id="searchInput" placeholder="Buscar productos...">
                                                                                                                                                                                </div>
                                                                                                                                                                                        <table id="productTable">
                                                                                                                                                                                                    <thead>
                                                                                                                                                                                                                    <tr>
                                                                                                                                                                                                                                        <th>Item</th>
                                                                                                                                                                                                                                                            <th>Pack</th>
                                                                                                                                                                                                                                                                                <th>Size</th>
                                                                                                                                                                                                                                                                                                    <th>Descripción</th>
                                                                                                                                                                                                                                                                                                                    </tr>
                                                                                                                                                                                                                                                                                                                                </thead>
                                                                                                                                                                                                                                                                                                                                            <tbody>
                                                                                                                                                                                                                                                                                                                                            """

    print(f"Procesando {len(datos)} productos...")
    for idx, row in datos.iterrows():
                item = str(row.get('Item', 'N/A'))
                pack = str(row.get('Pack', 'N/A'))
                size = str(row.get('Size', 'N/A'))
                desc = str(row.get('Descripción', 'N/A'))
                html_content += f"<tr><td>{item}</td><td>{pack}</td><td>{size}</td><td>{desc}</td></tr>\n"

    html_content += """
                </tbody>
                        </table>
                                <div class="footer">
                                            <p>Catálogo generado automáticamente - Usa el buscador para filtrar productos</p>
                                                    </div>
                                                        </div>
                                                            <script>
                                                                    document.getElementById('searchInput').addEventListener('keyup', function(e) {
                                                                                const searchTerm = e.target.value.toLowerCase();
                                                                                            const tableRows = document.querySelectorAll('#productTable tbody tr');
                                                                                                        tableRows.forEach(row => {
                                                                                                                        const text = row.textContent.toLowerCase();
                                                                                                                                        row.style.display = text.includes(searchTerm) ? '' : 'none';
                                                                                                                                                    });
                                                                                                                                                            });
                                                                                                                                                                </script>
                                                                                                                                                                </body>
                                                                                                                                                                </html>
                                                                                                                                                                    """

    print("Generando HTML...")
    with open(nombre_html, 'w', encoding='utf-8') as f:
                f.write(html_content)

    print(f"\n✅ ¡Catálogo HTML generado!")
    print(f"📄 Archivo: {nombre_html}")
    print(f"📊 Productos: {len(datos)}")

if __name__ == '__main__':
        generar_catalogo_html()
