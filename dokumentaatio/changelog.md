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
