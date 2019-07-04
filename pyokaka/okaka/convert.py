import json
from pathlib import Path


_dir = Path(__file__).parent

def _load_transtable():
    with (_dir / '../transtable.json').open() as fin:
        data = json.load(fin)

    convert_tpls = [
        (key, value) for value, keys in data.items() for key in keys
    ]
    convert_tpls += [
        ('{}{}'.format(key[0], key), 'っ{}'.format(value)) 
        for key, value in convert_tpls if key not in 'aiueon'
    ]
    convert_tpls += [('\'', ''), ('-', 'ー')]

    convert_tpls.sort(key=lambda e: len(e[0]), reverse=True)
    
    return convert_tpls


_convert_tpls = _load_transtable()
def convert(roman_sentence):
    roman_sentence = roman_sentence.lower()

    def step():
        for key, value in _convert_tpls:
            if roman_sentence.startswith(key):
                return key, value
        
        head_ch = roman_sentence[0]
        return head_ch, head_ch

    ret = []
    while roman_sentence:
        frm, to = step()

        ret.append(to)
        roman_sentence = roman_sentence[len(frm):]

    return ''.join(ret)
        
