import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_myydyt_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_myydyt_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_syo_kateisella_edullisesti_palauttaa_oikein_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300),60)

    def test_syo_kateisella_edullisesti_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)

    def test_syo_kateisella_edullisesti_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_syo_kateisella_edullisesti_raha_ei_riita_ja_kassa_sama(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_syo_kateisella_edullisesti_raha_ei_riita_ja_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)

    def test_syo_kateisella_edullisesti_raha_ei_riita_myydyt_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_kateisella_maukkaasti_palauttaa_oikein_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)

    def test_syo_kateisella_maukkaasti_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)

    def test_syo_kateisella_maukkaasti_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_kateisella_maukkaasti_raha_ei_riita_ja_kassa_sama(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_syo_kateisella_edullisesti_raha_ei_riita_ja_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100),100)

    def test_syo_kateisella_edullisesti_raha_ei_riita_myydyt_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_kortilla_edullisesti_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
    
    def test_syo_kortilla_edullisesti_rahaa_tarpeeksi_kortin_saldo_laskee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 7.60 euroa")

    def test_syo_kortilla_edullisesti_rahaa_tarpeeksi_kassa_nousee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_syo_kortilla_edullisesti_rahaa_ei_tarpeeksi(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti),False)

    def test_syo_kortilla_edullisesti_rahaa_ei_tarpeeksi_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti),"Kortilla on rahaa 1.00 euroa")

    def test_syo_kortilla_edullisesti_rahaa_ei_tarpeeksi_myydyt_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_syo_kortilla_maukkaasti_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
    
    def test_syo_kortilla_maukkaasti_rahaa_tarpeeksi_kortin_saldo_laskee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 6.00 euroa")

    def test_syo_kortilla_maukkaasti_rahaa_tarpeeksi_kassa_nousee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_syo_kortilla_maukkaasti_rahaa_ei_tarpeeksi(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti),False)

    def test_syo_kortilla_edullisesti_rahaa_ei_tarpeeksi_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti),"Kortilla on rahaa 1.00 euroa")

    def test_syo_kortilla_edullisesti_rahaa_ei_tarpeeksi_myydyt_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_syo_kortilla_edullisesti_kassa_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_syo_kortilla_maukkaasti_kassa_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kortille_lataus_kasvattaa_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 20.00 euroa")

    def test_kortille_lataus_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,101000)

    def test_lataus_kortille_ei_onnistu_jos_negatiivinen(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-500),None)