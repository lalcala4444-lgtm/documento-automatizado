#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Catálogo PDF Profesional
Lee datos de Excel y crea un PDF formateado y profesional
"""

import os
import pandas as pd
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime

def generar_catalogo_pdf(archivo_entrada='datos/productos.xlsx'):
      """
          Genera un catálogo PDF profesional desde un archivo Excel.
              Columnas esperadas: Item, Pack, Size, Descripción
                  """

    # Verificar que el archivo existe
      if not os.path.exists(archivo_entrada):
                print(f"Error: No se encuentra {archivo_entrada}")
                print("Asegúrate de:")
                print("1. Crear carpeta 'datos/' en la raíz del proyecto")
                print("2. Colocar tu archivo Excel como 'productos.xlsx' en esa carpeta")
                return

      # Leer datos
      print("Leyendo datos...")
      datos = pd.read_excel(archivo_entrada)

    # Verificar columnas requeridas
      columnas_requeridas = ['Item', 'Pack', 'Size', 'Descripción']
      columnas_faltantes = [col for col in columnas_requeridas if col not in datos.columns]

    if columnas_faltantes:
              print(f"Error: Columnas faltantes: {columnas_faltantes}")
              print(f"Columnas encontradas: {list(datos.columns)}")
              return

    # Crear carpeta output si no existe
    os.makedirs('output', exist_ok=True)

    # Configurar documento PDF
    fecha = datetime.now().strftime("%d/%m/%Y")
    nombre_pdf = f"output/Catalogo_Productos_{fecha.replace('/', '_')}.pdf"

    doc = SimpleDocTemplate(
              nombre_pdf,
              pagesize=letter,
              rightMargin=0.5*inch,
              leftMargin=0.5*inch,
              topMargin=0.75*inch,
              bottomMargin=0.75*inch
    )

    # Estilos
    styles = getSampleStyleSheet()
    titulo_style = ParagraphStyle(
              'Titulo',
              parent=styles['Heading1'],
              fontSize=24,
              textColor=colors.HexColor('#1f4788'),
              spaceAfter=12,
              alignment=TA_CENTER,
              fontName='Helvetica-Bold'
    )

    encabezado_style = ParagraphStyle(
              'Encabezado',
              parent=styles['Normal'],
              fontSize=10,
              textColor=colors.white,
              alignment=TA_CENTER,
              fontName='Helvetica-Bold'
    )

    # Contenido del documento
    contenido = []

    # Título
    contenido.append(Paragraph("CATÁLOGO DE PRODUCTOS", titulo_style))
    contenido.append(Paragraph(f"Actualizado: {fecha}", styles['Normal']))
    contenido.append(Spacer(1, 0.3*inch))

    # Preparar datos para tabla
    datos_tabla = [[
              Paragraph("Item", encabezado_style),
              Paragraph("Pack", encabezado_style),
              Paragraph("Size", encabezado_style),
              Paragraph("Descripción", encabezado_style)
    ]]

    # Agregar datos
    for idx, row in datos.iterrows():
              datos_tabla.append([
                            str(row.get('Item', 'N/A')),
                            str(row.get('Pack', 'N/A')),
                            str(row.get('Size', 'N/A')),
                            str(row.get('Descripción', 'N/A'))[:100]  # Limitar descripción a 100 caracteres
              ])

    # Crear tabla
    tabla = Table(datos_tabla, colWidths=[1.2*inch, 0.8*inch, 0.8*inch, 3*inch])

    # Estilo de tabla
    tabla.setStyle(TableStyle([
              ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
              ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
              ('FONTSIZE', (0, 0), (-1, 0), 10),
              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
              ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
              ('GRID', (0, 0), (-1, -1), 1, colors.black),
              ('FONTSIZE', (0, 1), (-1, -1), 8),
              ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
    ]))

    contenido.append(tabla)

    # Construir PDF
    print("Generando PDF...")
    doc.build(contenido)

    print(f"\n✅ ¡Catálogo PDF generado exitosamente!")
    print(f"📄 Archivo: {nombre_pdf}")
    print(f"📊 Productos incluidos: {len(datos)}")
    print(f"\nPuedes encontrar el archivo en la carpeta 'output/'")

if __name__ == '__main__':
      generar_catalogo_pdf()
