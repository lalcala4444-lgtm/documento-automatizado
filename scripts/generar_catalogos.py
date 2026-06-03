#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd
from docx import Document

archivo_datos = 'datos/productos.xlsx'
if not os.path.exists(archivo_datos):
              print(f"Error: No encontre {archivo_datos}")
              exit()

print("Leyendo datos...")
datos = pd.read_excel(archivo_datos)
os.makedirs('output', exist_ok=True)

print(f"Creando {len(datos)} documentos...")
for idx, row in datos.iterrows():
              doc = Document()
              doc.add_heading(f"Catalogo #{idx+1}", 0)
              doc.add_paragraph(f"Item: {row.get('Item', 'N/A')}")
              doc.add_paragraph(f"Pack: {row.get('Pack', 'N/A')}")
              doc.add_paragraph(f"Size: {row.get('Size', 'N/A')}")
              desc = row.get('Descripcion', row.get('Descripción', 'N/A'))
              doc.add_paragraph(f"Descripcion: {desc}")
              doc.save(f"output/catalogo_{idx+1:04d}.docx")
              if (idx+1) % 100 == 0:
                                print(f"  {idx+1} documentos creados...")

          print(f"Listo! Se crearon {len(datos)} catalogos")
