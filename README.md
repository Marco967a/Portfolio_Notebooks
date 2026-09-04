# Data Science & Analytics Portfolio

Benvenuto nel mio repository portfolio! Qui raccolgo una selezione di progetti e notebook incentrati su **Data Cleaning**, **Analisi Esplorativa dei Dati (EDA)**, **Feature Engineering & Normalizzazione** e **Modellazione Predittiva**.

---

## 👤 Presentazione Personale

Ciao, sono **Marco**! Sono un appassionato di dati e aspirante Data Analyst / Data Scientist. Il mio approccio al dato si fonda su tre principi chiave:

1. **Rigore Metodologico**: Prima di ogni modellazione, dedico grande cura alla comprensione e alla pulizia del dato (gestione di valori mancanti, duplicati, outlier e incongruenze), evitando scorciatoie che possano distorcere la distribuzione originale.
2. **EDA Approfondita e Storytelling**: Credo che le visualizzazioni e l'analisi statistica (univariata, bivariata e multivariata) siano essenziali per estrarre insight autentici, identificare pattern nascosti e validare ipotesi di business o scientifiche.
3. **Modellazione e Trasparenza**: Applico tecniche di scaling e algoritmi di Machine Learning ponendo l'accento sull'interpretazione dei risultati (feature importance, metriche di valutazione coerenti e generalizzabilità del modello).

### 🛠️ Competenze e Stack Tecnologico
* **Linguaggi & Ambienti**: Python, Jupyter Notebook, Google Colab
* **Manipolazione & Analisi Dati**: Pandas, NumPy
* **Visualizzazione**: Matplotlib, Seaborn
* **Machine Learning & Statistica**: Scikit-Learn (Linear Regression, Preprocessing, Metrics, Train/Test Split)

---

## 📑 Indice dei Progetti

| Progetto | Dominio | Tecniche Chiave | Risultato / Metriche | Notebook |
| :--- | :--- | :--- | :--- | :---: |
| **CalCOFI Oceanographic Analysis** | Scienze Ambientali / Oceanografia | EDA, Data Cleaning, Normalizzazione, Regressione Lineare Semplice e Multipla, Feature Importance | $R^2 \approx 0.96$, $\text{RMSE} \approx 0.18$ | [OCEAN.ipynb](./OCEAN.ipynb) |
| **Adult Census Income** | Socio-Economico / Demografico | Pulizia avanzata (imputazione distributiva di `?`), EDA Bivariata/Multivariata, Analisi di Disparità di Genere | Identificazione dei driver socio-economici di reddito | [ADULT.ipynb](./ADULT.ipynb) |
| **Iris Benchmark Scaling** | Botanica / Machine Learning Foundations | Data Cleaning, EDA comparativa morfologica, Benchmark di Normalizzazione (MinMax vs Standard vs Robust) | Dimostrazione dell'invarianza di skewness nei diversi scaler | [IRIS.ipynb](./IRIS.ipynb) |

---

## 🔬 Executive Summary dei Progetti

### 1. [Analisi Oceanografica e Predizione della Temperatura Marina](./OCEAN.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marco967a/Portfolio_Notebooks/blob/main/OCEAN.ipynb)

* **Obiettivo**: Analizzare le proprietà chimico-fisiche e biogeochimiche delle masse d'acqua marine e costruire modelli di regressione lineare (semplice e multipla) in grado di predire con precisione la temperatura superficiale e profonda dell'acqua (`T_degC`), quantificando il contributo relativo di ciascuna variabile oceanografica.
* **Dataset**: [CalCOFI Bottle Database](https://newdata.calcofi.com/index.php/database/calcofi-database/bottle-field-descriptions) (California Cooperative Oceanic Fisheries Investigations), uno dei set di dati oceanografici più completi al mondo. È stato estratto un sottoinsieme rappresentativo di 45.000 campioni, pulito e ridotto a 11.100 record completi su 9 variabili fondamentali: variabili fisiche (`Depthm`, `Salnty`, `STheta`), nutrienti e parametri biologici (`O2ml_L`, `PO4uM`, `SiO3uM`, `NO3uM`, `ChlorA`) e variabile target (`T_degC`).
* **Conclusioni Chiave**:
  * Il modello di **regressione lineare multipla** dimostra un'elevata accuratezza e capacità di generalizzazione, raggiungendo $R^2 \approx 0.96$ (sia su training che su test set) con un errore medio quadratico $\text{RMSE} \approx 0.18$, confermando l'assenza di overfitting.
  * Nella comparazione delle regressioni semplici, la **densità potenziale (`STheta`)** risulta il singolo predittore più potente da solo ($R^2 = 0.94$), seguita dai nutrienti **fosfati (`PO4uM`, $R^2 = 0.76$)** e **nitrati (`NO3uM`, $R^2 = 0.75$)**, a testimonianza dei forti legami termodinamici e dei fenomeni di *upwelling*.
  * L'analisi dell'importanza delle feature conferma che parametri fisici (`STheta`) e biogeochimici (`PO4uM`, `O2ml_L`) dominano la predizione; la profondità pura (`Depthm`) ha un impatto diretto marginale una volta noti i parametri chimico-fisici dello strato d'acqua.

---

### 2. [Adult Census Income: Data Cleaning ed Analisi Socio-Economica](./ADULT.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marco967a/Portfolio_Notebooks/blob/main/ADULT.ipynb)

* **Obiettivo**: Eseguire una pulizia rigorosa su un dataset censuario reale caratterizzato da valori mancanti non standard e rumore, conducendo un'analisi esplorativa mirata a identificare i principali determinanti socio-demografici ed educativi che discriminano la soglia di reddito annuo ($\le 50\text{K}$ vs $> 50\text{K}$).
* **Dataset**: Adult Census Income (US Census Bureau). Composto da 32.510 record (dopo la rimozione dei duplicati) e 15 variabili comprendenti dati demografici (`age`, `race`, `sex`, `native country`), variabili lavorative (`workclass`, `occupation`, `hours per week`, `capital gain`, `capital loss`), educative/familiari (`education`, `education num`, `marital status`, `relationship`) e target (`income`).
* **Data Cleaning Rilevante**:
  * I valori mancanti, originariamente codificati con il carattere `?` in tre colonne categoriche (`workclass`, `occupation`, `native country`), sono stati gestiti con una sostituzione probabilistica conforme alla distribuzione originale delle categorie. Ciò ha evitato distorsioni da sovraffollamento della moda e ha preservato il 5,6% del campione totale che altrimenti sarebbe andato perso con un'eliminazione ingenua.
  * Gli outlier numerici sono stati preservati poiché rappresentano casi economici reali e validi indispensabili per non alterare la rappresentatività del campione.
* **Conclusioni Chiave**:
  * **Istruzione ed Esperienza**: L'istruzione è il fattore più discriminante (`education num` è superiore in media di 2 anni nei soggetti $>50\text{K}$), unita all'età lavorativa (età media superiore di +7,5 anni nel gruppo ad alto reddito) e alle ore lavorate settimanali (+6,6 ore).
  * **Disparità di Genere & Segregazione**: L'analisi evidenzia un marcato gender pay gap (il 30,6% degli uomini guadagna $>50\text{K}$ contro appena l'11% delle donne; le donne rappresentano solo il 15,5% della fascia ad alto reddito pur costituendo un terzo del campione totale). Inoltre, si rileva una forte segregazione occupazionale, con le donne concentrate in ruoli amministrativi e di servizio. Anche in presenza di percorsi di istruzione avanzati, il divario di genere rimane tangibile.
  * **Ruolo del Capitale**: Le variabili di guadagno e perdita patrimoniale (`capital-gain`/`capital-loss`), pur caratterizzate da elevata asimmetria (con mediana a 0), registrano medie fino a 25 volte più alte nel segmento ad alto reddito.

---

### 3. [Iris Flower: EDA e Benchmark di Normalizzazione](./IRIS.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marco967a/Portfolio_Notebooks/blob/main/IRIS.ipynb)

* **Obiettivo**: Esplorare le proprietà biometriche del classico dataset Iris ed effettuare un'analisi comparativa empirica di tre tecniche fondamentali di feature scaling (**MinMaxScaler**, **StandardScaler**, **RobustScaler**), valutandone l'effetto su scale, centratura e preservazione della forma distributiva.
* **Dataset**: Fisher's Iris Dataset. 147 campioni analizzati (dopo eliminazione di duplicati) articolati su 4 feature biometriche continue (`SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`) e una variabile target categorica a tre classi (`Species`: *Iris-setosa*, *Iris-versicolor*, *Iris-virginica*).
* **Conclusioni Chiave**:
  * **Morfologia delle Specie**: *Iris-setosa* risulta nettamente e linearmente separabile dalle altre specie già al livello bivariato grazie alle ridotte dimensioni di petalo (lunghezza e larghezza) e sepali più corti ma più larghi. Al contrario, *versicolor* e *virginica* presentano un parziale grado di sovrapposizione dimensionale.
  * **Preservazione della Forma Distributiva**: Il confronto statistico e visivo ha dimostrato che tutte e tre le metodologie di normalizzazione preservano integralmente la forma della distribuzione originale; i valori di *skewness* (asimmetria) rimangono rigorosamente identici pre e post-trasformazione.
  * **Proprietà dei Singoli Scaler**:
    * `MinMaxScaler`: Comprime i valori nell'intervallo compatto $[0, 1]$, ideale per algoritmi basati su gradienti o immagini, ma sensibile agli outlier.
    * `StandardScaler`: Centra i dati sulla media ($\mu = 0$) con varianza unitaria ($\sigma = 1$), presupposto per algoritmi che assumono gaussianità o regressioni regolarizzate.
    * `RobustScaler`: Ricalibra i dati basandosi su mediana e scarto interquartile (IQR), offrendo la massima robustezza in presenza di valori anomali senza alterare la struttura informativa.

---

## 💻 Come Eseguire i Notebook

I notebook possono essere eseguiti sia localmente tramite Jupyter / VS Code, sia direttamente su Google Colab cliccando sui rispettivi badge.

### Esecuzione in Locale
1. Clona il repository:
   ```bash
   git clone https://github.com/Marco967a/Portfolio_Notebooks.git
   cd Portfolio_Notebooks
   ```

2. Crea e attiva un ambiente virtuale (consigliato):
   ```bash
   python -m venv .venv
   # Su Windows:
   .venv\Scripts\activate
   # Su macOS/Linux:
   source .venv/bin/activate
   ```

3. Installa i pacchetti necessari:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

4. Avvia Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

## 📬 Contatti & Link

- **GitHub**: [@Marco967a](https://github.com/Marco967a)
- **Email**: [marco.santagati96@gmail.com](mailto:marco.santagati96@gmail.com)

---
*Progetto curato da Marco Santagati. Sentiti libero di aprire una issue o una pull request per suggerimenti o approfondimenti!*