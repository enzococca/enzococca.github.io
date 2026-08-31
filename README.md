# enzococca.github.io

La mia pagina personale: i progetti, in italiano e in inglese.
Sta online su <https://enzococca.github.io>.

## Com'è fatta

Una pagina sola, senza framework e senza passaggi di compilazione in rete.
I due testi convivono nell'HTML e il CSS ne nasconde uno: la lingua si cambia
senza ricaricare, e la pagina resta leggibile anche con JavaScript spento.

| File | A cosa serve |
|---|---|
| `progetti.py` | I contenuti: un blocco per ogni progetto, con il testo nelle due lingue |
| `build.py` | Il modello: HTML, CSS e la manciata di righe di JavaScript |
| `index.html` | Il risultato — **generato, non si modifica a mano** |

## Aggiungere o cambiare un progetto

1. apri `progetti.py`, copia un blocco esistente e cambia i campi
   (`nome`, `url`, `privato`, `meta`, `it`, `en`, `tag`, `extra`);
2. `python3 build.py`
3. committa `progetti.py` **e** `index.html`.

Per un progetto privato metti `"url": None` e `"privato": True`: compare la
scheda con il badge *Privato / Private* e nessun collegamento al codice.

I tag scritti in italiano si traducono da soli se compaiono in
`TRADUZIONE_TAG`, dentro `build.py`; quelli tecnici (QGIS, PostGIS, DJI…)
restano uguali nelle due lingue.

## Guardarla prima di pubblicare

    python3 -m http.server 8899
    # poi http://127.0.0.1:8899

Il `file://` diretto funziona lo stesso, ma con un server locale il
comportamento è identico a quello di GitHub Pages.
