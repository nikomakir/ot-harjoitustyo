# Ohjelmistotekniikka, harjoitustyö

## Sudoku
Harjoitustyön aiheena on Sudoku -peli.

## Dokumentaatio

 - [tuntikirjanpito.md](./dokumentaatio/tuntikirjanpito.md)

 - [vaatimusmaarittely.md](./dokumentaatio/vaatimusmaarittely.md)

 - [changelog.md](./dokumentaatio/changelog.md)
 
## Asennus
Asenna riippuvuudet komennolla:
```
poetry install

``` 

## Komentorivitoiminnot

### Käynnistys

Ohjelman pystyy suorittaa komennolla:
```
poetry run invoke start

```
### Testaus

Testit ajetaan komennolla:
```
poetry run invoke test

```
### Testikattavuus

Kattavuusraportin voi luoda komennolla:
```
poetry run invoke coverage-report

``` 
Raportti generoituu _htmlcov_-nimiseen tiedostoon.
