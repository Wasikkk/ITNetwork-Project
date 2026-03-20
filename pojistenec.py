#!/usr/bin/env python3


class Pojistenec:
    """Reprezentuje pojisteneho - uchovava jeho osobni udaje."""

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """Inicializuje pojisteneho se zadanymi udaji."""
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """Vraci textovou reprezentaci pojisteneho."""
        return f"Jmeno: {self.jmeno}\tPrijmeni: {self.prijmeni}\tTelefon: {self.telefon}\tVek: {self.vek}"
