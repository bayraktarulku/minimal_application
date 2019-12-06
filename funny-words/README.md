Inspired by the funny-words library.

## Command-line Usage
```sh
funny-words [-n] [-w] [-d] [-l]

-l, --language   Selects the language in which words are returned.
-n, --number     how many lines of funny words to generate
-w, --words      how many funny words to generate per line
-d, --delimiter  what to put between the funny words
```

## Command-line Examples

* if language = tr
```Its will return a funny tdk translate```
* else
```In its purest form funny-words will return a single pair of randomly
selected funny words separated by a space.```

```sh
$ python3 run.py
rainbow calculator
```

If you feel like being vertically loquacious you can increase the number of pairs returned with `-n, --number`

```sh
$ python3 funny_words/run.py --number 5
chalk pecan
kabob soya
aardvark stuffing
sunshine ache
buzz rotate
```

If you feel like being horizontally loquacious you can increase the number of words generated per line with `-w, --words`

```sh
$ python3 funny_words/run.py --words 4
chart squiggle camera spiral
```

If spaces are not your cup of tea you can change the delimiter between words with `-d, --delimiter`

```sh
$ python3 funny_words/run.py --delimiter -
shadow-magenta
```

And, as always, you can mix and match to suit your specific need

```sh
$ python3 funny_words/run.py --number 5 --language tr --words 1
light - yeğni
happy hour - indirim saatleri
prime time - altın saatler
bypass - köprüleme
panik - ürkü
```


Thanks TDK for translate.
