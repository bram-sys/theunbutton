#!/usr/bin/env python3
"""
Uitbetalingsverdeling — Achter Vergeten Deuren
Na wegvallen Janivo (€3.000) en Amarte (€3.500)
"""

# === INKOMSTEN ===
inkomsten = {
    "Uitkoopsommen (Delft Fringe)": 3_900,
    "Sponsor NLE Tech":              350,
    "Fonds ZOZ":                   4_000,
}
inkomsten_totaal = sum(inkomsten.values())  # €8.250

# === PRODUCTIEKOSTEN (niet-personen) ===
productiekosten = {
    "Repetitieruimte":      700 - 100,  # €100 bespaard
    "Decór":                350,
    "Kostuum":              250,
    "Technisch materieel":  500 - 200,  # €200 bespaard
    "Social Media":         100,
    "Drukwerk":             150,
    "Verspreiding":         300,
}
productie_totaal = sum(productiekosten.values())

# === BESCHIKBAAR VOOR PERSONEN ===
beschikbaar = inkomsten_totaal - productie_totaal

# === PERSONEN & DAGEN ===
# Maker (Anouscha): 6 dagen regie + 5 dagen script = 11 dagen
# 5 Acteurs: 6 dagen repetitie + 3 speeldagen = 9 dagen per acteur
# Technicus: 3 speeldagen
# Productie: 3 speeldagen

maker_dagen = 11
acteur_dagen = 9
technicus_dagen = 3
productie_dagen = 3
aantal_acteurs = 5

totaal_dagen = (
    maker_dagen
    + aantal_acteurs * acteur_dagen
    + technicus_dagen
    + productie_dagen
)

# === VERDELING ===
# Basisvergoeding per dag voor iedereen, plus een creatieve toeslag
# voor de maker (script + regie = intellectueel eigendom)

basis_dagvergoeding = 95  # per dag, voor iedereen
maker_creatieve_toeslag = 300  # extra voor script + regie IP

maker_basis = maker_dagen * basis_dagvergoeding
maker_totaal = maker_basis + maker_creatieve_toeslag
acteur_totaal = acteur_dagen * basis_dagvergoeding
technicus_totaal = technicus_dagen * basis_dagvergoeding
productie_totaal_persoon = productie_dagen * basis_dagvergoeding

uitbetaling_totaal = (
    maker_totaal
    + aantal_acteurs * acteur_totaal
    + technicus_totaal
    + productie_totaal_persoon
)
buffer = beschikbaar - uitbetaling_totaal

# === RAPPORT ===
print("=" * 60)
print("  UITBETALINGSVERDELING — ACHTER VERGETEN DEUREN")
print("=" * 60)

print("\n📊 FINANCIEEL OVERZICHT")
print("-" * 60)
print(f"{'Inkomsten (zonder Janivo & Amarte):':<42} €{inkomsten_totaal:>7,.0f}")
for naam, bedrag in inkomsten.items():
    print(f"  · {naam:<38} €{bedrag:>7,.0f}")

print(f"\n{'Productiekosten (aangepast):':<42} €{sum(productiekosten.values()):>7,.0f}")
for naam, bedrag in productiekosten.items():
    print(f"  · {naam:<38} €{bedrag:>7,.0f}")

print("-" * 60)
print(f"{'BESCHIKBAAR VOOR UITBETALING:':<42} €{beschikbaar:>7,.0f}")

print(f"\n\n💰 VOORGESTELDE VERDELING")
print("-" * 60)
print(f"  Basisdagvergoeding:     €{basis_dagvergoeding}/dag (voor iedereen)")
print(f"  Maker creatieve toeslag: €{maker_creatieve_toeslag} (script + regie IP)")
print()

print(f"  {'Persoon':<22} {'Dagen':>5}  {'Basis':>8}  {'Toeslag':>8}  {'Totaal':>8}")
print(f"  {'-'*22} {'-'*5}  {'-'*8}  {'-'*8}  {'-'*8}")
print(f"  {'Maker (Anouscha)':<22} {maker_dagen:>5}  €{maker_basis:>6,.0f}  €{maker_creatieve_toeslag:>6,.0f}  €{maker_totaal:>6,.0f}")
for i in range(1, aantal_acteurs + 1):
    print(f"  {'Acteur ' + str(i):<22} {acteur_dagen:>5}  €{acteur_totaal:>6,.0f}  €{'—':>6}  €{acteur_totaal:>6,.0f}")
print(f"  {'Technicus':<22} {technicus_dagen:>5}  €{technicus_totaal:>6,.0f}  €{'—':>6}  €{technicus_totaal:>6,.0f}")
print(f"  {'Productie':<22} {productie_dagen:>5}  €{productie_totaal_persoon:>6,.0f}  €{'—':>6}  €{productie_totaal_persoon:>6,.0f}")
print(f"  {'-'*22} {'-'*5}  {'-'*8}  {'-'*8}  {'-'*8}")
print(f"  {'TOTAAL UITBETALING':<22} {totaal_dagen:>5}  {'':>8}  {'':>8}  €{uitbetaling_totaal:>6,.0f}")
print(f"  {'Buffer':<22} {'':>5}  {'':>8}  {'':>8}  €{buffer:>6,.0f}")

print(f"\n\n📋 SAMENVATTING PER PERSOON")
print("-" * 60)
print(f"  Maker (Anouscha):  €{maker_totaal:>6,.0f}  ({maker_dagen} dagen × €{basis_dagvergoeding} + €{maker_creatieve_toeslag} toeslag)")
print(f"  Per acteur:        €{acteur_totaal:>6,.0f}  ({acteur_dagen} dagen × €{basis_dagvergoeding})")
print(f"  Technicus:         €{technicus_totaal:>6,.0f}  ({technicus_dagen} dagen × €{basis_dagvergoeding})")
print(f"  Productie:         €{productie_totaal_persoon:>6,.0f}  ({productie_dagen} dagen × €{basis_dagvergoeding})")

verschil_pct = ((maker_totaal / acteur_totaal) - 1) * 100
print(f"\n  → Maker krijgt {verschil_pct:.0f}% meer dan elke acteur")
print(f"  → Speeldagen gelijk verdeeld: elke acteur speelt alle {3} dagen")

print(f"\n\n✅ WAAROM MEER VOOR DE MAKER?")
print("-" * 60)
print("""  1. Creatief eigenaarschap — Anouscha schreef het script en
     regisseerde. Dat is intellectueel eigendom.
  2. Meer werkdagen — 11 dagen (regie + script) vs 9 per acteur.
  3. Verantwoordelijkheid — artistieke en organisatorische
     eindverantwoordelijkheid voor het gehele project.
  4. Branchestandaard — in de podiumkunsten is het gebruikelijk
     dat makers meer verdienen dan uitvoerenden.

  De toeslag van €300 is bescheiden en erkent de extra creatieve
  investering zonder de acteurs tekort te doen.""")

print(f"\n{'=' * 60}")
