# Dear Esther Translation File Converter

# FAQ

## What is this program for?
It converts your Dear Esther (2012) localisation files to Dear Esther: Landmark Edition (2017) version.

## But, why?
![But why image](http://giphygifs.s3.amazonaws.com/media/1M9fmo1WAFVK0/giphy.gif)
The original game has a redux version called Landmark Edition, which has been rewritten to another engine, and because of this, the resource files are in another format. The volunteer translators who made the translations for the original game did not create new ones for the new edition, so players trying the new one are forced to used the default languages. This program tries to solve this problem.

## It only converted some lines, why?
Currently, only lines in `closecaption_language.txt` can be converted, because these are the only lines where the keys belonging to the strings are the same in both versions.

To provide a solution to the differing keys, I created a `keys.json` file, where one could match old keys to the new ones.

## How can I contribute to this repository?
As mentioned above, a large part of strings cannot be converted currently, but matching the keys from the old translations (examples are in the `resources` folder) to the new ones would be a solution.

## Some string are shorter than the keys belonging to them. Wouldn't it be quicker to copy the strings instead of mapping the keys?
Sure, it might be, but mapping only has to be done once, while copying the strings would have to be done for every translation.

## The program crashes when I want to import a file other than `closecaption_language.txt`, why?
The program has **only** been tested with and optimised for this file, since this is the most important one regarding gameplay. Support for other files might be added later.

## What is the resources folder for?
It contains translation files collected from the internet, they are needed for developing and debugging the program. They are **not** made by me, links to the authors might be included in the corresponding files.

# How to use

usage: main.py [-h] -s SOURCE [-e ENCODING] [-x XMLSOURCE] -o OUTPUT

arguments:
```
-h, --help show this help message and exit

-s SOURCE, --source SOURCE your Dear Esther localisation file

-e ENCODING, --encoding ENCODING encoding of the source file, default is utf16

-x XMLSOURCE, --xmlsource XMLSOURCE a source XML file from the LE version. The default one is found inside the install folder

-o OUTPUT, --output OUTPUT name of the output localisation file.
```
## Two sources, what?
The first file, the `SOURCE` is the localised one you probably downloaded from a videogame translator forum, and it's in the format of the original Dear Esther game (which is why you are probably here in the first place). It's probably the right one if it's called `closecaption_<some_language>.txt`.

The second file, called `XMLSOURCE` is the one you need to copy from the folder of the DE: Landmark Edition. It is needed because the program itself cannot create a proper XML translation file, only overwrite an already existing one. You should use one in a language you already understand, because the strings that could not be translated will stay in this language. The default file is the English one, which is also included in this repository (`text_English.txt`), so if otherwise you are comfortable with the language, just skip this argument.

The game also includes French, German, Russian and Spanish translations, so if you prefer these languages, use these files as sources.

# License
[GPl v3.0](https://choosealicense.com/licenses/gpl-3.0/)

Pull requests are welcome and appreciated!