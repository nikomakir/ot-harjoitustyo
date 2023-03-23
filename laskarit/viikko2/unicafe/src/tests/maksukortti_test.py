import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_rahan_laataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 12.00 euroa")

    def test_saldo_vahenee_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_nostettavaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_palauttaa_onnistumisen(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900),True)
    
    def test_rahan_ottaminen_palauttaa_False_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100),False)
