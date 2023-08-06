# col-spanish
A collection of tools to work with text write in Spanish (Colombia)


### Purpose of the Package
The purpose of the package is to create a group of functions that help to work with text in spanish, to be more accurate with spanish from Colombia.

### Features
+ normalization functions:
    - del_punctuation -> delete punctuation marks
    - del_accents -> delete accents

### Geting Started
The package can be found in Pypi, hence you can install it using pip
```bash
pip install col_spanish
```

### Usage
Using the normalization function to remove punctuation marks
```python
>>> from col_spanish import del_punctuation
>>> del_punctuation('Hola, ¿cómo estas? ¡bien!')
```


### Examples
```python
>>> from col_spanish import del_punctuation

>>> del_punctuation('Hola, ¿cómo estas? ¡bien!')
Hola cómo estas bien

>>> text = "Hola, ¿cómo estas? ¡bien!"
>>> normalized_text = del_punctuation(text)
>>> normalized_text
Hola cómo estas bien
```

### Contribution
Contributions are welcolme.
If you notice a bug let us know, thanks!

### Author
+ Main maintainer: Sergio A. Sosa Bautista (@sergioasb8)