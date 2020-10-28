


def chk_VVT(dict_old, dict_new):
    for key_old, value_old in dict_old.items():
        for key_new, value_new in dict_new.items():
            if key_new==key_old=='Verfahren':
                for x, item in enumerate(value_old):
                    print (item[x])


if (__name__=='__main__'):
    dict_old={'Verfahren': [{
        'Nr': 1, 'Bezeichnung':
        'Aktenvernichtung', 
        'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
        'Die Aktenvernichtung (Papier) wird duch einen ext. DL [Firma] ausgeführt. Hierbei werden Personalakten und Akten mit Kundendaten vernichtet.', 
        'Rechtsgrundlagen':
        'Art. 6 lit. c) (Gesetzliche Grundlage);Art. 6 lit. f) (berechtigtes Interesse)'}, 
        {'Nr': 2, 'Bezeichnung': 'EXT DL Hosting Webpage ',
        'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
        'Die Fa. [NAME] hostet die Webpage. Weiterhin wir die WP von der Fa. [Name] betreut, Hierbei kann der ext. DL \
        bei Gelegenheit Kenntnis von [Nutzerdaten (IP Adresse, Nutzungsverhalten, E-Mail)] erlangen. Die Datenverarbeitung findet folgendermaßen statt: [Prozessbeschreibung]', 
        'Rechtsgrundlagen':
        'Art. 6 lit. f) (berechtigtes Interesse)'
        }], 'TOMS':[{'TOM': 1, 'Toms2': 2}, {'POM': 1, 'POM2': 2}]}
        
    dict_new={'Verfahren': [{
        'Nr': 1, 'Bezeichnung':
        'Aktenvernichtung', 
        'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
        'Die Aktenvernichtung (Papier) wird duch einen ext. DL [Firma] ausgeführt. Hierbei werden Personalakten und Akten mit Kundendaten vernichtet.', 
        'Rechtsgrundlagen':
        'Art. 6 lit. c) (Gesetzliche Grundlage);Art. 6 lit. f) (berechtigtes Interesse)'}, 
        {'Nr': 2, 'Bezeichnung': 'EXT DL Hosting Webpage ',
        'Beschreibung des Vorgangs und Zweck der Verarbeitung': 
        'Die Fa. [NAME] hostet die Webpage. Weiterhin wir die WP von der Fa. [Name] betreut, Hierbei kann der ext. DL \
        bei Gelegenheit Kenntnis von [Nutzerdaten (IP Adresse, Nutzungsverhalten, E-Mail)] erlangen. Die Datenverarbeitung findet folgendermaßen statt: [Prozessbeschreibung]', 
        'Rechtsgrundlagen':
        'Art. 6 lit. f) (berechtigtes Interesse)'
        }], 'TOMS':[{'TOM': 1, 'Toms2': 2}, {'POM': 1, 'POM2': 2}]}
    chk_VVT(dict_old, dict_new)
    pass