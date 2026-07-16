# -*- coding: utf-8 -*-
"""Genereert alle HTML-pagina's van LefLiving.be op basis van content.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build import base_html, write_page, OUT, SITE_URL
from content import ARTICLES, PARTNERS, FAQ_ITEMS

AVATAR = "/images/charlotte-avatar.svg"


def artikel_kaart(a):
    return f"""
<div class="kaart">
  <div class="kaart-beeld">{a['icon']}</div>
  <div class="kaart-inhoud">
    <div class="datum">{a['date_display']}</div>
    <h3><a href="/nieuws/{a['slug']}/">{a['title']}</a></h3>
    <p>{a['excerpt']}</p>
    <a class="lees-verder" href="/nieuws/{a['slug']}/">Lees verder &rarr;</a>
  </div>
</div>"""


# ---------------------------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------------------------
def build_home():
    laatste = ARTICLES[:3]
    kaarten = "\n".join(artikel_kaart(a) for a in laatste)

    content = f"""
<div class="wrap">
  <section class="hero">
    <h1>Inspiratie en tips voor wonen en leven</h1>
    <p class="intro">LefLiving.be bundelt praktische tips en inspiratie rond interieur, sfeer en het dagelijkse leven in huis. Van een kleine ruimte optimaal inrichten tot de juiste glazen voor een mooi gedekte tafel: heldere artikelen waar je meteen iets aan hebt.</p>
    <div class="knoppen">
      <a class="btn btn-primair" href="/nieuws/">Lees het laatste nieuws</a>
      <a class="btn btn-secundair" href="/over/">Ontdek het platform</a>
    </div>
  </section>

  <section>
    <h2 class="sectie-titel">De laatste artikelen</h2>
    <p class="sectie-sub">Recent gepubliceerd op LefLiving.be</p>
    <div class="grid">
      {kaarten}
    </div>
  </section>

  <section>
    <h2 class="sectie-titel">Waarom LefLiving.be</h2>
    <p class="sectie-sub">Drie dingen waar dit platform voor staat</p>
    <div class="grid">
      <div class="kaart">
        <div class="kaart-inhoud">
          <h3>Praktisch en sfeervol</h3>
          <p>Artikelen die verder gaan dan mooie plaatjes: concrete tips die meteen toepasbaar zijn in een echt huis.</p>
        </div>
      </div>
      <div class="kaart">
        <div class="kaart-inhoud">
          <h3>Onafhankelijk opgebouwd</h3>
          <p>De inhoud vertrekt vanuit wat werkt in de praktijk, niet vanuit wat het best verkoopt. Externe links worden altijd duidelijk vermeld.</p>
        </div>
      </div>
      <div class="kaart">
        <div class="kaart-inhoud">
          <h3>Regelmatig aangevuld</h3>
          <p>Het platform groeit gestaag verder met nieuwe artikelen en een uitbreidende lijst van nuttige partnersites.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="center">
    <h2 class="sectie-titel">Nieuwsgierig naar wie hierachter zit?</h2>
    <p class="sectie-sub">Maak kennis met de schrijfster van LefLiving.be</p>
    <a class="btn btn-primair" href="/schrijfster/">Ontmoet Charlotte</a>
  </section>
</div>
"""
    html = base_html(
        title="LefLiving.be – Inspiratie en tips voor wonen en leven",
        description="Praktische tips en inspiratie over wonen en leefstijl: interieur, sfeer, klussen en het dagelijkse leven in huis.",
        canonical_path="/",
        content=content,
        active="/",
    )
    write_page("/", html)


# ---------------------------------------------------------------------------
# OVER
# ---------------------------------------------------------------------------
def build_over():
    content = """
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Over LefLiving.be</h1>
      <p class="intro">LefLiving.be is een onafhankelijk platform over wonen en leefstijl. Van een kleine ruimte slim inrichten tot de juiste sfeer creëren met verlichting: dit platform bundelt inspiratie en praktische uitleg voor wie graag met aandacht woont.</p>

      <h2>Waarom dit platform bestaat</h2>
      <p>Interieur- en leefstijlcontent online is er in overvloed, maar bestaat vaak uit mooie foto's zonder concrete uitleg. LefLiving.be probeert het anders aan te pakken: artikelen die niet alleen inspireren, maar ook uitleggen hoe je iets zelf aanpakt, praktisch en zonder overbodige omwegen.</p>

      <h2>Welke onderwerpen komen aan bod</h2>
      <p>De artikelen op dit platform bestrijken een brede waaier aan thema's rond wonen en leven, waaronder:</p>
      <ul>
        <li>Interieur en indeling</li>
        <li>Sfeer en verlichting</li>
        <li>Klussen en meubels monteren</li>
        <li>Tafelen en huishoudelijke basics</li>
        <li>Duurzaam en bewust wonen</li>
      </ul>
      <p>Deze lijst groeit mee met nieuwe artikelen. Heb je zelf een onderwerp waar je graag meer over zou lezen? Een berichtje via de <a href="/contact/">contactpagina</a> is altijd welkom.</p>

      <h2>Hoe de artikelen tot stand komen</h2>
      <p>Elk artikel vertrekt vanuit een concrete, herkenbare vraag over wonen of leven. Waar mogelijk wordt informatie aangevuld met verwijzingen naar betrouwbare, gespecialiseerde bronnen en websites, zodat lezers ook zelf verder kunnen zoeken. Op de <a href="/partners/">partnerspagina</a> staat een overzicht van websites die het platform de moeite waard vindt om te vermelden.</p>

      <h2>Wie schrijft dit allemaal</h2>
      <p>Achter LefLiving.be zit Charlotte, die met veel plezier interieur- en leefstijlonderwerpen uitzoekt en uitschrijft. Meer over haar en haar aanpak is te lezen op de <a href="/schrijfster/">pagina over de schrijfster</a>.</p>

      <h2>Vragen of opmerkingen</h2>
      <p>Voor vragen, suggesties of feedback kan altijd gemaild worden naar <a href="mailto:info@lefliving.be">info@lefliving.be</a>. Elk bericht wordt gelezen.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Over LefLiving.be – uitleg over het platform",
        description="Ontdek wat LefLiving.be is, welke onderwerpen aan bod komen en hoe de artikelen tot stand komen.",
        canonical_path="/over/",
        content=content,
        active="/over/",
    )
    write_page("/over/", html)


# ---------------------------------------------------------------------------
# SCHRIJFSTER
# ---------------------------------------------------------------------------
def build_schrijfster():
    content = f"""
<div class="wrap">
  <section>
    <div class="smal">
      <div class="schrijfster-hero">
        <img src="{AVATAR}" alt="Getekende avatar van Charlotte, schrijfster van LefLiving.be">
        <div class="tekst">
          <h1>Charlotte</h1>
          <p class="intro">De stem achter LefLiving.be</p>
        </div>
      </div>

      <h2>Over Charlotte</h2>
      <p>Charlotte schrijft met veel plezier over wonen en leefstijl: interieur, sfeer, kleine klussen in huis en alles wat een woning aangenamer maakt om in te leven. Wat haar drijft, is de combinatie van esthetiek en praktisch nut: mooi is fijn, maar het moet ook werken in een echt, bewoond huis.</p>

      <p>Voordat ze aan een artikel begint, denkt ze na over de lezer die met een concrete vraag zit: hoe richt je een kleine kamer ruimtelijker in, welk glas past bij welke drank, hoe hang je een deur weer netjes recht. Die praktische vragen vormen het uitgangspunt van elk artikel.</p>

      <h2>Haar aanpak</h2>
      <p>Charlotte houdt van heldere, toepasbare uitleg boven vage sfeerbeelden. Ze zoekt liever naar het concrete antwoord: welke keuze werkt het best, waar moet je op letten, en hoe pak je het zelf aan. Waar het kan, verwijst ze door naar gespecialiseerde bronnen en websites, zodat lezers zelf verder kunnen graven als ze dat willen.</p>

      <h2>Contact</h2>
      <p>Heb je een vraag over een artikel, een suggestie voor een nieuw onderwerp, of gewoon een opmerking? Charlotte leest alle berichten die binnenkomen via <a href="mailto:info@lefliving.be">info@lefliving.be</a>.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Charlotte – de schrijfster achter LefLiving.be",
        description="Maak kennis met Charlotte, de schrijfster van LefLiving.be, en haar aanpak bij het schrijven van artikelen over wonen en leefstijl.",
        canonical_path="/schrijfster/",
        content=content,
        active=None,
        og_image=AVATAR,
    )
    write_page("/schrijfster/", html)


# ---------------------------------------------------------------------------
# PARTNERS
# ---------------------------------------------------------------------------
def build_partners():
    items = "\n".join(
        f"""<li>
  <h3><a href="{p['url']}" target="_blank" rel="noopener">{p['naam']}</a></h3>
  <p>{p['omschrijving']}</p>
</li>"""
        for p in PARTNERS
    )
    content = f"""
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Partners en nuttige websites</h1>
      <p class="intro">Naast eigen artikelen verwijst LefLiving.be graag door naar websites die het vermelden waard zijn. Deze pagina groeit mee: op termijn komen hier ook linkpartners te staan waarmee wordt samengewerkt. Voorlopig alvast een overzicht van websites die goed aansluiten bij de onderwerpen op dit platform.</p>
    </div>
  </section>

  <section>
    <ul class="partner-lijst">
      {items}
    </ul>
  </section>

  <section>
    <div class="smal">
      <h2>Zelf een website voorstellen?</h2>
      <p>Ken je een website die goed zou passen bij dit overzicht, of ben je zelf op zoek naar een samenwerking? Een berichtje via <a href="mailto:info@lefliving.be">info@lefliving.be</a> is welkom.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Partners en nuttige websites – LefLiving.be",
        description="Een overzicht van nuttige websites en (toekomstige) linkpartners die aansluiten bij de onderwerpen op LefLiving.be.",
        canonical_path="/partners/",
        content=content,
        active="/partners/",
    )
    write_page("/partners/", html)


# ---------------------------------------------------------------------------
# NIEUWS OVERZICHT
# ---------------------------------------------------------------------------
def build_nieuws_index():
    kaarten = "\n".join(artikel_kaart(a) for a in ARTICLES)
    content = f"""
<div class="wrap">
  <section>
    <h1>Nieuws en artikelen</h1>
    <p class="intro">Alle artikelen op een rij, van interieur en sfeer tot klussen en tafelen.</p>
  </section>
  <section>
    <div class="grid">
      {kaarten}
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Nieuws – LefLiving.be",
        description="Alle artikelen van LefLiving.be op een rij: praktische tips en inspiratie over wonen en leefstijl.",
        canonical_path="/nieuws/",
        content=content,
        active="/nieuws/",
    )
    write_page("/nieuws/", html)


# ---------------------------------------------------------------------------
# NIEUWS ARTIKELEN
# ---------------------------------------------------------------------------
def build_articles():
    for a in ARTICLES:
        content = f"""
<div class="wrap">
  <article class="artikel">
    <a class="terug-link" href="/nieuws/">&larr; Terug naar overzicht</a>
    <h1>{a['title']}</h1>
    <div class="meta">
      <img class="auteur-mini" src="{AVATAR}" alt="Charlotte">
      <span>Door <a href="/schrijfster/">Charlotte</a> &middot; {a['date_display']}</span>
    </div>
    {a['body']}

    <div class="auteur-box">
      <img src="{AVATAR}" alt="Charlotte">
      <div>
        <h4>Charlotte</h4>
        <p>Schrijft op LefLiving.be over wonen en leefstijl. <a href="/schrijfster/">Meer over Charlotte</a>.</p>
      </div>
    </div>
  </article>
</div>
"""
        html = base_html(
            title=f"{a['title']} – LefLiving.be",
            description=a["meta_description"],
            canonical_path=f"/nieuws/{a['slug']}/",
            content=content,
            active="/nieuws/",
        )
        write_page(f"/nieuws/{a['slug']}/", html)


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def build_contact():
    content = """
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Contact</h1>
      <p class="intro">Een vraag, suggestie of opmerking? Een mailtje volstaat.</p>
      <div class="contact-kaart">
        <p>Er is bewust geen contactformulier op deze website. Stuur in plaats daarvan gerust een e-mail naar onderstaand adres, dat komt rechtstreeks in de mailbox terecht en wordt zo snel mogelijk gelezen.</p>
        <a class="btn btn-primair mailknop" href="mailto:info@lefliving.be">info@lefliving.be</a>
      </div>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Contact – LefLiving.be",
        description="Neem contact op met LefLiving.be via info@lefliving.be.",
        canonical_path="/contact/",
        content=content,
        active="/contact/",
    )
    write_page("/contact/", html)


# ---------------------------------------------------------------------------
# PRIVACYBELEID
# ---------------------------------------------------------------------------
def build_privacy():
    content = """
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Privacybeleid</h1>
      <p class="intro">Laatst bijgewerkt: juli 2026</p>

      <h2>Wie is verantwoordelijk</h2>
      <p>Deze website, LefLiving.be, is verantwoordelijk voor de verwerking van persoonsgegevens zoals beschreven in dit privacybeleid. Voor alle vragen hierover kan gemaild worden naar <a href="mailto:info@lefliving.be">info@lefliving.be</a>.</p>

      <h2>Welke gegevens worden verwerkt</h2>
      <p>LefLiving.be is een informatieve website zonder gebruikersaccounts, zonder contactformulier en zonder inschrijvingen. Er worden dus geen persoonsgegevens verzameld via formulieren op deze website.</p>
      <p>Wanneer je zelf een e-mail stuurt naar info@lefliving.be, worden de gegevens die je daarin meedeelt (zoals naam en e-mailadres) enkel gebruikt om je bericht te beantwoorden. Deze gegevens worden niet doorgegeven aan derden en niet langer bewaard dan nodig voor de afhandeling van je vraag.</p>

      <h2>Technische gegevens via hosting</h2>
      <p>Deze website wordt gehost via Cloudflare Pages. Zoals bij vrijwel elke website worden daarbij automatisch technische gegevens verwerkt die nodig zijn om de website te laten werken en te beveiligen, zoals IP-adres, browsertype en tijdstip van een bezoek. Deze gegevens worden verwerkt door de hostingpartij in het kader van de goede werking en beveiliging van de website, en niet gebruikt voor het opstellen van bezoekersprofielen door LefLiving.be zelf.</p>
      <p>Op dit moment maakt LefLiving.be geen gebruik van eigen analytics- of trackingtools. Mocht dat in de toekomst veranderen, dan wordt dit privacybeleid daarop aangepast.</p>

      <h2>Jouw rechten</h2>
      <p>Je hebt het recht om te vragen welke gegevens over jou verwerkt worden, om deze te laten verbeteren of verwijderen, en om bezwaar te maken tegen de verwerking ervan. Een verzoek hiertoe kan gestuurd worden naar <a href="mailto:info@lefliving.be">info@lefliving.be</a>.</p>

      <h2>Klachten</h2>
      <p>Ben je niet tevreden over hoe met jouw gegevens wordt omgegaan, dan kan je terecht bij de Belgische Gegevensbeschermingsautoriteit via <a href="https://www.gegevensbeschermingsautoriteit.be" target="_blank" rel="noopener">gegevensbeschermingsautoriteit.be</a>.</p>

      <h2>Wijzigingen</h2>
      <p>Dit privacybeleid kan van tijd tot tijd worden aangepast, bijvoorbeeld wanneer de website nieuwe functionaliteiten krijgt. De datum bovenaan deze pagina geeft aan wanneer het beleid voor het laatst werd bijgewerkt.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Privacybeleid – LefLiving.be",
        description="Lees hoe LefLiving.be omgaat met persoonsgegevens en welke rechten je hebt.",
        canonical_path="/privacybeleid/",
        content=content,
        active=None,
    )
    write_page("/privacybeleid/", html)


# ---------------------------------------------------------------------------
# COOKIEBELEID
# ---------------------------------------------------------------------------
def build_cookies():
    content = """
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Cookiebeleid</h1>
      <p class="intro">Laatst bijgewerkt: juli 2026</p>

      <h2>Gebruikt deze website cookies?</h2>
      <p>LefLiving.be maakt op dit moment geen gebruik van tracking-, marketing- of analyticscookies. Er worden geen cookies geplaatst om je surfgedrag te volgen of om je op andere websites gerichte advertenties te tonen.</p>

      <h2>Technische cookies via hosting</h2>
      <p>Deze website wordt gehost via Cloudflare Pages. Zoals bij de meeste moderne hostingdiensten kunnen daarbij louter technische, functionele cookies of vergelijkbare technieken gebruikt worden die noodzakelijk zijn voor de beveiliging en goede werking van de website (bijvoorbeeld bescherming tegen misbruik). Deze technische cookies verzamelen geen persoonlijke surfgeschiedenis en worden niet gebruikt voor marketingdoeleinden.</p>

      <h2>Externe links</h2>
      <p>Artikelen op deze website bevatten soms links naar externe websites, bijvoorbeeld webshops die relevant zijn voor het onderwerp. Eenmaal je op zo'n link klikt en de externe website bezoekt, geldt het cookiebeleid van die website, niet van LefLiving.be.</p>

      <h2>Toekomstige wijzigingen</h2>
      <p>Mocht LefLiving.be in de toekomst alsnog analytics- of marketingcookies gaan gebruiken, dan wordt daarvoor eerst toestemming gevraagd waar dat wettelijk vereist is, en wordt dit cookiebeleid dienovereenkomstig aangepast.</p>

      <h2>Vragen</h2>
      <p>Vragen over dit cookiebeleid kunnen gemaild worden naar <a href="mailto:info@lefliving.be">info@lefliving.be</a>.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Cookiebeleid – LefLiving.be",
        description="Lees welke cookies LefLiving.be wel en niet gebruikt.",
        canonical_path="/cookiebeleid/",
        content=content,
        active=None,
    )
    write_page("/cookiebeleid/", html)


# ---------------------------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------------------------
def build_disclaimer():
    content = """
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Disclaimer</h1>
      <p class="intro">Laatst bijgewerkt: juli 2026</p>

      <h2>Algemene informatie</h2>
      <p>De artikelen op LefLiving.be zijn met zorg samengesteld en bedoeld als algemene, praktische informatie en inspiratie rond wonen en leefstijl. Ze vormen geen vervanging voor professioneel advies, bijvoorbeeld van een interieurarchitect, aannemer of andere specialist. Bij twijfel over de veiligheid of haalbaarheid van een klus of aanpassing, raadpleeg je best een deskundige.</p>

      <h2>Geen garantie op juistheid of volledigheid</h2>
      <p>Ondanks de zorg die aan elk artikel wordt besteed, kan LefLiving.be niet garanderen dat alle informatie op elk moment volledig, actueel of foutloos is. Situaties, producten en regelgeving kunnen wijzigen. Gebruik van de informatie op deze website gebeurt op eigen verantwoordelijkheid.</p>

      <h2>Aansprakelijkheid</h2>
      <p>LefLiving.be is niet aansprakelijk voor schade, van welke aard dan ook, die zou voortvloeien uit het gebruik van de informatie op deze website, of uit het toepassen van tips of adviezen uit de artikelen.</p>

      <h2>Externe links en partnerlinks</h2>
      <p>Deze website bevat links naar externe websites, waaronder webshops en informatieve bronnen. Deze links worden aangeboden ter aanvulling en zijn geen garantie voor de juistheid, veiligheid of betrouwbaarheid van de inhoud op die externe websites. LefLiving.be heeft geen controle over de inhoud van externe websites en is daar niet verantwoordelijk voor.</p>
      <p>Sommige links in artikelen zijn partner- of affiliatelinks. Dat betekent dat LefLiving.be in bepaalde gevallen een vergoeding kan ontvangen wanneer via zo'n link een aankoop wordt gedaan. Dit heeft geen invloed op de prijs die je als bezoeker betaalt, en geen invloed op de onafhankelijkheid van de redactionele inhoud. Waar van toepassing wordt dit ook rechtstreeks in het artikel vermeld.</p>

      <h2>Vragen</h2>
      <p>Vragen over deze disclaimer kunnen gemaild worden naar <a href="mailto:info@lefliving.be">info@lefliving.be</a>.</p>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Disclaimer – LefLiving.be",
        description="Lees de disclaimer van LefLiving.be over aansprakelijkheid, externe links en partnerlinks.",
        canonical_path="/disclaimer/",
        content=content,
        active=None,
    )
    write_page("/disclaimer/", html)


# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------
def build_faq():
    items = "\n".join(
        f"""<div class="faq-item">
  <h3>{item['vraag']}</h3>
  <p>{item['antwoord']}</p>
</div>"""
        for item in FAQ_ITEMS
    )
    content = f"""
<div class="wrap">
  <section>
    <div class="smal">
      <h1>Veelgestelde vragen</h1>
      <p class="intro">Een antwoord op de meest gestelde vragen over LefLiving.be.</p>
      {items}
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Veelgestelde vragen – LefLiving.be",
        description="Antwoorden op veelgestelde vragen over LefLiving.be, de inhoud en hoe je contact opneemt.",
        canonical_path="/faq/",
        content=content,
        active=None,
    )
    write_page("/faq/", html)


# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------
def build_404():
    content = """
<div class="wrap">
  <section class="center">
    <h1>Pagina niet gevonden</h1>
    <p class="intro">Deze pagina bestaat niet (meer). Mogelijk is de link verouderd of verkeerd getypt.</p>
    <div class="knoppen center" style="justify-content:center;">
      <a class="btn btn-primair" href="/">Terug naar de homepage</a>
      <a class="btn btn-secundair" href="/nieuws/">Bekijk het nieuws</a>
    </div>
  </section>
</div>
"""
    html = base_html(
        title="Pagina niet gevonden – LefLiving.be",
        description="Deze pagina bestaat niet (meer).",
        canonical_path="/404.html",
        content=content,
        active=None,
    )
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# SITEMAP & ROBOTS
# ---------------------------------------------------------------------------
def build_sitemap_robots():
    paths = ["/", "/over/", "/schrijfster/", "/partners/", "/nieuws/", "/contact/",
             "/privacybeleid/", "/cookiebeleid/", "/disclaimer/", "/faq/"]
    paths += [f"/nieuws/{a['slug']}/" for a in ARTICLES]

    urls = "\n".join(
        f"  <url><loc>{SITE_URL}{p}</loc></url>" for p in paths
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)


def build_all():
    build_home()
    build_over()
    build_schrijfster()
    build_partners()
    build_nieuws_index()
    build_articles()
    build_contact()
    build_privacy()
    build_cookies()
    build_disclaimer()
    build_faq()
    build_404()
    build_sitemap_robots()


if __name__ == "__main__":
    build_all()
    print("Site gegenereerd in site/")
