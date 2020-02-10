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

while:

`python typelesson_generator.py -d ./dict/german/top30.txt abcdefghijklmnopqrstuvwxyz --max_chars=1000 --max_line_chars=200`

will produce:

```
und die dem eine auch auf ich sie auf nach des das nicht dass mit die sie von mit ist ich nach dass ist wie auch nicht sich auch als auch wie von mit eine nicht des wie die die die wie der der und auch
der mit den ist nach und eine des mit als ich von die wie die ist die das nicht die eine der von als auch nach von den von und des mit ich das wie der des die eine auch des ich mit dass und das nach dass
wie sie und des eine ich und dass eine ich der den wie sie auf der ist wie sich nach dass von die und nach den wie sie ist ich sich und dem das sie der und mit nach auf das dass dass sie dass der die nicht
das ich als des wie nach der sie als des ich das ein ist ich nicht auf das ich dass als wie die nach der eine des von von von und als ein des nicht eine nach sich mit sich als eine sich nach sie mit ein
von des dass als dem als eine das als dem des sich mit nach der ein nicht wie sie das sie die dem dass ich das der als ich dass ich dem mit nach ich das als ein nicht von sich auf dass dem auch
```
## License

This project is licensed under the MIT License - see the LICENSE.txt file for details