# Ohjelmistotekniikka, harjoitustyö

## Sudoku
Harjoitustyön aiheena on Sudoku -peli.

## Dokumentaatio
 - [käyttöohje](./dokumentaatio/kayttoohje.md)

 - [tuntikirjanpito.md](./dokumentaatio/tuntikirjanpito.md)

 - [vaatimusmaarittely.md](./dokumentaatio/vaatimusmaarittely.md)

 - [changelog.md](./dokumentaatio/changelog.md)
 
 - [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
 
## Lataaminen
- [Release 1](https://github.com/nikomakir/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/nikomakir/ot-harjoitustyo/releases/tag/viikko6)
 
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

### Pylint

Pylint -tarkistus ajetaan komennolla:
```
poetry run invoke lint

