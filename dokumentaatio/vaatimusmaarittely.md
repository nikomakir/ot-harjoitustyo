# Vaatimusmäärittely

## Sovelluksen idea

Sovellus on tunnettu Sudoku-peli. Pelissä käyttäjä täyttää 9x9 ruudukon siten, että jokaisella pysty- ja vaakarivillä on kaikki numerot 1-9:ään vain kerran ja lisäksi pienemmissä 3x3 ruudukoissa esiintyy jokainen luku vain kerran. Käyttäjä voi jatkaa edellistä peliä tai luoda uuden pelin. Lisäksi peli mittaa aikaa ja muistiin jää paras suoritusaika jokaisesta vaikeustasosta (alussa vain yksi taso ja myöhemmin mahdollisesti lisää).

## Käyttöliittymäluonnos

- Graafinen käyttöliittymä Pygame -kirjastolla
- Aloitusruudulla valitaan, aloitetaanko uusi peli vai jatketaanko edellistä
- Peliruudulla näkyy ruudukko ja kulmassa aika
- Peliruudulla on nappi, josta pääsee takaisin aloitusruudulle

## Perusversion toiminnallisuus

- Käyttäjä voi luoda uuden pelin *(tehty)* tai jatkaa edellisestä pelistä *(tehty)*, jos sellainen on kesken
  - peli arpoo uuden ruudukon pohjan. Ruudukossa on valmiiksi täytettynä numeroita, jotta sen voi ratkaista *(tehty)*
- Pelissä käyttäjä täyttää ruudukkoon puuttuvat numerot *(tehty)*
  - käyttäjän itse täyttämiä numeroita voi muutella, mutta valmiina olevia ei *(tehty)*
  - jos täyttää väärän numeron, niin se kyllä onnistuu, mutta numero muuttuu *punaiseksi* siinä vaiheessa, kun jokin pelin säännön ehdoista ei selvästi toteudu näkyvillä ja täytetyillä numeroilla
- Peli päättyy, kun ruudukon kaikki numerot on täytetty oikein
  - muistiin jää paras suoritusaika jokaiselta vaikeustasolta
  - pelistä voi palata aloitusruudulle milloin tahansa, jolloin keskeneräinen peli jää muistiin *(tehty)*

## Jatkokehitysideoita

Myöhemmin peliä voidaan täydentää:
- Peliin lisätään vaikeustasoja, esim. kaksi vaikeampaa tasoa, jossa olisi vähemmän valmiina olevia numeroita
- Ruudulla on "Hint" -nappi, joka lisää jonkin puuttuvan numeron. Tämä toiminto voisi olla esim. helpoimmassa vaikeustasossa
- Peli pitää lisäksi tilastoa pelatuista peleistä, kuinka monta on pelattu jne.
 - tilaston voi myös nollata
 


