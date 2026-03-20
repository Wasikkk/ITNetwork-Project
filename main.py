#!/usr/bin/env python3
"""
Evidence pojistencu
Autor: Jan Wasserbauer
Verze: 1.0
Datum: 2026-02-23
Popis: Jednoducha aplikace pro spravu evidence pojistencu.
       Umoznuje pridavat, vypisovat a vyhledavat pojistene osoby.
"""

from evidencepojistencu import EvidencePojistencu
import os


###### FUNKCE ######
def zadej_text(vyzva):
    """Vyzve uzivatele k zadani textu a overi, ze obsahuje pouze pismena."""
    try:
        while True:
            text = input(vyzva)
            if not text.strip():
                print("Pole nesmi byt prazdne!")
            elif not text.isalpha():
                print("Pole musi obsahovat pouze pismena!")
            else:
                return text
    except Exception:
        print("Chyba pri zadavani textu!")


###### HLAVNI FUNKCE ######
def main():
    evidence = EvidencePojistencu()

    ###### MENU SMYCKA ######
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print("------------------------------------\nEvidence pojistenych\n------------------------------------\n")
            print()
            print("Zvolte číslo z MENU:\n\n1\t-\tPridat noveho pojistnika\n2\t-\tVypsat vsechny pojistene")
            print("3\t-\tVyhledat Pojistnika\n4\t-\tKonec")

            volba = input("Vase volba: ")
            match volba:
                case "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("------------------------------------\nRegistrace Pojistneho\n------------------------------------\n")
                    jmeno = zadej_text("Zadejte jmeno pojistneho: ")
                    prijmeni = zadej_text("Zadejte prijmeni pojistneho: ")
                    try:
                        telefon = int(input("Zadejte telefonní číslo: "))
                        vek = int(input("Zadejte věk: "))
                    except Exception:
                        print("Musis zadat ciselne hodnoty.")
                        input("\n\nStisknete Enter pro pokracovani...")
                        continue

                    try:
                        evidence.pridej(jmeno, prijmeni, vek, telefon)
                        print("\nPojistenec byl uspesne pridan!")
                    except ValueError as e:
                        print(f"\nChyba: {e}")
                    input("\n\nStisknete Enter pro pokracovani...")
                case "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("------------------------------------\nVypis vsech pojistenych\n------------------------------------\n")
                    if evidence.pojistenci:
                        for pojistenec in evidence.pojistenci:
                            print(pojistenec)
                    else:
                        print("Zadni pojistenci v evidenci.")
                    input("\n\nStisknete Enter pro pokracovani...")
                case "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("------------------------------------\nVyhledavani pojistneho\n------------------------------------\n")
                    jmeno = input("Zadej jmeno hledaneho pojistneho (nebo Enter pro preskoceni): ")
                    prijmeni = input("Zadej prijmeni hledaneho pojistneho (nebo Enter pro preskoceni): ")

                    nalezeni = evidence.vyhledej(jmeno, prijmeni)
                    if nalezeni:
                        print(f"\nNalezeno {len(nalezeni)} pojistencu:\n")
                        for pojistenec in nalezeni:
                            print(pojistenec)
                    else:
                        print("\nZadny pojistenec nenalezen.")
                    input("\n\nStisknete Enter pro pokracovani...")
                case "4":
                    break
                case _:
                    print("Neplatna volba, zkuste to znovu.")
        except Exception:
            print("Neco se pokazilo :-() ")


if __name__ == "__main__":
    main()
