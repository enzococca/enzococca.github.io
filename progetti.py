"""I progetti mostrati in pagina, con il testo nelle due lingue.

Per aggiungerne uno: copia un blocco, cambia i campi e rilancia `python3 build.py`.
Ogni campo è preso da GitHub o dal README del progetto: se cambi il progetto,
aggiorna anche qui, così la pagina non racconta cose che non sono più vere.

Campi:
  nome      titolo mostrato
  url       link al codice (None per i repository privati)
  privato   True -> niente link, badge "Privato / Private"
  meta      riga tecnica: linguaggio, licenza, stelle… (non tradotta)
  it / en   due o tre righe che spiegano a cosa serve
  tag       parole chiave (non tradotte)
  extra     link secondario (etichetta_it, etichetta_en, url) oppure None
"""

STRATI = [
    {
        "num": "01",
        "titolo_it": "pyArchInit e il suo ecosistema",
        "titolo_en": "pyArchInit and its ecosystem",
        "intro_it": "Il sistema che uso per registrare gli scavi: schede stratigrafiche, "
                    "materiali, matrix di Harris e cartografia dentro QGIS. Ne sono lo "
                    "sviluppatore principale, e intorno al plugin è cresciuta una famiglia "
                    "di strumenti per portarlo in campo, sul web e sul telefono.",
        "intro_en": "The system I use to record excavations: stratigraphic sheets, finds, "
                    "Harris matrix and mapping inside QGIS. I am its lead developer, and a "
                    "family of tools has grown around the plugin to take it into the field, "
                    "onto the web and onto a phone.",
        "progetti": [
            {
                "nome": "pyArchInit",
                "url": "https://github.com/pyarchinit/pyarchinit",
                "privato": False,
                "meta": "Python · QGIS plugin · GPL-2.0 · ★13",
                "it": "Il plugin QGIS per la documentazione archeologica: unità stratigrafiche, "
                      "reperti, campionature, periodizzazioni, matrix di Harris e schede di stampa, "
                      "su PostGIS o SpatiaLite. Sono il primo contributore del repository ufficiale, "
                      "con oltre 2.100 commit.",
                "en": "The QGIS plugin for archaeological recording: stratigraphic units, finds, "
                      "samples, phasing, Harris matrix and printable sheets, on PostGIS or SpatiaLite. "
                      "I am the top contributor to the official repository, with more than 2,100 commits.",
                "tag": ["QGIS", "PostGIS", "stratigrafia"],
                "extra": ("Sito del progetto", "Project site", "https://pyarchinit.github.io"),
            },
            {
                "nome": "pyarchinit-qfield",
                "url": "https://github.com/enzococca/pyarchinit-qfield",
                "privato": False,
                "meta": "QML · QField plugin · ★1",
                "it": "Plugin QField per schedare US e materiali direttamente in trincea, con lo "
                      "stesso schema dati di pyArchInit: quello che registri sul tablet rientra nel "
                      "database senza ricopiature.",
                "en": "A QField plugin to record stratigraphic units and finds straight from the "
                      "trench, on the same data schema as pyArchInit: what you type on the tablet "
                      "goes back into the database without being copied out by hand.",
                "tag": ["QField", "campo", "offline"],
                "extra": None,
            },
            {
                "nome": "pyarchinit-mini",
                "url": "https://github.com/enzococca/pyarchinit-mini",
                "privato": False,
                "meta": "Python · web · desktop · CLI · REST",
                "it": "Una versione autonoma e leggera di pyArchInit, senza dipendenze GIS: stessa "
                      "gestione di siti, US e inventario materiali, ma con quattro interfacce — web, "
                      "desktop, riga di comando e API REST.",
                "en": "A standalone, lightweight pyArchInit without the GIS dependencies: the same "
                      "sites, stratigraphic units and finds inventory, reachable through four "
                      "interfaces — web, desktop, command line and a REST API.",
                "tag": ["FastAPI", "SQLite", "REST"],
                "extra": None,
            },
            {
                "nome": "pyarchinit-storage-server",
                "url": "https://github.com/enzococca/pyarchinit-storage-server",
                "privato": False,
                "meta": "Python · Railway",
                "it": "Server proxy per lo storage remoto di pyArchInit su Google Drive con service "
                      "account: le foto di scavo restano raggiungibili da tutta la squadra senza "
                      "distribuire credenziali.",
                "en": "A proxy server for pyArchInit's remote storage on Google Drive with a service "
                      "account: excavation photos stay reachable by the whole team without handing "
                      "credentials around.",
                "tag": ["storage", "Google Drive"],
                "extra": None,
            },
            {
                "nome": "pyarchinit-api-docs",
                "url": "https://github.com/enzococca/pyarchinit-api-docs",
                "privato": False,
                "meta": "mkdocs-material",
                "it": "Il riferimento API del plugin, generato automaticamente dal codice: serve a "
                      "chi vuole estendere pyArchInit invece di rifarlo da capo.",
                "en": "The plugin's API reference, generated automatically from the code: it is for "
                      "people who want to extend pyArchInit instead of rebuilding it.",
                "tag": ["documentazione"],
                "extra": None,
            },
            {
                "nome": "pyarchinit-website",
                "url": "https://github.com/enzococca/pyarchinit-website",
                "privato": False,
                "meta": "TypeScript",
                "it": "Il sito del progetto: presentazione, guide e materiali per chi si avvicina "
                      "a pyArchInit per la prima volta.",
                "en": "The project's website: overview, guides and material for anyone approaching "
                      "pyArchInit for the first time.",
                "tag": ["web"],
                "extra": None,
            },
        ],
    },
    {
        "num": "02",
        "titolo_it": "Rilievo, fotogrammetria, topografia",
        "titolo_en": "Survey, photogrammetry, topography",
        "intro_it": "Portare le misure dallo scavo al modello senza passare da una workstation. "
                    "Fotogrammetria da telefono e da drone, stazione totale, sezioni e profili.",
        "intro_en": "Getting measurements from the trench to the model without going through a "
                    "workstation. Photogrammetry from phone and drone, total station, sections "
                    "and profiles.",
        "progetti": [
            {
                "nome": "Photo3D",
                "url": None,
                "privato": True,
                "meta": "Swift · Kotlin · Python · iOS / Android / macOS / Windows / Linux",
                "it": "Fotogrammetria che sta in tasca e gira sul tuo computer. Scatti con il "
                      "telefono o pianifichi un volo con un drone DJI, e il tuo Mac, Windows o Linux "
                      "elabora con Metashape o WebODM: nessun account cloud, le foto non escono di "
                      "casa. Maschere con un tocco, scala metrica reale, GCP, sezioni e profili "
                      "misurati dentro l'app. Provato in campo su una trincea a Bintan: 177 foto da "
                      "drone, 302.928 facce.",
                "en": "Photogrammetry that fits in your pocket and runs on your own computer. Shoot "
                      "with the phone or plan a DJI drone flight, and your Mac, Windows or Linux box "
                      "processes it with Metashape or WebODM: no cloud account, the photos never "
                      "leave the house. One-tap masking, real metric scale, ground control points, "
                      "sections and profiles measured inside the app. Field-tested on a trench in "
                      "Bintan: 177 drone photos, 302,928 faces.",
                "tag": ["Metashape", "WebODM", "DJI", "SwiftUI", "Compose"],
                "extra": ("Guida di campo", "Field guide", "https://enzococca.github.io/photo3d-guida"),
            },
            {
                "nome": "Total Open Station",
                "url": "https://github.com/totalopenstation/totalopenstation",
                "privato": False,
                "meta": "Python · ★83 · contributore",
                "it": "Il software libero che scarica ed esporta i dati dalle stazioni totali, nato "
                      "nel progetto IOSA di Stefano Costa e Luca Bianconi. Contribuisco al progetto "
                      "a monte e ne curo il ponte verso QGIS.",
                "en": "The free software that downloads and exports data from total stations, born "
                      "in the IOSA project by Stefano Costa and Luca Bianconi. I contribute upstream "
                      "and maintain the bridge towards QGIS.",
                "tag": ["stazione totale", "upstream"],
                "extra": None,
            },
            {
                "nome": "totalopenstationToQgis",
                "url": "https://github.com/enzococca/totalopenstationToQgis",
                "privato": False,
                "meta": "Python · QGIS plugin · ★1",
                "it": "Il ponte: lancia Total Open Station da dentro QGIS, riconosce le porte seriali "
                      "e USB, e porta i punti battuti direttamente nel progetto, con anteprima prima "
                      "di importare.",
                "en": "The bridge: launches Total Open Station from inside QGIS, detects serial and "
                      "USB ports, and brings surveyed points straight into the project, with a "
                      "preview before importing.",
                "tag": ["QGIS", "seriale"],
                "extra": None,
            },
            {
                "nome": "dual_profile_viewer",
                "url": "https://github.com/enzococca/dual_profile_viewer",
                "privato": False,
                "meta": "Python · QGIS plugin · ★1",
                "it": "Profili altimetrici in QGIS: profilo singolo o doppio, sezioni multiple su "
                      "poligono, vista 3D ed esportazione vettoriale georiferita. Nato per "
                      "l'archeologia, usato anche in geologia e ingegneria.",
                "en": "Elevation profiles in QGIS: single or dual profile, multi-section polygons, "
                      "3D view and georeferenced vector export. Built for archaeology, useful in "
                      "geology and engineering too.",
                "tag": ["DEM", "profili", "3D"],
                "extra": None,
            },
            {
                "nome": "wall_section",
                "url": "https://github.com/enzococca/wall_section",
                "privato": False,
                "meta": "Python · QGIS plugin",
                "it": "Sezioni attraverso più DEM sovrapposti, restituite come multipoligoni "
                      "topologicamente corretti e in scala: serve a disegnare i prospetti dei muri "
                      "e le sequenze stratigrafiche senza ridisegnarli a mano.",
                "en": "Sections across several stacked DEMs, returned as topologically correct, "
                      "scaled multipolygons: it is how you draw wall elevations and stratigraphic "
                      "sequences without redrawing them by hand.",
                "tag": ["DEM", "muri", "stratigrafia"],
                "extra": None,
            },
        ],
    },
    {
        "num": "03",
        "titolo_it": "App da campo",
        "titolo_en": "Field apps",
        "intro_it": "Quello che serve in trincea funziona offline, si usa con le mani sporche e "
                    "non chiede di registrarsi da nessuna parte.",
        "intro_en": "What you need in a trench works offline, can be used with dirty hands and "
                    "does not ask you to sign up anywhere.",
        "progetti": [
            {
                "nome": "Giornale di Scavo",
                "url": None,
                "privato": True,
                "meta": "Swift / SwiftUI · Kotlin / Compose · iOS + Android",
                "it": "Il diario di scavo digitale che sostituisce quello cartaceo: semplicissimo e "
                      "100% offline, tutto resta sul dispositivo. Stessa impostazione e stesse "
                      "funzioni nelle due versioni native, iOS e Android.",
                "en": "The digital excavation diary that replaces the paper one: dead simple and "
                      "100% offline, everything stays on the device. Same shape and same features "
                      "in both native versions, iOS and Android.",
                "tag": ["offline", "SwiftUI", "Jetpack Compose"],
                "extra": ("Privacy", "Privacy", "https://enzococca.github.io/giornale-di-scavo"),
            },
            {
                "nome": "FieldNotes",
                "url": None,
                "privato": True,
                "meta": "Swift · iOS + macOS",
                "it": "App per ricognizioni etnografiche e archeologiche: osservazioni, note vocali, "
                      "foto, schizzi disegnati a mano e coordinate GPS su ogni rilevamento, "
                      "raccolti in survey.",
                "en": "An app for ethnographic and archaeological surveys: observations, voice notes, "
                      "photos, hand-drawn sketches and GPS coordinates on every finding, gathered "
                      "into surveys.",
                "tag": ["ricognizione", "GPS", "multipiattaforma"],
                "extra": None,
            },
            {
                "nome": "Rendiconta",
                "url": None,
                "privato": True,
                "meta": "Swift · Kotlin · iOS + Android",
                "it": "Scatti una foto a scontrini e fatture e l'app compila la rendicontazione "
                      "della missione nel formato del modulo di richiesta rimborsi: elenco numerato "
                      "dei giustificativi, importi, totale e foto in allegato.",
                "en": "Photograph your receipts and invoices and the app fills in the mission "
                      "expense report in the reimbursement-form format: numbered list of receipts, "
                      "amounts, total and the photos attached.",
                "tag": ["OCR", "missioni"],
                "extra": None,
            },
            {
                "nome": "Create Layer",
                "url": "https://github.com/enzococca/createlayer",
                "privato": False,
                "meta": "QML · QField ≥ 3.2",
                "it": "Plugin QField per creare nuovi layer direttamente sul campo, digitalizzare "
                      "geometrie ed esportare i dati raccolti senza tornare a QGIS desktop.",
                "en": "A QField plugin to create new layers directly in the field, digitise "
                      "geometries and export what you collected without going back to QGIS desktop.",
                "tag": ["QField", "GeoJSON"],
                "extra": None,
            },
        ],
    },
    {
        "num": "04",
        "titolo_it": "Analisi spaziale",
        "titolo_en": "Spatial analysis",
        "intro_it": "Strumenti per far dire qualcosa ai dati: superfici di costo, geostatistica, "
                    "interrogazione di database spaziali, decomposizione di palinsesti.",
        "intro_en": "Tools that make the data say something: cost surfaces, geostatistics, "
                    "spatial database querying, palimpsest decomposition.",
        "progetti": [
            {
                "nome": "GeoArchaeo",
                "url": "https://github.com/enzococca/GeoArchaeo",
                "privato": False,
                "meta": "Python · QGIS plugin · ★3",
                "it": "Geostatistica per l'archeologia dentro QGIS: kriging, variogrammi e "
                      "riconoscimento di pattern con machine learning, per capire come si "
                      "distribuiscono i materiali sul terreno.",
                "en": "Geostatistics for archaeology inside QGIS: kriging, variograms and machine "
                      "learning pattern recognition, to understand how finds are distributed across "
                      "the ground.",
                "tag": ["kriging", "machine learning"],
                "extra": None,
            },
            {
                "nome": "movecost",
                "url": "https://github.com/enzococca/movecost",
                "privato": False,
                "meta": "Python + R · QGIS plugin",
                "it": "Superfici di costo dipendenti dalla pendenza, percorsi e corridoi a costo "
                      "minimo per lo studio del movimento umano nel paesaggio: porta il pacchetto R "
                      "movecost di Gianmarco Alberti dentro QGIS con un'interfaccia Python.",
                "en": "Slope-dependent accumulated cost surfaces, least-cost paths and corridors for "
                      "the study of human movement across the landscape: it brings Gianmarco "
                      "Alberti's movecost R package into QGIS behind a Python interface.",
                "tag": ["least-cost path", "R", "paesaggio"],
                "extra": ("Versione R per QGIS", "R version for QGIS",
                          "https://github.com/enzococca/movecostTOqgis"),
            },
            {
                "nome": "GeoSQL",
                "url": "https://github.com/enzococca/geosql-python",
                "privato": False,
                "meta": "Python + Kotlin · libreria + plugin PyCharm",
                "it": "Cassetta degli attrezzi per database spaziali: PostGIS, SpatiaLite, Oracle "
                      "Spatial, SQL Server e MySQL, più SQL su CSV, Excel, Parquet, GeoJSON e "
                      "shapefile via DuckDB. Le interrogazioni si possono scrivere in linguaggio "
                      "naturale, e il plugin per PyCharm mostra il risultato su mappa.",
                "en": "A toolkit for spatial databases: PostGIS, SpatiaLite, Oracle Spatial, SQL "
                      "Server and MySQL, plus SQL over CSV, Excel, Parquet, GeoJSON and shapefiles "
                      "through DuckDB. Queries can be written in plain language, and the PyCharm "
                      "plugin puts the result on a map.",
                "tag": ["PostGIS", "DuckDB", "AI"],
                "extra": ("Plugin PyCharm", "PyCharm plugin",
                          "https://github.com/enzococca/geosql-plugin"),
            },
            {
                "nome": "palimpsestr",
                "url": "https://github.com/enzococca/palimpsestr",
                "privato": False,
                "meta": "R · ★2",
                "it": "Decomposizione probabilistica dei palinsesti archeologici con Stratigraphic "
                      "Entanglement Fields: prova a separare gli eventi che si sono sovrapposti in "
                      "un unico deposito.",
                "en": "Probabilistic decomposition of archaeological palimpsests using Stratigraphic "
                      "Entanglement Fields: an attempt to pull apart the events that piled up into a "
                      "single deposit.",
                "tag": ["R", "bayesiano", "teoria"],
                "extra": None,
            },
        ],
    },
    {
        "num": "05",
        "titolo_it": "Ceramica e reperti",
        "titolo_en": "Pottery and finds",
        "intro_it": "Classificare, confrontare e misurare i materiali: dal coccio disegnato al "
                    "modello 3D, con l'aiuto della visione artificiale quando serve.",
        "intro_en": "Classifying, comparing and measuring finds: from the drawn sherd to the 3D "
                    "model, with computer vision where it helps.",
        "progetti": [
            {
                "nome": "Ceramica Classifier",
                "url": "https://github.com/enzococca/ceramic-classifier",
                "privato": False,
                "meta": "Python · machine learning",
                "it": "Classificazione automatica di frammenti ceramici decorati dagli scavi in "
                      "Oman, dall'Umm an-Nar al Wadi Suq fino all'Età del Ferro: confronta le "
                      "decorazioni con collezioni di riferimento e propone paralleli tipologici e "
                      "attribuzioni cronologiche.",
                "en": "Automatic classification of decorated pottery sherds from excavations in "
                      "Oman, from Umm an-Nar and Wadi Suq to the Iron Age: it compares decorations "
                      "with reference collections and proposes typological parallels and "
                      "chronological attributions.",
                "tag": ["Oman", "tipologia", "ML"],
                "extra": None,
            },
            {
                "nome": "Ceramica KhUTM",
                "url": "https://github.com/enzococca/ceramic-khutm",
                "privato": False,
                "meta": "Python · Flask",
                "it": "La stessa idea calibrata sulle collezioni del museo KhUTM: confronto con il "
                      "corpus Schmidt 1937 e con altre raccolte di riferimento per datare i "
                      "frammenti decorati.",
                "en": "The same idea tuned to the KhUTM museum collections: comparison against the "
                      "Schmidt 1937 corpus and other reference collections to date decorated sherds.",
                "tag": ["museo", "corpus"],
                "extra": None,
            },
            {
                "nome": "CeramicaDatabase",
                "url": "https://github.com/enzococca/pottery-comparison",
                "privato": False,
                "meta": "Python · web",
                "it": "Visore e gestionale web unificato per le collezioni ceramiche della penisola "
                      "arabica: sfoglia, confronta, ruota e cataloga i pezzi da una sola interfaccia.",
                "en": "A unified web viewer and manager for archaeological ceramic collections from "
                      "the Arabian Peninsula: browse, compare, rotate and catalogue the pieces from "
                      "one interface.",
                "tag": ["catalogo", "web"],
                "extra": None,
            },
            {
                "nome": "BrozeAXE-AI",
                "url": "https://github.com/enzococca/BrozeAXE-AI",
                "privato": False,
                "meta": "Python · mesh 3D · ★1",
                "it": "Analisi morfometrica e classificazione di bronzi dell'Età del Bronzo a partire "
                      "da mesh 3D (OBJ, PLY, STL). Nato per il ripostiglio di asce di Savignano, "
                      "unisce misura sulla mesh, statistica, machine learning e ragionamento con un "
                      "modello linguistico.",
                "en": "Morphometric analysis and classification of Bronze Age metalwork from 3D "
                      "meshes (OBJ, PLY, STL). Built for the Savignano axe hoard, it combines "
                      "measurement on the mesh, statistics, machine learning and reasoning with a "
                      "language model.",
                "tag": ["3D", "morfometria", "Età del Bronzo"],
                "extra": None,
            },
            {
                "nome": "sherdtool-web",
                "url": None,
                "privato": True,
                "meta": "Python · web self-hosted",
                "it": "Applicazione web per l'analisi dei cocci a partire da scansioni 3D, da "
                      "installare sul proprio server: misure, orientamento e confronti sul frammento "
                      "digitalizzato.",
                "en": "A self-hosted web application for analysing pottery sherds from 3D scans: "
                      "measurements, orientation and comparisons on the digitised fragment.",
                "tag": ["3D", "self-hosted"],
                "extra": None,
            },
            {
                "nome": "Fauna Manager",
                "url": "https://github.com/enzococca/schedafaune",
                "privato": False,
                "meta": "Python · pyArchInit",
                "it": "Gestione delle schede faunistiche (scheda FR) integrata con pyArchInit: i "
                      "dati archeozoologici si agganciano alle unità stratigrafiche invece di vivere "
                      "in un foglio di calcolo a parte.",
                "en": "Faunal record sheets (FR sheet) integrated with pyArchInit: zooarchaeological "
                      "data hooks onto the stratigraphic units instead of living in a separate "
                      "spreadsheet.",
                "tag": ["archeozoologia", "QGIS"],
                "extra": None,
            },
        ],
    },
    {
        "num": "06",
        "titolo_it": "Archeologia subacquea e marittima",
        "titolo_en": "Underwater and maritime archaeology",
        "intro_it": "Sott'acqua cambia tutto: i tempi sono quelli della bombola, la rete non c'è e "
                    "i dati devono aspettare la risalita.",
        "intro_en": "Underwater everything changes: your time is what the tank gives you, there is "
                    "no network, and the data has to wait for the ascent.",
        "progetti": [
            {
                "nome": "Shipwreck Excavation",
                "url": None,
                "privato": True,
                "meta": "Python · QGIS plugin · PostGIS / Supabase",
                "it": "Sistema completo per lo scavo di relitti dentro QGIS: reperti con foto e "
                      "modelli 3D, registro delle immersioni, squadre, costi e budget, bot Telegram "
                      "per inserire i dati quando la rete non c'è, storage su Cloudflare R2 e Google "
                      "Drive. Bilingue inglese e indonesiano.",
                "en": "A complete system for shipwreck excavation inside QGIS: finds with photos and "
                      "3D models, dive logs, crew, costs and budget, a Telegram bot for entering "
                      "data when there is no network, storage on Cloudflare R2 and Google Drive. "
                      "Bilingual, English and Indonesian.",
                "tag": ["relitti", "PostGIS", "Supabase"],
                "extra": None,
            },
            {
                "nome": "HFF-Survey",
                "url": "https://github.com/enzococca/HFF",
                "privato": False,
                "meta": "Python · QGIS plugin · ★1",
                "it": "Plugin QGIS per le ricognizioni della Honor Frost Foundation: registrazione "
                      "di siti e survey marittimi con lo stesso rigore di uno scavo terrestre.",
                "en": "A QGIS plugin for Honor Frost Foundation surveys: recording maritime sites "
                      "and survey work with the same rigour as a land excavation.",
                "tag": ["survey", "QGIS"],
                "extra": ("Installer", "Installer", "https://github.com/enzococca/hff_installer"),
            },
            {
                "nome": "HFF Telegram bot",
                "url": None,
                "privato": True,
                "meta": "Python · Telegram",
                "it": "Bot Telegram per inserire dati di campo in HFF-Survey: se il database non è "
                      "raggiungibile mette le scritture in coda in locale e le rigioca appena la "
                      "rete torna.",
                "en": "A Telegram bot for field data entry into HFF-Survey: when the database is "
                      "unreachable it queues the writes locally and replays them as soon as the "
                      "network is back.",
                "tag": ["offline-first", "bot"],
                "extra": None,
            },
        ],
    },
    {
        "num": "07",
        "titolo_it": "Banche dati e cartografia in rete",
        "titolo_en": "Databases and web mapping",
        "intro_it": "Progetti nati su territori precisi — Soqotra, il Tamil Nadu, le Nilgiri — dove "
                    "il problema non era raccogliere i dati ma renderli consultabili.",
        "intro_en": "Projects born on specific ground — Soqotra, Tamil Nadu, the Nilgiris — where "
                    "the problem was not collecting the data but making it searchable.",
        "progetti": [
            {
                "nome": "Soqotra Rock Art Database",
                "url": "https://github.com/enzococca/SoqotraRockArt",
                "privato": False,
                "meta": "Python · Flask · web",
                "it": "Catalogo web dell'arte rupestre di Soqotra: schedatura completa dei pannelli, "
                      "autenticazione degli utenti e gestione condivisa dei record.",
                "en": "A web catalogue of Soqotra's rock art: full recording of the panels, user "
                      "authentication and shared record management.",
                "tag": ["arte rupestre", "Yemen"],
                "extra": None,
            },
            {
                "nome": "Korkai Archaeological Map",
                "url": "https://github.com/enzococca/korkai-map",
                "privato": False,
                "meta": "HTML · Leaflet",
                "it": "Mappa interattiva dei siti archeologici intorno a Korkai, nel Tamil Nadu: un "
                      "modo semplice per far vedere a chiunque dove sono le evidenze.",
                "en": "An interactive map of the archaeological sites around Korkai, Tamil Nadu: a "
                      "plain way to show anyone where the evidence is.",
                "tag": ["India", "mappa"],
                "extra": None,
            },
            {
                "nome": "Badaga–English Dictionary",
                "url": None,
                "privato": True,
                "meta": "Python · FastAPI",
                "it": "Digitalizzazione del dizionario badaga–inglese di Hockings e Pilot-Raichoor "
                      "(1992): le voci sono estratte dalle scansioni con un modello di visione, "
                      "collegate al Dravidian Etymological Dictionary e cercabili anche per "
                      "somiglianza fonetica.",
                "en": "A digitisation of the Badaga–English dictionary by Hockings and "
                      "Pilot-Raichoor (1992): entries are pulled out of the scans with a vision "
                      "model, linked to the Dravidian Etymological Dictionary and searchable by "
                      "phonetic similarity.",
                "tag": ["linguistica", "India", "OCR"],
                "extra": None,
            },
            {
                "nome": "Nilgiri Deforestation",
                "url": None,
                "privato": True,
                "meta": "Python · Landsat · Sentinel",
                "it": "Analisi multi-temporale e multi-sensore della copertura forestale delle "
                      "Nilgiri Hills dal 1988 a oggi: venticinque classificazioni Landsat messe a "
                      "confronto per misurare quanto bosco è sparito.",
                "en": "Multi-temporal, multi-sensor analysis of forest cover in the Nilgiri Hills "
                      "from 1988 to today: twenty-five Landsat classifications compared to measure "
                      "how much forest has gone.",
                "tag": ["telerilevamento", "India"],
                "extra": None,
            },
        ],
    },
    {
        "num": "08",
        "titolo_it": "Intelligenza artificiale applicata",
        "titolo_en": "Applied AI",
        "intro_it": "Non l'IA come vetrina, ma come attrezzo: leggere archivi, scrivere "
                    "documentazione, orchestrare procedure che altrimenti restano nel cassetto.",
        "intro_en": "Not AI as a showcase but as a tool: reading archives, writing documentation, "
                    "orchestrating procedures that would otherwise stay in a drawer.",
        "progetti": [
            {
                "nome": "Ganesha RAG",
                "url": None,
                "privato": True,
                "meta": "Python · Flask · LangChain · FAISS",
                "it": "Piattaforma RAG self-hosted per gruppi di ricerca: si conversa con i propri "
                      "documenti ottenendo citazioni verificabili, si generano grafici e report, si "
                      "georiferiscono mappe storiche, si trascrivono registrazioni con Whisper e si "
                      "lavora in chat tradotta. Cinque lingue: olandese, inglese, tamil, italiano e "
                      "kannada.",
                "en": "A self-hosted RAG platform for research teams: chat with your own documents "
                      "and get verifiable citations, generate charts and reports, georeference "
                      "historical maps, transcribe recordings with Whisper and work in a translated "
                      "team chat. Five languages: Dutch, English, Tamil, Italian and Kannada.",
                "tag": ["RAG", "Whisper", "multilingua"],
                "extra": None,
            },
            {
                "nome": "PyArchInit DocuGenius",
                "url": None,
                "privato": True,
                "meta": "Kotlin · plugin JetBrains",
                "it": "Generatore di documentazione per le IDE JetBrains: dal codice tira fuori un "
                      "manuale utente e un riferimento API in PDF, con impaginazione da manuale vero "
                      "— copertina, titoli, riquadri di nota e avvertenza — e in più lingue.",
                "en": "A documentation generator for JetBrains IDEs: it turns code into a user "
                      "manual and an API reference in PDF, laid out like a real manual — cover, "
                      "headings, tip and warning boxes — in several languages.",
                "tag": ["IntelliJ", "PDF", "documentazione"],
                "extra": None,
            },
            {
                "nome": "Gennaro / modelbuilderAI",
                "url": "https://github.com/enzococca/modelbuilderAI",
                "privato": False,
                "meta": "Python · workflow builder",
                "it": "Orchestratore di agenti con costruttore visuale di flussi: si compone la "
                      "catena di lavorazione trascinando i blocchi, invece di scrivere ogni volta lo "
                      "stesso script di collegamento.",
                "en": "An agent orchestrator with a visual workflow builder: you compose the "
                      "processing chain by dragging blocks instead of writing the same glue script "
                      "over and over.",
                "tag": ["agenti", "workflow"],
                "extra": None,
            },
            {
                "nome": "Deep Search AI",
                "url": "https://github.com/enzococca/deep-search-ai",
                "privato": False,
                "meta": "Python · vector database",
                "it": "Ricerca multimodale su testi, immagini e documenti con agenti specializzati e "
                      "database vettoriale: pensata per chi ha archivi eterogenei e nessuna voglia di "
                      "aprirli uno a uno.",
                "en": "Multimodal search over texts, images and documents with specialised agents "
                      "and a vector database: made for people with heterogeneous archives and no "
                      "wish to open them one by one.",
                "tag": ["ricerca semantica", "agenti"],
                "extra": None,
            },
        ],
    },
]
