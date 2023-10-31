import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negatiivinen_varasto = Varasto(-10)
        self.negatiivinen_saldo = Varasto(10, -10)
        self.suuri_saldo_varasto = Varasto(10, 20)

    def test_konstruktori_nollaa_negatiivisen_varaston(self):
        self.assertAlmostEqual(self.negatiivinen_varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_saldon(self):
        self.assertAlmostEqual(self.negatiivinen_saldo.saldo, 0)
    
    def test_konstruktori_saldo_ei_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.suuri_saldo_varasto.saldo, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_saldo(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_saldoa_yli_tilavuuden_verran(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ota_varastosta_negatiivinen_summa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-12)

        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_ota_varastosta_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_varasto_string_muoto(self):
        varasto_str = "saldo = 0, vielä tilaa 10"
        self.assertAlmostEqual(str(self.varasto), varasto_str)
