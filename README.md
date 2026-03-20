# Evidence pojištěnců

Konzolová aplikace pro správu evidence pojištěných osob. Projekt byl vytvořen jako součást kurzu Python OOP na platformě ITnetwork.

## Funkce

- Přidání nového pojištěného (jméno, příjmení, věk, telefonní číslo)
- Výpis všech pojištěných
- Vyhledání pojištěného podle jména a/nebo příjmení

## Spuštění

Aplikace nevyžaduje žádné externí závislosti. Stačí mít nainstalovaný Python 3.10+.

```bash
python main.py
```

## Struktura projektu

```
├── main.py                  # Hlavní soubor, UI a menu
├── evidencepojistencu.py    # Třída EvidencePojistencu - správa kolekce
└── pojistenec.py            # Třída Pojistenec - datový model
```

