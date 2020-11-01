def chk_ToDo(dict_old, dict_new):
    ToDo_old=dict_old['ToDos']
    ToDo_new=dict_new['ToDos']
    lst_cmpr_result=[]
    for x, verfahren_o in enumerate(ToDo_old):         
        beschr_o=verfahren_o['Beschreibung']
        for y, verfahren_n in enumerate(ToDo_new): 
            result_cmpr={}
            if verfahren_n['Beschreibung']==beschr_o:
                # überprüftes Verfahren wird gelöscht
                ToDo_new.pop(y) 
            if 'Bezeichnung' in result_cmpr:
                lst_cmpr_result.append(result_cmpr)
    # Hinzufügen der neuen Verfahren
    for verfahren_neu in ToDo_new:
        neueVerf=neue_verfahren_add(verfahren_neu)
        lst_cmpr_result.append(neueVerf)
    return lst_cmpr_result
            
def neue_verfahren_add(verfahren_neu):
    dict_neueVerfahren={}
    dict_neueVerfahren['Verfahren Nr']=verfahren_neu['Verfahren Nr']
    dict_neueVerfahren['Bezeichnung']=verfahren_neu['Bezeichnung']
    dict_neueVerfahren['Beschreibung']=verfahren_neu['Beschreibung']
    dict_neueVerfahren['Erledigt']='*** NEU *** TO DO ***'
    return dict_neueVerfahren

def main(dict_old, dict_new):
    result=chk_ToDo(dict_old, dict_new)
    return result

if (__name__=='__main__'):
    pass