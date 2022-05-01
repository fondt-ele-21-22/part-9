import csv
import numpy as np
from matplotlib import pyplot as plt

def read_csv(fname):
    header, data = None, []
    with open(fname) as fp:
        reader = csv.reader(fp, quoting=csv.QUOTE_NONNUMERIC)
        for i, row in enumerate(reader):
            if i == 0:
                header = row # La prima riga del CSV contiene l'intestazione
            else:
                data.append(row) # ...Le altre righe contengono dati
    # Converto i dati in array
    data = np.array(data)
    # Restituisco i risultati
    return data, header


def scatter(x, y, xlabel=None, ylabel=None, figsize=None, add_bisector=False):
    plt.figure(figsize=figsize)
    plt.scatter(x, y)
    if add_bisector:
        l, u = min(min(x), min(y)), max(max(x), max(y))
        plt.plot([l, u], [l, u], color='tab:orange', linestyle=':')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(':')
    plt.show()

    
def plot(x, y, xlabel=None, ylabel=None, figsize=None):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(':')
    plt.show()
    
    
def fit(x_list, y):
    # Converto i vettori in colonne
    x_cols = [x.reshape(-1, 1) for x in x_list]
    # Ottengo la matrice dei coefficienti
    X = np.hstack(x_cols)
    # Risolvo il problema ai minimi quadrati
    sol, sse, _, _ = np.linalg.lstsq(X, y, rcond=None)
    # Restituisco il risultato
    return sol, sse[0] # sse[0] accede alla prima cella dell'array (i.e. è uno scalare)