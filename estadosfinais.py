def token(chave):

    
    estados_finais = {
    
        'q7': 'eskreva',
        'q12': 'kinicio',
        'q14': 'enkuanto',
        'q22': 'kim',
        'q23': 'kint',
        'q26': 'sek',
        'q30': 'senaok',
        'q44': 'fimenkuanto',
        'q49': 'leiak',
        'q50': '+',
        'q51': '-',
        'q52': '*',
        'q53': '/',
        'q54': '(',
        'q55': ')',
        'q56': '<',
        'q57': '=',
        'q59': '==',
        'q58': ';',
        'q60': 'numeko',
        'q61': 'kid',
        'q64': 'string',
        'q65': '{',
        'q66': '}',

    }
    if chave in estados_finais:
        return estados_finais[chave]
    else:
        return False