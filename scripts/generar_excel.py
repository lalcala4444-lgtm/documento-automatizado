#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Excel Mejorado
Procesa datos y agrega calculos automaticos
"""

import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

def generar_excel():
      print("=" * 50)
      print("Generador Excel Mejorado")
      print("=" * 50)

    archivo_entrada = 'datos/productos.xlsx'
    archivo_salida = 'output/productos_procesados.xlsx'

    if not os.path.exists(archivo_entrada):
              print(f"Error: No se encontro {archivo_entrada}")
              return

    print(f"\nLeyendo {archivo_entrada}...")
    datos = pd.read_excel(archivo_entrada)

    # Agrega columnas calculadas
    if 'Precio' in datos.columns:
              datos['Precio_IVA'] = datos['Precio'] * 1.21
              datos['Descuento_10'] = datos['Precio'] * 0.90

    os.makedirs('output', exist_ok=True)
    print(f"Guardando en {archivo_salida}...")
    datos.to_excel(archivo_salida, index=False)

    # Formato
    wb = load_workbook(archivo_salida)
    ws = wb.active

    # Encabezados
    fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    font = Font(bold=True, color="FFFFFF")

    for cell in ws[1]:
              cell.fill = fill
              cell.font = font
              cell.alignment = Alignment(horizontal="center")

    wb.save(archivo_salida)
    print(f"\n✓ Archivo guardado: {archivo_salida}")
    print(f"Se agregaron columnas calculadas")
    print("Listo!\n")

if __name__ == '__main__':
      generar_excel()
  
