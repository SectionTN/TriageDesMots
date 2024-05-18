from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array


def compter_espace(ch):
    nb = 0
    for i in range(len(ch)):
        if ch[i] == " ":
            nb += 1
    return nb + 1


def bulle(T, N):
    for i in range(N):
        for j in range(N-i-1):
            if len(T[j]) > len(T[j+1]):
                aux = T[j]
                T[j] = T[j+1]
                T[j+1] = aux

def convertir(T, N):
    ch = ""
    for i in range(N):
        ch = ch + T[i] + " "
    return ch

def trier(ch):
    N = compter_espace(ch)
    T = array([str] * N)
    debut = 0
    fin = ch.find(" ")
    for i in range(N):
        T[i] = ch[debut: fin]
        debut = fin + 1
        fin = ch.find(" ", fin + 1)
        if fin == -1:
            fin = ch.find(".")
    bulle(T, N)
    return convertir(T, N)

def Play():
    ch = window.phrase.text()
    if ch == "" or len(ch) > 50:
        message = "introduire un phrase"
    elif ch.find("  ") != -1:
        message = "entre deux mots un seul espace autorisé"
    elif ch[-1] != ".":
        message = "une phrase doit terminer par un point"
    elif not ("A" <= ch[0].upper() <= "Z"):
        message = "une phrase doit commencer par une lettre"
    else:
        message = trier(ch)
    window.resultat.setText(message)


application = QApplication([])
window = loadUi("InterfaceTriage.ui");
window.b_trier.clicked.connect(Play)
window.show()
application.exec_()
