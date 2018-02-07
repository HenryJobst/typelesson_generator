# Type lesson generator

A small program to generate type lesson texts of a given set of letters.

There are two modes. One is generating words with random letters and length out of the given possible letters.
The other mode is choosing words of a given dictionary with only the given letters.

## Usage

```
usage: typelesson_generator.py [-h] [-e EMPHASIS_LETTERS] [--version]
                               [-m {letters,words}] [-d DICTIONARY]
                               [--max_chars MAX_CHARS]
                               [--max_line_chars MAX_LINE_CHARS]
                               [--min_word_len MIN_WORD_LEN]
                               [--max_word_len MAX_WORD_LEN]
                               letters

Typewriting lesson generator.

positional arguments:
  letters               no other letters, than this

optional arguments:
  -h, --help            show this help message and exit
  -e EMPHASIS_LETTERS, --emphasis_letters EMPHASIS_LETTERS
                        letters in every word
  --version             show program's version number and exit
  -m {letters,words}, --mode {letters,words}
                        generation mode, default: words
  -d DICTIONARY, --dictionary DICTIONARY
                        filename for a dictionary file
  --max_chars MAX_CHARS
                        target char length
  --max_line_chars MAX_LINE_CHARS
                        target line char length
  --min_word_len MIN_WORD_LEN
                        minimum word length
  --max_word_len MAX_WORD_LEN
                        maximum word length
```

## Getting started

`python3 typelesson_generator.py haeiudtrnsf -m letters`

will produce:

```
erf fihd hshth hdnrtr ash uue set hhhu ineau fsahfd etu fha
fefn hiu sea tnif aetts are teh iata ttfhh ddienh irn erd
huui hefaf ansiad fsu dnst duisr retnnt fan uas frea tht
ress ihe nasu nnhts ssd adh sinn aun stf ifs ehif hdush arfntr
tri nhdr iaaui tntsad sah edhd ufirh sndhfe tne ruef nihfs
srn ehsi nrhia nah aruu hhd rsuh sdstt isiruf etu tsi tnff
snu shhd dnrea rftinr erh faf deda sthru safdsa fdr rrns
itnff dhs hstd fni ehrs ihr isds hri afis dtsdu dht iatf
sdfse ufrhsh san aeir ush aiht fas fhnh tes usut rrdia aae
naft aharh rufann sia ass frrf eiinh uda nasi utntn hfsaii
fad strn rieda ranfaf eff

```
while:

`python3 typelesson_generator.py haeiudtrnsf`

will produce:

```
eher einst erriet sauste eher fast ehrend rinnen hauten sahne
diffus rare daher arides des raffe tatest hure frei tute
rundet feste uns nein daher erdete friss heftet turn hautet
haue diese neu ferne reifst niest ihren nasses einen fasse
sieht runter siede rundet sieden freuen heitre frei riss
freut anrede ihren nennst hefte ruhe drehst tatest steter
eifern tauen staust drauf darein fahren ihn feine faires
unter tutet eins friert unsre fassen raue untreu harren redet
raufst neu ahnend endete auftut entern straff ahndet reiht
sannt artet indes erriet ehrtet rares hisst traf untief inne
erstes dein niste andres
```

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details