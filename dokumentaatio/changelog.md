# Changelog

## Viikko 3

- lisätty Sudoku -luokka
- lisätty pelilogiikasta vastaava luokka GameGrid
- lisätty käyttöliittymästä vastaavat luokat GameLoop, Renderer, EventQueue
- lisätty testit kattamaan koko Sudoku -luokan

## Viikko 4

- lisätty käyttöliittymään Menu -luokka, joka vastaa aloitusvalikosta
- muokattu Sudoku -luokkaa 
    - nyt voi generoida täytettävän ruudukon dokusan -kirjaston avulla
    - päivitetty check_if_complete metodin toiminta vastaamaan luokan uuttaa toiminnallisuutta
- muokattu GameGrid -luokkaa
    - nyt voi luoda eri vaikeustason pelejä, mutta vielä ei ole käyttöliittymässä valintamahdollisuutta
- muokattu Sudoku -luokan testit kattamaan koko luokan
- lisätty testejä GameGrid -luokalle

## Viikko 5

- lisätty repositorio -mallinen tallennusluokka SudokuRepository, joka vastaa sudokuruudukon tallennuksesta
- sovelluslogiikasta vastaavan GameGrid -luokan nimi muutettu GameService 
- muutettu sovelluslogiikasta vastaavan luokan GameService toimintaa siten, että se tallentaa ja lataa pelitietoa SudokuRepository luokan avulla csv tiedostoon
    - lisäksi pystyy nyt luomaan uuden pelin aina luokan sisällä
- muutettu Sudoku -luokan toimintaa siten, että oletusarvoisesti luo uuden ruudukon dokusan kirjastolla
    - voi antaa argumentteina valmiit listat, joiden mukaan luokka toimii normaalisti
    
