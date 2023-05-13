# Ohjelmistotekniikka, harjoitustyö

## Sudoku
Harjoitustyön aiheena on Sudoku -peli. Pelissä voi asettaa vaikeustason ja ratkoa Sudoku -ruudukon. Ohjelma tallentaa myös keskeneräisen pelin ja sitä voi jatkaa. 

## Huomio ohjelman toimivuudesta

Ohjelmaa on testattu Python 3.10.6 versiolla. Sovelluksen vaatimuksena on versio 3.10 tai uudempi, eli toimivuudesta ei ole varmuutta vanhemmilla Python versioilla.

## Dokumentaatio
 - [Käyttöohje](./dokumentaatio/kayttoohje.md)

 - [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

 - [Vaatimusmaarittely](./dokumentaatio/vaatimusmaarittely.md)

 - [Changelog](./dokumentaatio/changelog.md)
 
 - [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

 - [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
 
## Lataaminen
- [Loppupalautus](https://github.com/nikomakir/ot-harjoitustyo/releases/tag/loppupalautus)
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

