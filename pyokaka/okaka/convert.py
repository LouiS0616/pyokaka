from ..util.priority_dict import PriorityDict

import json
from pathlib import Path


_dir = Path(__file__).parent

def _make_sokuon_tpls(items):
    return [
        ('{}{}'.format(key[0], key), 'っ{}'.format(value))
        for key, value in items
    ]

def _load_transtable():
    with (_dir / '../transtable.json').open() as fin:
        data = json.load(fin)

    convert_tpls = [
        (key, value) for value, keys in data.items() for key in keys
    ]
    convert_tpls += _make_sokuon_tpls(
        filter(lambda kv: kv[-1] not in 'あいうえおん', convert_tpls)
    )
    convert_tpls += [('\'', ''), ('-', 'ー')]

    pd = PriorityDict(lambda k: 100-len(k))
    pd.update(convert_tpls)
    return pd


#
#
_convert_dct = _load_transtable()
def convert(roman_sentence):
    roman_sentence = roman_sentence.lower()

    def step():
        for key, value in _convert_dct.items():
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
        

def update_convert_dct(dct, *, top_priority=False):
    items = tuple(dct.items())
    items = {
        **dct, **dict(_make_sokuon_tpls(items))
    }

    print(items)

    if top_priority:
        _convert_dct.update(items, priority_func=lambda _: 0)
    else:
        _convert_dct.update(items)

