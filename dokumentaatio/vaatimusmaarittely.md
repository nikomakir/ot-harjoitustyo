# Vaatimusmäärittely

## Sovelluksen idea

Sovellus on tunnettu Sudoku-peli. Pelissä käyttäjä täyttää 9x9 ruudukon siten, että jokaisella pysty- ja vaakarivillä on kaikki numerot 1-9:ään vain kerran ja lisäksi pienemmissä 3x3 ruudukoissa esiintyy jokainen luku vain kerran. Käyttäjä voi jatkaa edellistä peliä tai luoda uuden pelin.

## Käyttöliittymäluonnos

- Graafinen käyttöliittymä Pygame -kirjastolla
- Aloitusruudulla valitaan, aloitetaanko uusi peli vai jatketaanko edellistä, sekä voidaan siirtyä Options -valikkoon
- Peliruudulla näkyy ruudukko ja pelin vaikeustaso
- Peliruudulta pääsee takaisin aloitusruudulle

## Perusversion toiminnallisuus

- Käyttäjä voi luoda uuden pelin tai jatkaa edellistä peliä, jos sellainen on kesken
  - peli arpoo uuden ruudukon pohjan. Ruudukossa on valmiiksi täytettynä numeroita, jotta sen voi ratkaista
  - käyttäjä voi asettaa halutun vaikeustason Options -valikossa
- Pelissä käyttäjä täyttää ruudukkoon puuttuvat numerot
  - käyttäjän itse täyttämiä numeroita voi muutella, mutta valmiina olevia ei 
- Peli päättyy, kun ruudukon kaikki numerot on täytetty oikein
  - pelistä voi palata aloitusruudulle milloin tahansa, jolloin keskeneräinen peli jää muistiin 

## Jatkokehitysideoita

Myöhemmin peliä voidaan täydentää:
- Suoritusajan mittaus
- Peli pitää lisäksi tilastoa pelatuista peleistä, kuinka monta on pelattu jne.
 - tilaston voi myös nollata
- Peliä voi konfiguroida enemmän, esim. näytön kokoa, fonttia ja värejä.
 


