"""I repository pubblici di GitHub: le stelle e i contatori aggiornati per la pagina e una scheda
automatica per ogni repository recente che non ha ancora una scheda scritta a mano.

`python3 build.py --github` li scarica (con GITHUB_TOKEN se c'è nell'ambiente, altrimenti senza:
bastano poche richieste) e li conserva in `repository.json`; `--offline` rilegge quel file.
L'action `pagina` fa la stessa cosa a ogni push, ogni ora e a richiesta: un repository nuovo
compare da solo, con nome e descrizione presi da GitHub, finché non gli scrivi la sua scheda in
`progetti.py` (allora esce dalla lista automatica) o non lo metti fra gli `ESCLUSI`.
"""
import base64
import datetime as dt
import json
import re
import urllib.request

API = "https://api.github.com"
MESI = 12       # un repository entra da solo se è stato toccato negli ultimi dodici mesi
MASSIMO = 12    # schede automatiche al massimo, dalle più recenti

# Parole che diventano etichette quando compaiono nel nome o nella descrizione di un repository
# senza topic su GitHub: (espressione, etichetta), dalle più specifiche alle più generiche. Le
# etichette in italiano le traduce TRADUZIONE_TAG di build.py.
VOCABOLARIO = [
    (r"rimontagg|\brefit", "rimontaggi"),
    (r"analisi spaziale|spatial analys", "analisi spaziale"),
    (r"ceramic|pottery", "ceramica"),
    (r"\blitic|lithic", "litica"),
    (r"stratigraf|matrix di harris|harris matrix", "stratigrafia"),
    (r"photogrammetr|fotogrammetr", "fotogrammetria"),
    (r"\bortho|ortofoto", "ortofoto"),
    (r"\bdem\b|\bdsm\b|elevation|\bquote\b", "DEM"),
    (r"\blidar\b", "LiDAR"),
    (r"\bdrone|\bdji\b|\buav\b", "drone"),
    (r"least.?cost|movecost", "least-cost path"),
    (r"\bqgis\b", "QGIS"),
    (r"\bqfield\b", "QField"),
    (r"\bpostgis\b", "PostGIS"),
    (r"\bspatialite\b", "SpatiaLite"),
    (r"\bpyarchinit\b", "pyArchInit"),
    (r"photo3d", "Photo3D"),
    (r"\bgeolibre\b", "GeoLibre"),
    (r"\bmetashape\b", "Metashape"),
    (r"webodm|\bodm\b", "WebODM"),
    (r"\bpycharm\b|intellij", "PyCharm"),
    (r"\bmongodb\b", "MongoDB"),
    (r"\bkafka\b", "Kafka"),
    (r"\bocr\b", "OCR"),
    (r"\bai\b|ai-powered|intelligenza artificiale|\bllm\b|\bgpt\b", "AI"),
    (r"ricevut|scontrin|receipt", "ricevute"),
    (r"\bmuse", "museo"),
    (r"\bexcel\b|\bxlsx\b", "Excel"),
    (r"\bsql\b|database|banca dati|duckdb", "database"),
    (r"\bandroid\b|\bapk\b", "Android"),
    (r"\bios\b|swiftui|iphone|ipad", "iOS"),
    (r"\bplugin\b", "plugin"),
    (r"\binstall", "installer"),
    (r"privacy", "privacy"),
    (r"\bweb\b|\bhtml\b|browser|\bsito\b|website", "web"),
]


def _chiedi(url, token=None):
    intestazioni = {"Accept": "application/vnd.github+json", "User-Agent": "enzococca.github.io"}
    if token:
        intestazioni["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=intestazioni), timeout=30) as r:
        return json.load(r), r.headers


def _pagine(url, token=None):
    while url:
        dati, intestazioni = _chiedi(url, token)
        yield from dati
        m = re.search(r'<([^>]+)>;\s*rel="next"', intestazioni.get("Link") or "")
        url = m.group(1) if m else None


def scarica(utente, token=None):
    """Repository pubblici (non fork), numero dei repository pubblici e commit su pyArchInit, in
    un dizionario serializzabile."""
    repository = []
    for r in _pagine(f"{API}/users/{utente}/repos?per_page=100&type=owner", token):
        if r.get("fork"):
            continue
        licenza = (r.get("license") or {}).get("spdx_id") or ""
        repository.append({
            "nome": r["name"], "url": r["html_url"], "descrizione": r.get("description") or "",
            "linguaggio": r.get("language") or "", "licenza": "" if licenza == "NOASSERTION" else licenza,
            "stelle": int(r.get("stargazers_count") or 0), "topics": list(r.get("topics") or []),
            "sito": r.get("homepage") or "", "archiviato": bool(r.get("archived")),
            "creato": r["created_at"][:10], "aggiornato": (r.get("pushed_at") or r["updated_at"])[:10],
        })
    profilo, _ = _chiedi(f"{API}/users/{utente}", token)
    commit = None
    try:
        for c in _pagine(f"{API}/repos/pyarchinit/pyarchinit/contributors?per_page=100", token):
            if c.get("login") == utente:
                commit = int(c["contributions"])
    except Exception:  # il contatore resta quello scritto a mano
        pass
    return {"scaricato": dt.date.today().isoformat(), "repository_pubblici": int(profilo.get("public_repos") or 0),
            "commit_pyarchinit": commit, "repository": repository}


def _dal_readme(utente, nome, token=None):
    """Il primo paragrafo di testo del README (senza titoli, badge, immagini e tabelle), tagliato
    a 220 caratteri; vuoto se il README non c'è o non dice niente."""
    try:
        dati, _ = _chiedi(f"{API}/repos/{utente}/{nome}/readme", token)
        testo = base64.b64decode(dati["content"]).decode("utf-8", "replace")
    except Exception:
        return ""
    if "You just built a plugin for QGIS" in testo:  # il README del Plugin Builder, mai sostituito
        return ""
    for blocco in re.split(r"\n\s*\n", testo):
        riga = blocco.strip()
        if not riga or riga.startswith(("#", "!", "[!", "<", "|", "```", "-", "*", ">", "=")):
            continue
        riga = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", riga)
        riga = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", riga)
        riga = re.sub(r"<[^>]+>", " ", riga)
        riga = " ".join(re.sub(r"[`*_>#]", "", riga).split())
        if len(riga) < 40:
            continue
        return riga if len(riga) <= 220 else riga[:217].rsplit(" ", 1)[0] + "…"
    return ""


def automatici(dati, conosciuti, esclusi=(), utente="enzococca", token=None, oggi=None):
    """Una scheda per ogni repository pubblico toccato negli ultimi MESI mesi che non è fra i
    `conosciuti` (gli url delle schede scritte a mano) né fra gli `esclusi` (nomi), dal più
    recente, al massimo MASSIMO. Testo da GitHub, uguale nelle due lingue: la descrizione del
    repository, altrimenti il primo paragrafo del README; un repository senza l'una e senza
    l'altro resta fuori. Niente archiviati, niente la pagina stessa."""
    oggi = oggi or dt.date.today()
    limite = (oggi - dt.timedelta(days=30 * MESI)).isoformat()
    conosciuti = {u.rstrip("/").lower() for u in conosciuti if u}
    schede = []
    for r in sorted(dati["repository"], key=lambda r: r["aggiornato"], reverse=True):
        if r["archiviato"] or r["aggiornato"] < limite or r["nome"] in esclusi or r["nome"] == f"{utente}.github.io":
            continue
        if r["url"].rstrip("/").lower() in conosciuti:
            continue
        descrizione = r["descrizione"] or _dal_readme(utente, r["nome"], token)
        if not descrizione:
            continue
        meta = " · ".join(x for x in (r["linguaggio"], r["licenza"], f"★{r['stelle']}" if r["stelle"] else "") if x)
        schede.append({"nome": r["nome"], "url": r["url"], "privato": False, "meta": meta or r["creato"][:4],
                       "it": descrizione, "en": descrizione, "tag": etichette(r, descrizione),
                       "extra": ("Sito", "Site", r["sito"]) if r["sito"] else None})
        if len(schede) >= MASSIMO:
            break
    return schede


def etichette(r, descrizione):
    """Le etichette di una scheda automatica: i topic di GitHub se ci sono, altrimenti le parole del
    VOCABOLARIO che compaiono nel nome o nella descrizione, e il linguaggio se restano poche; al
    massimo quattro."""
    if r["topics"]:
        return r["topics"][:4]
    testo = f'{r["nome"].replace("-", " ").replace("_", " ")} {descrizione}'.lower()
    tag = []
    for espressione, etichetta in VOCABOLARIO:
        if etichetta not in tag and re.search(espressione, testo):
            tag.append(etichetta)
    if len(tag) < 2 and r["linguaggio"] and r["linguaggio"] not in tag:
        tag.append(r["linguaggio"])
    return tag[:4]


def strato_automatico(schede, num):
    return {
        "num": num,
        "titolo_it": "Ultimi repository",
        "titolo_en": "Latest repositories",
        "intro_it": "Repository pubblici toccati negli ultimi dodici mesi che non hanno ancora una scheda "
                    "scritta a mano: nome e descrizione sono quelli di GitHub e si aggiornano da soli.",
        "intro_en": "Public repositories touched in the last twelve months without a hand-written card "
                    "yet: name and description come from GitHub and update by themselves.",
        "progetti": schede,
    }


def aggiorna_stelle(strati, dati):
    """Le stelle di GitHub nella riga `meta` delle schede scritte a mano (★N aggiornato, o
    aggiunto se il repository ne ha)."""
    stelle = {r["url"].rstrip("/").lower(): r["stelle"] for r in dati["repository"]}
    for s in strati:
        for p in s["progetti"]:
            n = stelle.get((p["url"] or "").rstrip("/").lower())
            if n is None:
                continue
            if re.search(r"★\s*\d[\d.,]*", p["meta"]):
                p["meta"] = re.sub(r"★\s*\d[\d.,]*", f"★{n}", p["meta"])
            elif n:
                p["meta"] = f'{p["meta"]} · ★{n}' if p["meta"] else f"★{n}"
