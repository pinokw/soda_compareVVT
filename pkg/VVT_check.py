import Levenshtein


def chk_VVT(dict_old, dict_new):
    vvt_old=dict_old['Verfahren']
    vvt_new=dict_new['Verfahren']
    lst_cmpr_result=[]
    for x, verfahren_o in enumerate(vvt_old):       #1. Verfahren in OLD
        bez_o=verfahren_o['Bezeichnung']        
        lfrst_o=verfahren_o['Löschfrist']
        risk_o=verfahren_o['Risiko für Betroffenen']
        descr_o=verfahren_o['Beschreibung des Vorgangs und Zweck der Verarbeitung']
        rgl_o=verfahren_o['Rechtsgrundlagen']
        rechtlW_o=verfahren_o['Rechtliche Würdigung']
        for y, verfahren_n in enumerate(vvt_new): 
            result_cmpr={}
            if verfahren_n['Bezeichnung']==bez_o:
                #Löschfrist
                lfrst_n=verfahren_n['Löschfrist']
                dict_compare=vergleiche_bewerte(lfrst_o, lfrst_n, bez_o, verfahren_o, 'Löschfrist', result_cmpr)
                result_cmpr=dict_compare

                #Risiko
                risk_n=verfahren_n['Risiko für Betroffenen']
                dict_compare=vergleiche_bewerte(risk_o, risk_n, bez_o, verfahren_o, 'Risiko für Betroffenen', result_cmpr)
                result_cmpr=dict_compare

                #Beschreibung
                descr_n=verfahren_n['Beschreibung des Vorgangs und Zweck der Verarbeitung']
                dict_compare=vergleiche_bewerte(descr_o, descr_n, bez_o, verfahren_o, 'Beschreibung des Vorgangs und Zweck der Verarbeitung', result_cmpr)
                result_cmpr=dict_compare

                # Rechtsgrundlage
                rgl_n=verfahren_n['Rechtsgrundlagen']
                dict_compare=vergleiche_bewerte(rgl_o, rgl_n, bez_o, verfahren_o, 'Rechtsgrundlagen', result_cmpr)
                result_cmpr=dict_compare

                #rechtlW
                rechtlW_n=verfahren_n['Rechtliche Würdigung']
                dict_compare=vergleiche_bewerte(rechtlW_o, rechtlW_n, bez_o, verfahren_o, 'Rechtliche Würdigung', result_cmpr)
                result_cmpr=dict_compare
                # überprüftes Verfahren wird gelöscht
                vvt_new.pop(y) 
            if 'Bezeichnung' in result_cmpr:
                lst_cmpr_result.append(result_cmpr)
    # Hinzufügen der neuen Verfahren
    for verfahren_neu in vvt_new:
        neueVerf=neue_verfahren_add(verfahren_neu)
        lst_cmpr_result.append(neueVerf)
    return lst_cmpr_result
            
def check_items(string_o, string_n):
    similar_factor=Levenshtein.distance(string_o, string_n)
    return similar_factor

def neue_verfahren_add(verfahren_neu):
    dict_neueVerfahren={}
    dict_neueVerfahren['Bezeichnung']=verfahren_neu['Bezeichnung']
    dict_neueVerfahren['Beschreibung des Vorgangs und Zweck der Verarbeitung']='Verfahren ist ** NEU **'
    return dict_neueVerfahren

def vergleiche_bewerte(info_o, info_n, bez_o, verfahren_o, str_column, result_cmpr):
    check_info=check_items(str(info_o), str(info_n))
    if check_info>5 and check_info<500:
        # Speichern des Verfahrens und der Änderung in einem DICT
        if bez_o in result_cmpr:
            result_cmpr[str_column]='Änderungen'
        elif bez_o not in result_cmpr:
            result_cmpr['Bezeichnung']=bez_o
            result_cmpr[str_column]='Änderungen'
    if check_info>500:
        if bez_o in result_cmpr:
            result_cmpr[str_column]='ACHTUNG: Komplette Überarbeitung'
        elif bez_o not in result_cmpr:
            result_cmpr['Bezeichnung']=bez_o
            result_cmpr[str_column]='ACHTUNG: Komplette Überarbeitung'
    return result_cmpr

def main(dict_old, dict_new):
    result=chk_VVT(dict_old, dict_new)
    return result

if (__name__=='__main__'):
    #dict_old={'Verfahren': [{
     #   'Nr': 1, 'Bezeichnung':
     #   'Aktenvernichtung', 
      #  'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
       # 'Die Aktenvernichtung (Papier) wird duch einen ext. DL [Firma] ausgeführt. Hierbei werden Personalakten und Akten mit Kundendaten vernichtet.', 
        #'Rechtsgrundlagen':
    #    'Art. 6 lit. c) (Gesetzliche Grundlage);Art. 6 lit. f) (berechtigtes Interesse)'}, 
    #    {'Nr': 2, 'Bezeichnung': 'EXT DL Hosting Webpage',
     #   'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
    #    'Die Fa. [NAME] hostet die Webpage. Weiterhin wir die WP von der Fa. [Name] betreut, Hierbei kann der ext. DL \
    #    bei Gelegenheit Kenntnis von [Nutzerdaten (IP Adresse, Nutzungsverhalten, E-Mail)] erlangen. Die Datenverarbeitung findet folgendermaßen statt: [Prozessbeschreibung]', 
    #    'Rechtsgrundlagen':
    #    'Art. 6 lit. f) (berechtigtes Interesse)'
    #    }], 'TOMS':[{'TOM': 1, 'Toms2': 2}, {'POM': 1, 'POM2': 2}]}
        
    #dict_new={'Verfahren': [{
    #    'Nr': 1, 'Bezeichnung':
    #    'Aktenvernichtung', 
    #    'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
    #    'Die Aktenvernichtung (Papier) wird duch einen ext. DL [Firma] ausgeführt. Hierbei werden Personalakten und Akten mit Kundendaten vernichtet.', 
    #    'Rechtsgrundlagen':
    #    'Art. 6 lit. c) (Gesetzliche Grundlage);Art. 6 lit. f) (berechtigtes Interesse)'}, 
    #    {'Nr': 2, 'Bezeichnung': 'EXT DL Hosting Webpage',
    #    'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
    #    'Die Fa. [NAME] hostet die Website. Weiterhin wir die WP von der Fa. [Name betreut, Hierbei kann der ext. DL \
    #    bei Gelegenheit Kenntnis von [Nutzerdaten IP Adresse, Nutzungsverhalten, E-Mail)] erlangen. Die Datenverarbeitung findet folgendermaßen statt: [Prozessbeschreibung]', 
    #    'Rechtsgrundlagen':
    #    'Art. 6 lit. f) (berechtigtes Interesse)'
    #    }], 'TOMS':[{'TOM': 1, 'Toms2': 2}, {'POM': 1, 'POM2': 2}]}
    #chk_VVT(dict_old, dict_new)
    pass