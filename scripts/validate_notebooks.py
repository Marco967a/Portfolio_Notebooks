"""
Script di validazione per Portfolio_Notebooks.
Verifica:
1. Presenza e integrità dei dataset in data/
2. Validità sintattica e struttura JSON dei notebook .ipynb
3. Funzionamento della cella di caricamento dati per ciascun notebook
"""
import glob
import json
import os
import sys
import pandas as pd
import numpy as np

def test_datasets():
    print(">>> 1. Controllo Dataset in data/...")
    datasets = {
        os.path.join("data", "iris.csv"): (140, 160),
        os.path.join("data", "adult.csv"): (30000, 35000),
        os.path.join("data", "ocean_sample.csv"): (40000, 50000)
    }
    for path, (min_rows, max_rows) in datasets.items():
        if not os.path.exists(path):
            print(f"ERRORE: File {path} non trovato!")
            sys.exit(1)
        df = pd.read_csv(path)
        rows = len(df)
        if not (min_rows <= rows <= max_rows):
            print(f"ERRORE: {path} contiene {rows} righe (attese tra {min_rows} e {max_rows})")
            sys.exit(1)
        print(f"  [OK] {path}: {df.shape[0]} righe, {df.shape[1]} colonne")
    print("Tutti i dataset sono presenti e conformi.\n")

def test_notebooks_json():
    print(">>> 2. Controllo formato JSON dei notebook...")
    notebooks = glob.glob("*.ipynb")
    if not notebooks:
        print("ERRORE: Nessun notebook trovato!")
        sys.exit(1)
    for nb in notebooks:
        with open(nb, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "cells" not in data:
            print(f"ERRORE: {nb} non ha il campo 'cells'!")
            sys.exit(1)
        print(f"  [OK] {nb}: {len(data['cells'])} celle")
    print("Tutti i notebook hanno struttura JSON valida.\n")

def test_smoke_load():
    print(">>> 3. Smoke Test caricamento dati nei notebook...")
    for nb_name in ["IRIS.ipynb", "ADULT.ipynb", "OCEAN.ipynb"]:
        with open(nb_name, "r", encoding="utf-8") as f:
            nb = json.load(f)
        code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
        if len(code_cells) < 2:
            print(f"ERRORE: {nb_name} non ha abbastanza celle di codice!")
            sys.exit(1)
        
        globs = {"pd": pd, "np": np, "os": os}
        load_code = "".join(code_cells[1]["source"])
        try:
            exec(load_code, globs)
        except Exception as e:
            print(f"ERRORE caricamento in {nb_name}: {e}")
            sys.exit(1)
        
        df = globs.get("df")
        if df is None or df.empty:
            print(f"ERRORE: DataFrame vuoto in {nb_name}!")
            sys.exit(1)
        print(f"  [OK] {nb_name} data load riuscito: shape = {df.shape}")
    print("Tutti i notebook caricano i dati correttamente.\n")

if __name__ == "__main__":
    test_datasets()
    test_notebooks_json()
    test_smoke_load()
    print("========================================")
    print("TUTTI I TEST DI VALIDAZIONE COMPLETATI CON SUCCESSO!")
    print("========================================")
