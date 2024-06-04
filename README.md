# pdf_lightner

Lighten the annotations inside a pdf

## Why do I need to lighten my annotations ?

[Okular](https://okular.kde.org/fr/) will use the stroke color of some annotations for the box with the annotation text. If the stroke is a dark color, the text will not be readable


### Before
![Note before](img/Note_before.png)
![Caret before](img/Caret_before.png)

### After
![Note before](img/Note_after.png)
![Caret before](img/Caret_after.png)

## Installation
You can install it with pip:
```
pip install pdf_lightner
```

Or you can install it from the source
```
pip install .
```

## How to use
To lighten a pdf:
```
pdf_lightner lighten PATH_TO_PDF
```

It will create a new file with `_ligthen` added to the name of the file.


To get more info
```
pdf_lightner -h
```
