#!/usr/bin/env python3

from pojistenec import Pojistenec


class EvidencePojistencu:

    def __init__(self):
        self._pojistenci = []

    def pridej(self, jmeno, prijmeni, vek, telefon):
        # Validace dat
        if not jmeno or not prijmeni:
            raise ValueError("Jmeno a prijmeni nesmi byt prazdne")
        if not isinstance(vek, int) or vek <= 0 or vek > 150:
            raise ValueError("Vek musi byt kladne cislo mezi 1-150")
        if not isinstance(telefon, int) or telefon <= 0:
            raise ValueError("Telefon musi byt kladne cislo")

        self._pojistenci.append(Pojistenec(jmeno, prijmeni, vek, telefon))

    def vyhledej(self, jmeno, prijmeni):
        if not jmeno and not prijmeni:
            return []

        nalezenci = []
        for pojistenec in self._pojistenci:
            if (not jmeno or pojistenec.jmeno == jmeno) and (not prijmeni or pojistenec.prijmeni == prijmeni):
                nalezenci.append(pojistenec)
        return nalezenci

    @property
    def pojistenci(self):
        return self._pojistenci
    
