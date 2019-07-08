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
        table = json.load(fin)

    update_transtable({
        key: value for key, value in table.items()
        if key not in 'あいうえおん'
    })
    _convert_dct.update(
        (key, value) for value, keys in table.items() for key in keys
        if value in 'あいうえおん'
    )
    _convert_dct.update([
        ('\'', ''), ('-', 'ー')
    ])


#
#
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

    if top_priority:
        _convert_dct.update(items, priority_func=lambda _: 0)
    else:
        _convert_dct.update(items)


def update_transtable(table):
    update_convert_dct({
        key: value for value, keys in table.items() for key in keys
    })


#
#
_convert_dct = PriorityDict(lambda k: 100-len(k))
_load_transtable()
