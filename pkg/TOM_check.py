import Levenshtein


def chk_TOM(dict_old, dict_new):
    tom_old=dict_old['Allgemeine TOMs']
    tom_new=dict_new['Allgemeine TOMs']
    lst_cmpr_result=[]
    for x, verfahren_o in enumerate(tom_old):       #1. Verfahren in OLD
        kat_o=verfahren_o['Kategorie der allg. TOM']        
        beschr_o=verfahren_o['Beschreibung']
        for y, verfahren_n in enumerate(tom_new): 
            result_cmpr={}
            if verfahren_n['Kategorie der allg. TOM']==kat_o:
                #Beschreibung
                beschr_n=verfahren_n['Beschreibung']
                dict_compare=vergleiche_bewerte(beschr_o, beschr_n, kat_o, verfahren_n, 'Beschreibung', result_cmpr)
                result_cmpr=dict_compare
                # überprüftes Verfahren wird gelöscht
                tom_new.pop(y) 
            if 'Beschreibung' in result_cmpr:
                lst_cmpr_result.append(result_cmpr)
    # Hinzufügen der neuen Verfahren
    for verfahren_neu in tom_new:
        neueVerf=neue_verfahren_add(verfahren_neu)
        lst_cmpr_result.append(neueVerf)
    return lst_cmpr_result
            
def check_items(string_o, string_n):
    similar_factor=Levenshtein.distance(string_o, string_n)
    return similar_factor

def neue_verfahren_add(verfahren_neu):
    dict_neueVerfahren={}
    dict_neueVerfahren['Allgemeine TOM Nr']=verfahren_neu['Allgemeine TOM Nr']
    dict_neueVerfahren['Kategorie der allg. TOM']=verfahren_neu['Kategorie der allg. TOM']
    dict_neueVerfahren['Beschreibung']=verfahren_neu['Beschreibung']
    return dict_neueVerfahren

def vergleiche_bewerte(info_o, info_n, kat_o, verfahren_n, str_column, result_cmpr):
    check_info=check_items(str(info_o), str(info_n))
    if check_info>5 and check_info<500:
        # Speichern des Verfahrens und der Änderung in einem DICT
        #print ('Die Levensthein-Zahl für ' + verfahren_o['Bezeichnung'] + ' ' +  str_column + ' ist ' +  str(check_info))
        result_cmpr['Allgemeine TOM Nr']=verfahren_n['Allgemeine TOM Nr']
        result_cmpr['Kategorie der allg. TOM']=verfahren_n['Kategorie der allg. TOM']
        result_cmpr[str_column]='Änderungen'
    if check_info>500:
        result_cmpr['Allgemeine TOM Nr']=verfahren_n['Allgemeine TOM Nr']
        result_cmpr['Kategorie der allg. TOM']=verfahren_n['Kategorie der allg. TOM']
        result_cmpr[str_column]='ACHTUNG! Komplette Überarbeitung'
    return result_cmpr

def main(dict_old, dict_new):
    result=chk_TOM(dict_old, dict_new)
    return result

if (__name__=='__main__'):
    pass