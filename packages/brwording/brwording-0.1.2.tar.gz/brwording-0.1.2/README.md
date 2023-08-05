## `BRWording` - Text Analytics for Portuguese Wordings

Create an easy Text Analytics in *`One-Line-Code`*

<hr>

![](https://img.shields.io/badge/pypi-2.2.0-blue) ![](https://img.shields.io/badge/python-3.0|3.0|3.0-lightblue) ![](https://img.shields.io/badge/Licence-MIT-lightgray) ![](https://img.shields.io/badge/status-Beta-darkgreen) ![](https://img.shields.io/badge/pipeline-passed-green) ![](https://img.shields.io/badge/testing-passing-green) ![](https://img.shields.io/badge/TheScientist-APP-brown)


**Main Features:**

- Load `Excel`, `CSV` and `TXT` file types
- Stemming
- Lemmatization
- Stopwords
- TD-IDF
- Sentimental Analysis
- Graphical interpretation
- Word Cloud

The TF-IDF was calculated by:

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/tf-idf.png?raw=true)

<hr>

## How to Install

```shell
pip install BRWording
pip install pdfminer-six
```

<BR>
<hr>
<BR>

## How to use

`sintax`:
```python
from brwording import brwording

w = brwording.wording()

w.load_file('data/example.txt',type='txt')
w.build_tf_idf(lemmatizer=True,stopwords=True)

w.tfidf

```

The fields to `load_file` are:
2. `file`: the file path 
2. `type`: file type, can be `txt csv` or `excel`
3. `header`: if you are reading a csv file, so you must tell if this file has a header or not (`False` or `True`)
0. `sep`: if you are reading a csv file, you must tell what kind field separator you want
0. `column`: if you read a `csv` or `excel`file, you must tell what column you want to parse

The method `build_tf_idf` has a default `True`option for both parameters.

**Output**

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/tfidf.png?raw=true)

If want to see the sentimental Graphical interpretation

`sintax`:
```python

w.sentimental_graf()

```
You can rotate the graph if you pass `rotate=True` in argument

**output**

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/graf_sentimental.png?raw=true)

You can print the same information as a table using the follow command:


`sintax`:
```python

w.sentimental_table()

```

<br>

if you want to create a wordcloud, just strike the folowing command, but if you want to create a cloud with your own mask, just pass you image address as `picture`

`sintax`:
```python
w.word_cloud(picture='none')

```

**output**

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/wc.png?raw=true)

<hr>
<BR>

**Looking for a word into colection**

if you want to see what files on your colection has a word, run `look2word` 

`sintax`:
```python
w.look2word('bonito')

```

<BR>

New features are incoming.

<hr>
<BR>

`enjoi!`