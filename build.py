#!/usr/bin/env python3
"""Costruisce index.html a partire da progetti.py.

    python3 build.py             # solo le schede scritte a mano
    python3 build.py --github    # più stelle, contatori e repository recenti presi da GitHub
    python3 build.py --offline   # come --github, ma da repository.json senza scaricare

Il sito è una pagina sola, senza dipendenze: il testo c'è in italiano e in inglese
e si scambia con il CSS, così funziona anche se JavaScript è spento. L'action `pagina`
lo costruisce con `--github` e lo pubblica: un repository nuovo compare da solo.
"""

import argparse
import html
import json
import math
import os
import pathlib

import repository_github
from progetti import ESCLUSI, STRATI

RADICE = pathlib.Path(__file__).parent
UTENTE = "enzococca"
EMAIL = "enzo.ccc@gmail.com"

# I quattro numeri dell'apertura: (valore_it, valore_en, etichetta_it, etichetta_en).
# Sono controllati a mano — se li cambi, controlla che siano ancora veri.
#   2.146  commit su pyarchinit/pyarchinit (primo contributore, agosto 2026)
#   133    repository pubblici sul profilo
#   2013   iscritto a GitHub il 4 febbraio
#   18+    repository con un metadata.txt di plugin, esclusi doppioni e versioni vecchie
NUMERI = [
    ("2.146", "2,146", "commit su pyArchInit", "commits on pyArchInit"),
    ("133", "133", "repository pubblici", "public repositories"),
    ("2013", "2013", "su GitHub dal", "on GitHub since"),
    ("18+", "18+", "plugin QGIS e QField", "QGIS and QField plugins"),
]


def e(t):
    return html.escape(t, quote=True)


def due_lingue(it, en, tag="span", cls=""):
    """Lo stesso testo nelle due lingue: ne resta visibile una sola."""
    c = f' class="{cls}"' if cls else ""
    return (f'<{tag} lang="it" data-lingua="it"{c}>{it}</{tag}>'
            f'<{tag} lang="en" data-lingua="en"{c}>{en}</{tag}>')


# I tag scritti in italiano in progetti.py e la loro resa inglese. Quelli che non
# compaiono qui (QGIS, PostGIS, DJI, 3D…) restano identici nelle due lingue.
TRADUZIONE_TAG = {
    "stratigrafia": "stratigraphy",
    "campo": "field",
    "documentazione": "documentation",
    "stazione totale": "total station",
    "seriale": "serial",
    "profili": "profiles",
    "muri": "walls",
    "ricognizione": "survey",
    "multipiattaforma": "multiplatform",
    "missioni": "missions",
    "paesaggio": "landscape",
    "bayesiano": "Bayesian",
    "teoria": "theory",
    "tipologia": "typology",
    "museo": "museum",
    "catalogo": "catalogue",
    "morfometria": "morphometry",
    "Età del Bronzo": "Bronze Age",
    "archeozoologia": "zooarchaeology",
    "relitti": "shipwrecks",
    "arte rupestre": "rock art",
    "mappa": "map",
    "linguistica": "linguistics",
    "telerilevamento": "remote sensing",
    "multilingua": "multilingual",
    "agenti": "agents",
    "ricerca semantica": "semantic search",
    # etichette delle schede automatiche (repository_github.VOCABOLARIO)
    "rimontaggi": "refitting",
    "analisi spaziale": "spatial analysis",
    "ceramica": "pottery",
    "litica": "lithics",
    "fotogrammetria": "photogrammetry",
    "ortofoto": "orthophoto",
    "ricevute": "receipts",
    "installer": "installer",
}


def etichetta_tag(t):
    """Un tag: una sola forma se vale in tutte e due le lingue, altrimenti due."""
    inglese = TRADUZIONE_TAG.get(t)
    if inglese is None or inglese == t:
        return e(t)
    return due_lingue(e(t), e(inglese))


def sfondo_stratigrafico(larghezza=1200, altezza=440, strati=9, seme=7):
    """Sezione di scavo disegnata a mano: linee irregolari ma sempre uguali.

    Niente random: una somma di seni con numeri primi dà una linea che sembra
    tracciata a matita e non cambia a ogni build.
    """
    percorsi = []
    for i in range(strati):
        base = altezza * (i + 1) / (strati + 1)
        punti = []
        for x in range(0, larghezza + 1, 24):
            t = x / larghezza * math.pi * 2
            y = (base
                 + 11 * math.sin(t * (1.7 + i * 0.31) + i * seme)
                 + 6 * math.sin(t * (3.3 + i * 0.17) + i * 2.1)
                 + 3 * math.sin(t * 7.1 + i))
            punti.append(f"{x},{y:.1f}")
        percorsi.append(f'<polyline points="{" ".join(punti)}" />')
    return ('<svg class="sezione" viewBox="0 0 %d %d" preserveAspectRatio="none" '
            'aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
            'stroke-width="1.1" stroke-linecap="round">%s</g></svg>'
            % (larghezza, altezza, "".join(percorsi)))


def scheda(p):
    privato = p["privato"]
    titolo = e(p["nome"])
    if p["url"]:
        testa = f'<a class="scheda-titolo" href="{e(p["url"])}">{titolo}</a>'
    else:
        testa = f'<span class="scheda-titolo">{titolo}</span>'

    distintivo = ""
    if privato:
        distintivo = ('<span class="distintivo" title="repository privato">'
                      + due_lingue("Privato", "Private") + "</span>")

    tag = "".join(f'<li>{etichetta_tag(t)}</li>' for t in p["tag"])
    piede = []
    if p["url"]:
        piede.append(f'<a href="{e(p["url"])}">{due_lingue("Codice", "Code")}</a>')
    if p["extra"]:
        et_it, et_en, url = p["extra"]
        piede.append(f'<a href="{e(url)}">{due_lingue(e(et_it), e(et_en))}</a>')
    piede_html = f'<div class="scheda-piede">{"".join(piede)}</div>' if piede else ""

    return f"""        <article class="scheda{' scheda-privata' if privato else ''}">
          <header><h3>{testa}</h3>{distintivo}</header>
          <p class="meta">{e(p["meta"])}</p>
          {due_lingue(e(p["it"]), e(p["en"]), tag="p", cls="descrizione")}
          <ul class="tag">{tag}</ul>
          {piede_html}
        </article>"""


def strato(s):
    schede = "\n".join(scheda(p) for p in s["progetti"])
    etichetta = due_lingue(f'US&nbsp;{s["num"]}', f'SU&nbsp;{s["num"]}', cls="numero")
    return f"""    <section class="strato" id="s{s['num']}">
      <div class="strato-testa">
        {etichetta}
        <h2>{due_lingue(e(s["titolo_it"]), e(s["titolo_en"]))}</h2>
        {due_lingue(e(s["intro_it"]), e(s["intro_en"]), tag="p", cls="strato-intro")}
      </div>
      <div class="griglia">
{schede}
      </div>
    </section>"""


def numeri():
    voci = []
    for v_it, v_en, et_it, et_en in NUMERI:
        valore = e(v_it) if v_it == v_en else due_lingue(e(v_it), e(v_en))
        voci.append(f"<li><b>{valore}</b><span>{due_lingue(e(et_it), e(et_en))}</span></li>")
    return "\n      ".join(voci)


def indice():
    voci = []
    for s in STRATI:
        voci.append(f'<li><a href="#s{s["num"]}">'
                    f'<span class="indice-num">{s["num"]}</span>'
                    f'{due_lingue(e(s["titolo_it"]), e(s["titolo_en"]))}</a></li>')
    return "\n        ".join(voci)


CSS = """
:root {
  --sfondo:   #FAFAF8;
  --superficie: #FFFFFF;
  --inchiostro: #14181B;
  --smorzato: #5B666E;
  --linea:    #E2E4E0;
  --accento:  #1F4E5F;
  --ocra:     #8A5D1E;
  --ombra:    0 1px 2px rgba(20,24,27,.05), 0 8px 24px -16px rgba(20,24,27,.28);
  --sezione-opacita: .09;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-tema="chiaro"]) {
    --sfondo:   #0F1316;
    --superficie: #171C20;
    --inchiostro: #E9EDEF;
    --smorzato: #94A1A8;
    --linea:    #262D32;
    --accento:  #79C6BA;
    --ocra:     #D0A05A;
    --ombra:    0 1px 2px rgba(0,0,0,.4), 0 10px 28px -18px rgba(0,0,0,.9);
    --sezione-opacita: .14;
  }
}
:root[data-tema="scuro"] {
  --sfondo:   #0F1316;
  --superficie: #171C20;
  --inchiostro: #E9EDEF;
  --smorzato: #94A1A8;
  --linea:    #262D32;
  --accento:  #79C6BA;
  --ocra:     #D0A05A;
  --ombra:    0 1px 2px rgba(0,0,0,.4), 0 10px 28px -18px rgba(0,0,0,.9);
  --sezione-opacita: .14;
}

*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  * { animation: none !important; transition: none !important; }
}
body {
  margin: 0;
  background: var(--sfondo);
  color: var(--inchiostro);
  font-family: "Public Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 17px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3 {
  font-family: Newsreader, ui-serif, Georgia, "Times New Roman", serif;
  font-weight: 500;
  text-wrap: balance;
  margin: 0;
  letter-spacing: -.012em;
}
a { color: inherit; }
img { max-width: 100%; }

/* --- la lingua: ne resta visibile una sola --- */
html[lang="it"] [data-lingua="en"],
html[lang="en"] [data-lingua="it"] { display: none; }

.contenitore { width: min(1120px, 100% - 2.5rem); margin-inline: auto; }

/* --- barra --- */
.barra {
  position: sticky; top: 0; z-index: 20;
  background: color-mix(in srgb, var(--sfondo) 88%, transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--linea);
}
.barra .contenitore {
  display: flex; align-items: center; gap: 1rem;
  min-height: 58px;
}
.marchio {
  font-family: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: .8rem; letter-spacing: .1em; text-transform: uppercase;
  text-decoration: none; color: var(--smorzato); margin-right: auto;
}
.marchio b { color: var(--inchiostro); font-weight: 600; }
.comandi { display: flex; gap: .4rem; }
.comandi button, .comandi a {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .74rem; letter-spacing: .06em;
  background: transparent; color: var(--smorzato);
  border: 1px solid var(--linea); border-radius: 999px;
  padding: .34rem .74rem; cursor: pointer; text-decoration: none;
  transition: color .15s, border-color .15s;
}
.comandi button:hover, .comandi a:hover,
.comandi button:focus-visible, .comandi a:focus-visible {
  color: var(--accento); border-color: var(--accento);
}

/* --- apertura --- */
.apertura { position: relative; overflow: hidden; padding: 4.5rem 0 3.2rem; }
.sezione {
  position: absolute; inset: auto 0 0 0; width: 100%; height: 62%;
  color: var(--accento); opacity: var(--sezione-opacita);
  pointer-events: none;
  mask-image: linear-gradient(to top, #000 30%, transparent);
  -webkit-mask-image: linear-gradient(to top, #000 30%, transparent);
}
.apertura .contenitore { position: relative; }
.ritratto {
  width: 84px; height: 84px; border-radius: 50%;
  border: 1px solid var(--linea); margin-bottom: 1.4rem; display: block;
}
.apertura h1 { font-size: clamp(2.5rem, 6vw, 4rem); line-height: 1.04; }
.ruolo {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .82rem; letter-spacing: .12em; text-transform: uppercase;
  color: var(--accento); margin: .9rem 0 1.5rem;
}
.sommario { max-width: 62ch; font-size: 1.12rem; color: var(--smorzato); margin: 0 0 1rem; }
.sommario strong { color: var(--inchiostro); font-weight: 600; }
.numeri {
  display: flex; flex-wrap: wrap; gap: 2.2rem;
  margin: 2.2rem 0 0; padding: 0; list-style: none;
}
.numeri b {
  display: block;
  font-family: Newsreader, ui-serif, Georgia, serif;
  font-size: 2rem; font-weight: 500; line-height: 1.1;
  font-variant-numeric: tabular-nums;
}
.numeri li > span {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .7rem; letter-spacing: .1em; text-transform: uppercase; color: var(--smorzato);
}

/* --- indice --- */
.indice { border-top: 1px solid var(--linea); padding: 2rem 0 0; }
.indice ol {
  list-style: none; margin: 0; padding: 0;
  display: grid; gap: .1rem 2rem;
  grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
}
.indice a {
  display: flex; gap: .8rem; align-items: baseline;
  text-decoration: none; padding: .42rem 0;
  border-bottom: 1px solid transparent;
}
.indice a:hover, .indice a:focus-visible { color: var(--accento); border-bottom-color: var(--linea); }
.indice-num {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .74rem; color: var(--smorzato); font-variant-numeric: tabular-nums;
}

/* --- strati --- */
.strato { padding: 3.6rem 0 1rem; border-top: 1px solid var(--linea); margin-top: 3.2rem; }
.strato-testa { max-width: 68ch; margin-bottom: 2.2rem; }
.numero {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .72rem; letter-spacing: .16em;
  color: var(--ocra); display: block; margin-bottom: .7rem;
}
.strato h2 { font-size: clamp(1.7rem, 3.4vw, 2.35rem); }
.strato-intro { color: var(--smorzato); margin: .8rem 0 0; }

.griglia {
  display: grid; gap: 1.1rem;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
}
.scheda {
  background: var(--superficie);
  border: 1px solid var(--linea);
  border-radius: 12px;
  padding: 1.35rem 1.4rem 1.15rem;
  display: flex; flex-direction: column; gap: .62rem;
  box-shadow: var(--ombra);
  transition: border-color .16s, transform .16s;
}
.scheda:hover { border-color: color-mix(in srgb, var(--accento) 45%, var(--linea)); }
.scheda header { display: flex; align-items: flex-start; gap: .7rem; }
.scheda h3 { font-size: 1.24rem; flex: 1; }
.scheda-titolo { text-decoration: none; }
.scheda-titolo[href]:hover, .scheda-titolo[href]:focus-visible {
  color: var(--accento); text-decoration: underline; text-underline-offset: 3px;
}
.scheda-privata { border-style: dashed; }
.distintivo {
  flex: none;
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .62rem; letter-spacing: .1em; text-transform: uppercase;
  color: var(--ocra); border: 1px solid color-mix(in srgb, var(--ocra) 45%, transparent);
  border-radius: 999px; padding: .16rem .55rem; white-space: nowrap; margin-top: .18rem;
}
.meta {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .7rem; color: var(--smorzato); margin: 0; line-height: 1.5;
}
.descrizione { margin: 0; font-size: .96rem; }
.tag { list-style: none; display: flex; flex-wrap: wrap; gap: .34rem; margin: .15rem 0 0; padding: 0; }
.tag li {
  font-size: .7rem; color: var(--smorzato);
  border: 1px solid var(--linea); border-radius: 5px; padding: .1rem .44rem;
}
.scheda-piede { display: flex; gap: 1.1rem; margin-top: auto; padding-top: .5rem; }
.scheda-piede a {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .72rem; color: var(--accento); text-decoration: none;
}
.scheda-piede a::after { content: " \\2192"; }
.scheda-piede a:hover, .scheda-piede a:focus-visible { text-decoration: underline; text-underline-offset: 3px; }

/* --- chiusura --- */
.chiusura { border-top: 1px solid var(--linea); margin-top: 4rem; padding: 3rem 0 4rem; }
.chiusura p { max-width: 62ch; color: var(--smorzato); }
.chiusura .collegamenti { display: flex; flex-wrap: wrap; gap: 1.4rem; margin-top: 1.4rem; }
.chiusura .collegamenti a {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: .78rem; color: var(--accento); text-decoration: none;
}
.chiusura .collegamenti a:hover { text-decoration: underline; text-underline-offset: 3px; }
.piccolo { font-size: .78rem; margin-top: 2rem; }

:focus-visible { outline: 2px solid var(--accento); outline-offset: 3px; border-radius: 3px; }
@media (max-width: 620px) {
  body { font-size: 16px; }
  .apertura { padding-top: 3rem; }
  .numeri { gap: 1.5rem; }
  .griglia { grid-template-columns: 1fr; }
}
"""

JS = """
(function () {
  var r = document.documentElement;

  function lingua(l) {
    r.setAttribute("lang", l);
    try { localStorage.setItem("lingua", l); } catch (e) {}
    var b = document.getElementById("cambia-lingua");
    b.textContent = l === "it" ? "English" : "Italiano";
    b.setAttribute("aria-label", l === "it" ? "Switch to English" : "Passa all'italiano");
  }

  function tema(t) {
    r.setAttribute("data-tema", t);
    try { localStorage.setItem("tema", t); } catch (e) {}
    document.getElementById("cambia-tema").textContent = t === "scuro" ? "\\u25CB" : "\\u25CF";
  }

  var l = null, t = null;
  try { l = localStorage.getItem("lingua"); t = localStorage.getItem("tema"); } catch (e) {}
  if (!l) l = (navigator.language || "en").toLowerCase().indexOf("it") === 0 ? "it" : "en";
  if (!t) t = matchMedia("(prefers-color-scheme: dark)").matches ? "scuro" : "chiaro";
  lingua(l); tema(t);

  document.getElementById("cambia-lingua").addEventListener("click", function () {
    lingua(r.getAttribute("lang") === "it" ? "en" : "it");
  });
  document.getElementById("cambia-tema").addEventListener("click", function () {
    tema(r.getAttribute("data-tema") === "scuro" ? "chiaro" : "scuro");
  });
})();
"""


def costruisci():
    pagina = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Enzo Cocca — Archaeology &amp; Software</title>
<meta name="description" content="Archaeologist and developer. Lead developer of pyArchInit; field tools for excavation recording, photogrammetry, spatial analysis and underwater archaeology. Italiano / English.">
<meta property="og:title" content="Enzo Cocca — Archaeology &amp; Software">
<meta property="og:description" content="Field tools for archaeology: pyArchInit, Photo3D, QGIS plugins, mobile field apps.">
<meta property="og:type" content="profile">
<meta property="og:url" content="https://{UTENTE}.github.io/">
<meta property="og:image" content="https://avatars.githubusercontent.com/{UTENTE}">
<meta name="theme-color" content="#0F1316" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#FAFAF8" media="(prefers-color-scheme: light)">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='26'>%F0%9F%8F%BA</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Public+Sans:wght@400;600&display=swap">
<style>{CSS}</style>
</head>
<body>

<nav class="barra">
  <div class="contenitore">
    <a class="marchio" href="#"><b>Enzo Cocca</b> — {due_lingue("archeologia &amp; software", "archaeology &amp; software")}</a>
    <div class="comandi">
      <button id="cambia-lingua" type="button">Italiano</button>
      <button id="cambia-tema" type="button" aria-label="Tema chiaro / scuro" title="Tema · Theme">&#9679;</button>
      <a href="https://github.com/{UTENTE}">GitHub</a>
    </div>
  </div>
</nav>

<header class="apertura">
  {sfondo_stratigrafico()}
  <div class="contenitore">
    <img class="ritratto" src="https://avatars.githubusercontent.com/{UTENTE}" alt="Enzo Cocca" width="84" height="84" loading="lazy">
    <h1>{due_lingue("Archeologia,<br>scritta in codice", "Archaeology,<br>written in code")}</h1>
    <p class="ruolo">{due_lingue("Archeologo e sviluppatore", "Archaeologist and developer")}</p>
    {due_lingue(
      "Costruisco gli strumenti che poi uso in trincea. Sono lo <strong>sviluppatore "
      "principale di pyArchInit</strong>, il sistema libero di documentazione archeologica per "
      "QGIS, e intorno a quello è cresciuto tutto il resto: fotogrammetria da telefono e da "
      "drone, app che funzionano offline sotto il sole, analisi spaziale, banche dati per "
      "scavi subacquei e archivi che nessuno riusciva più a consultare. "
      "Tutto libero o autoinstallabile: i dati di scavo restano di chi scava.",
      "I build the tools I then use in the trench. I am the <strong>lead developer of "
      "pyArchInit</strong>, the free archaeological recording system for QGIS, and everything "
      "else grew around it: photogrammetry from phone and drone, apps that work offline under "
      "the sun, spatial analysis, databases for underwater excavations and archives nobody "
      "could search any more. "
      "All of it open or self-hosted: excavation data stays with the people who dig it.",
      tag="p", cls="sommario")}
    <ul class="numeri">
      {numeri()}
    </ul>
  </div>
</header>

<main>
  <nav class="indice contenitore" aria-label="Indice · Contents">
    <ol>
        {indice()}
    </ol>
  </nav>

  <div class="contenitore">
{chr(10).join(strato(s) for s in STRATI)}
  </div>
</main>

<footer class="chiusura">
  <div class="contenitore">
    <h2>{due_lingue("Parliamone", "Get in touch")}</h2>
    {due_lingue(
      "Se uno di questi strumenti ti serve, se vuoi contribuire o se hai uno scavo da "
      "documentare e non sai da che parte cominciare, scrivimi: quasi tutto quello che c'è qui "
      "è nato da una richiesta arrivata dal campo. Per i problemi su un progetto preciso "
      "conviene aprire una issue sul suo repository, così la discussione resta dov'è utile.",
      "If one of these tools would help you, if you want to contribute, or if you have an "
      "excavation to record and no idea where to start, write to me: nearly everything here "
      "started as a request that came in from the field. For a problem with one particular "
      "project an issue on its repository works better — the discussion stays where it helps.",
      tag="p")}
    <div class="collegamenti">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="https://github.com/{UTENTE}">github.com/{UTENTE}</a>
      <a href="https://github.com/pyarchinit/pyarchinit">pyArchInit</a>
      <a href="https://{UTENTE}.github.io/photo3d-guida">{due_lingue("Guida Photo3D", "Photo3D guide")}</a>
    </div>
    {due_lingue(
      "I progetti segnati come <em>Privati</em> sono in sviluppo o non ancora pubblicati: "
      "il codice non è accessibile, ma volentieri ne parlo.",
      "Projects marked <em>Private</em> are in development or not published yet: the code is "
      "not accessible, but I am happy to talk about them.",
      tag="p", cls="piccolo")}
  </div>
</footer>

<script>{JS}</script>
</body>
</html>
"""
    (RADICE / "index.html").write_text(pagina, encoding="utf-8")
    schede = sum(len(s["progetti"]) for s in STRATI)
    print(f"index.html scritto — {len(STRATI)} strati, {schede} progetti")


def aggiorna_numeri(dati):
    """I contatori dell'apertura che GitHub conosce: repository pubblici e commit su pyArchInit."""
    for i, (v_it, v_en, et_it, et_en) in enumerate(NUMERI):
        if et_en == "public repositories" and dati.get("repository_pubblici"):
            n = str(dati["repository_pubblici"])
            NUMERI[i] = (n, n, et_it, et_en)
        if et_en == "commits on pyArchInit" and dati.get("commit_pyarchinit"):
            n = dati["commit_pyarchinit"]
            NUMERI[i] = (f"{n:,}".replace(",", "."), f"{n:,}", et_it, et_en)


def main(argv=None):
    p = argparse.ArgumentParser(description="Costruisce index.html da progetti.py.")
    p.add_argument("--github", action="store_true",
                   help="scarica da GitHub stelle, contatori e repository recenti (GITHUB_TOKEN se c'è) e li salva in repository.json")
    p.add_argument("--offline", action="store_true", help="usa repository.json senza scaricare")
    a = p.parse_args(argv)
    cache = RADICE / "repository.json"
    token = os.environ.get("GITHUB_TOKEN") or None
    dati = None
    if a.github:
        dati = repository_github.scarica(UTENTE, token)
        cache.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")
    elif a.offline and cache.exists():
        dati = json.loads(cache.read_text(encoding="utf-8"))
    if dati:
        repository_github.aggiorna_stelle(STRATI, dati)
        conosciuti = [q["url"] for s in STRATI for q in s["progetti"]]
        schede = repository_github.automatici(dati, conosciuti, ESCLUSI, UTENTE, token if a.github else None)
        if schede:
            STRATI.append(repository_github.strato_automatico(schede, f"{len(STRATI) + 1:02d}"))
        aggiorna_numeri(dati)
    costruisci()


if __name__ == "__main__":
    main()
