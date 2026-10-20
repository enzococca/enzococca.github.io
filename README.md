# enzococca.github.io

La mia pagina personale: i progetti, in italiano e in inglese.
Sta online su <https://enzococca.github.io>.

## Com'è fatta

Una pagina sola, senza framework. I due testi convivono nell'HTML e il CSS ne
nasconde uno: la lingua si cambia senza ricaricare, e la pagina resta leggibile
anche con JavaScript spento.

| File | A cosa serve |
|---|---|
| `progetti.py` | I contenuti: un blocco per ogni progetto, con il testo nelle due lingue, e gli `ESCLUSI` |
| `build.py` | Il modello: HTML, CSS e la manciata di righe di JavaScript |
| `repository_github.py` | Quello che arriva da GitHub: stelle, contatori e i repository recenti senza scheda |
| `.github/workflows/pagina.yml` | L'action che costruisce la pagina e la pubblica |
| `index.html` | Il risultato — **generato, non si committa** (lo fa l'action) |

## Come si aggiorna da sola

L'action `pagina` costruisce la pagina con `python3 build.py --github` e la
pubblica su GitHub Pages a ogni push, ogni ora e a richiesta (*Actions >
pagina > Run workflow*). Da GitHub prende:

- le stelle (`★N`) nella riga `meta` delle schede scritte a mano;
- i contatori dell'apertura: repository pubblici e commit su pyArchInit;
- lo strato **Ultimi repository**: i repository pubblici toccati negli ultimi
  dodici mesi che non hanno una scheda qui, con nome e descrizione di GitHub
  (o il primo paragrafo del README) e le etichette dai topic del repository o,
  se non ne ha, dalle parole della descrizione (`VOCABOLARIO` in
  `repository_github.py`, tradotte da `TRADUZIONE_TAG`). Un repository nuovo compare da solo entro
  un'ora; quando gli scrivi la scheda in `progetti.py` esce dalla lista, e per
  non mostrarlo mai lo metti in `ESCLUSI`.

## Aggiungere o cambiare un progetto

1. apri `progetti.py`, copia un blocco esistente e cambia i campi
   (`nome`, `url`, `privato`, `meta`, `it`, `en`, `tag`, `extra`);
2. `python3 build.py` per guardare il risultato (`--github` per vederlo con i
   dati di GitHub, `--offline` per riusare `repository.json` senza scaricare);
3. committa `progetti.py`: l'action ricostruisce e pubblica la pagina.

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
