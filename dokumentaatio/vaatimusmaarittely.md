# Vaatimusmäärittely


## Sovelluksen idea

Sovellus on tunnettu Sudoku-peli. Pelissä käyttäjä täyttää 9x9 ruudukon siten, että jokaisella pysty- ja vaakarivillä on kaikki numerot 1-9:ään vain kerran ja lisäksi pienemmissä 3x3 ruudukoissa esiintyy jokainen luku vain kerran. Käyttäjä voi valita kolmesta eri vaikeustasosta "Easy", "Medium" tai "Hard". Käyttäjä voi jatkaa edellistä peliä tai luoda uuden pelin. Lisäksi peli mittaa aikaa ja muistiin jää paras suoritusaika jokaisesta vaikeustasosta.

## Käyttöliittymäluonnos

 - Graafinen käyttöliittymä
 - Aloitusruudulla valitaan, aloitetaanko uusi peli vai jatketaanko edellistä
 - Peliruudulla näkyy ruudukko ja kulmassa aika
 - Peliruudulla on nappi, josta pääsee takaisin aloitusruudulle

## Perusversion toiminnallisuus

 - Käyttäjä voi luoda uuden pelin tai jatkaa edellisestä pelistä, jos sellainen on kesken
  - pelistä valitaan vaikeustaso: Easy, Medium tai Hard
  - peli arpoo uuden ruudukon pohjan. Helpoimmassa vaikeustasossa on enemmän numeroita valmiiksi täytettynä kuin vaikeammilla tasoilla
 - Pelissä käyttäjä täyttää ruudukkoon puuttuvat numerot
  - käyttäjän itse täyttämiä numeroita voi muutella, mutta valmiina olevia ei
  - jos täyttää väärän numeron, niin se kyllä onnistuu, mutta numero muuttuu *punaiseksi* siinä vaiheessa, kun jokin pelin säännön ehdoista ei selvästi toteudu näkyvillä ja täytetyillä numeroilla
 - Peli päättyy, kun ruudukon kaikki numerot on täytetty oikein
  - muistiin jää paras suoritusaika jokaiselta vaikeustasolta
  - pelistä voi palata aloitusruudulle milloin tahansa, jolloin keskeneräinen peli jää muistiin

## Jatkokehitysideoita

Myöhemmin peliä voidaan täydentää:

 - Ruudulla on "Hint" -nappi, joka lisää jonkin puuttuvan numeron. Tämä toiminto voisi olla esim. helpoimmassa vaikeustasossa
 - Peli pitää lisäksi tilastoa pelatuista peleistä, kuinka monta on pelattu jne.
  - tilaston voi myös nollata
 


