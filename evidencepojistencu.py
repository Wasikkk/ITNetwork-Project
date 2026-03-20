#!/usr/bin/env python3

from pojistenec import Pojistenec


class EvidencePojistencu:
    """Spravuje kolekci pojistencu - umoznuje pridavani a vyhledavani."""

    def __init__(self):
        """Inicializuje prazdnou evidenci pojistencu."""
        self._pojistenci = []

    def pridej(self, jmeno, prijmeni, vek, telefon):
        """Prida noveho pojisteneho do evidence po validaci vstupnich dat."""
        # Validace dat
        if not jmeno or not prijmeni:
            raise ValueError("Jmeno a prijmeni nesmi byt prazdne")
        if not isinstance(vek, int) or vek <= 0 or vek > 150:
            raise ValueError("Vek musi byt kladne cislo mezi 1-150")
        if not telefon or not telefon.strip():
            raise ValueError("Telefon nesmi byt prazdny")

        self._pojistenci.append(Pojistenec(jmeno, prijmeni, vek, telefon))

    def vyhledej(self, jmeno, prijmeni):
        """Vyhleda pojisteneho podle jmena a/nebo prijmeni."""
        if not jmeno and not prijmeni:
            return []

        nalezenci = []
        for pojistenec in self._pojistenci:
            if (not jmeno or pojistenec.jmeno == jmeno) and (not prijmeni or pojistenec.prijmeni == prijmeni):
                nalezenci.append(pojistenec)
        return nalezenci

    @property
    def pojistenci(self):
        """Vraci seznam vsech pojistencu."""
        return self._pojistenci
