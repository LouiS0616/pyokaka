pyokaka
===
Simple tool for convert [Roma-ji][^1] sentence into [Hiragana][^2] one.\
ローマ字の文を平仮名に変換するシンプルなツールです。

## The origin of package name

By homage to [pykakashi](https://pypi.org/project/pykakasi/), what provides highly function to convert Kana-Kanji into Roma-ji.

_Okaka_(おかか) means bonito flakes in informal Japanese.

[^1]: https://en.wikipedia.org/wiki/Romanization_of_Japanese
[^2]: https://en.wikipedia.org/wiki/Hiragana

## Demo

**As command line tool**\
Use as REPL just by calling. To quit, send EOF.
```cmd
$ python -m pyokaka.okaka

Roman >>> ohayougozaimasu
JKana ... おはようございます
Roman >>> kon'nichiwa
JKana ... こんにちわ
Roman >>> oyasuminasai
JKana ... おやすみなさい
```

You can indicate file you want to convert.
```cmd
$ cat sample.txt
Ima wa mukashi, taketori no okina to iu mono ari keri.

$ python -m pyokaka.okaka sample.txt
いま わ むかし, たけとり の おきな と いう もの あり けり.
```

To apply additional rule, load json file in **utf-8**.
```json:sample.json
{
    "ら": ["la"], "り": ["li"], "る": ["lu"], "れ": ["le"], "ろ": ["lo"],
    "ふぁ": ["pha", "hua"], "ふぃ": ["phi"]
}
```

```cmd
$ cat sample.txt
elephant
lalallalalla

$ python -m pyokaka.okaka sample.txt
えlえpはんt
lあlあllあlあllあ

$ python -m pyokaka.okaka sample.txt --load sample.json
load for sample.json...
えれふぁんt
ららっららっら
```

For more information, view `python -m pyokaka.okaka --help`.

**As library**
```python
>>> from pyokaka import okaka
>>> okaka.convert('katsuobushi')
'かつおぶし'
```

You can add more vocabulary use convert dict or transtable from json.
```python
>>> okaka.convert('philipps')
'pひlいpps'
>>>
>>> okaka.update_convert_dct({
...     'p': 'ぷ', 's': 'す'
... })
>>>
>>> okaka.convert('philips')
'ぷひlいぷす'
>>>
>>> import json
>>> with open('sample.json', encoding='utf-8') as fin:
...     table = json.load(fin)
...
>>> okaka.update_transtable(table)
>>> okaka.convert('philips')
'ふぃりぷす'
```

## Notes

- You cannot reset convert table without restart.
- Though converter ignores letter what can be not interpret as a part of Roma-ji, remaining letters always be converted.
    ```cmd
    $ python -m pyokaka.okaka
    Roman >>> Oh dear, this is English!
    JKana ... おh であr, tひs いs えんglいsh!
    ```

- Hyphen always be replaced with [Cho'onpu](https://en.wikipedia.org/wiki/Ch%C5%8Donpu).
    ```cmd
    $ python -m pyokaka.okaka
    Roman >>> Roma-ji
    JKana ... ろまーじ
    ```

- Converter never analyze sentence structure. So it cannot recognize 'wa', 'o' and 'e' as postpositional particle.
    ```cmd
    $ python -m pyokaka.okaka
    Roman >>> Watashi wa depa-to e enpitsu o kai ni ikimashita.
    JKana ... わたし わ でぱーと え えんぴつ お かい に いきました.
    ```

- Conversion is based on greedy algorithm. Single quote can be used as separater if you need.
    ```cmd
    Roman >>> honya
    JKana ... ほにゃ
    Roman >>> honnya
    JKana ... ほっにゃ
    Roman >>> honnnya
    JKana ... ほんにゃ

    Roman >>> hon'ya
    JKana ... ほんや
    ```

## Install

This module is registered at PyPI. [PyPI - pyokaka](https://pypi.org/project/pyokaka/)

```
$ pip install pyokaka
```

## License
[MIT](https://github.com/LouiS0616/brainbite/blob/master/LICENSE)

## Author
[LouiS0616](https://github.com/LouiS0616)