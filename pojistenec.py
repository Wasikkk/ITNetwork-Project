#!/usr/bin/env python3

class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"Jmeno: {self.jmeno}\tPrijmeni: {self.prijmeni}\tTelefon: {self.telefon}\tVek: {self.vek}"
    