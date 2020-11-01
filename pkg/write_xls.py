from openpyxl import Workbook
import os, sys
from pathlib import Path
fileDir = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(fileDir)


def print_xls(vvt_check, tom_check, todo_check):
    str_xlsfile=os.path.join(fileDir, 'compare_result.xlsx')
    file_xls=Path(str_xlsfile)
    if file_xls.is_file():
        os.remove(str_xlsfile)
    wb=Workbook()
    #Sheet VVT
    sheet = wb.create_sheet('VVT', 0)
    headerdata_vvt=('Bezeichnung', 'Löschfrist', 'Risiko für Betroffenen',\
        'Beschreibung des Vorgangs und Zweck der Verarbeitung', 'Rechtsgrundlagen',\
        'Rechtliche Würdigung')
    sheet.append(headerdata_vvt)
    for a, vvt_entry in enumerate(vvt_check):
        sheet.cell(row=a+2, column=1, value=vvt_entry['Bezeichnung'])
        if 'Löschfrist' in vvt_entry:
            sheet.cell(row=a+2, column=2, value=vvt_entry['Löschfrist'])
        if 'Risiko für Betroffenen' in vvt_entry:
            sheet.cell(row=a+2, column=3, value=vvt_entry['Risiko für Betroffenen'])
        if 'Beschreibung des Vorgangs und Zweck der Verarbeitung' in vvt_entry:
            sheet.cell(row=a+2, column=4, value=vvt_entry['Beschreibung des Vorgangs und Zweck der Verarbeitung'])
        if 'Rechtsgrundlagen' in vvt_entry:
            sheet.cell(row=a+2, column=5, value=vvt_entry['Rechtsgrundlagen'])
        if 'Rechtliche Würdigung' in vvt_entry:
            sheet.cell(row=a+2, column=6, value=vvt_entry['Rechtliche Würdigung'])
    freezy=sheet['Y2']
    sheet.freeze_panes=freezy


    #Sheet TOM
    sheet = wb.create_sheet('TOM', 1)
    headerdata_tom=('Kategorie der allg. TOM', 'Beschreibung')
    sheet.append(headerdata_tom)
    freezy=sheet['Y2']
    sheet.freeze_panes=freezy


    #Sheet ToDo
    sheet = wb.create_sheet('ToDos', 2)
    headerdata_todo=('Verfahren Nr', 'Bezeichnung', 'Beschreibung', 'Status')
    sheet.append(headerdata_todo)
    freezy=sheet['Y2']
    sheet.freeze_panes=freezy
    #sheet.auto_filter.ref = "A1:Y1"
    wb.save(str_xlsfile)

def find_column_vvt(vvt_entry):
    pass
