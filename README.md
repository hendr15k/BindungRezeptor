# Zielprotein Vorhersage (Target Prediction)

Willkommen auf der Webseite zur Vorhersage potenzieller Zielproteine von Molekülen basierend auf ihrer SMILES-Repräsentation. Dieses Projekt ist inspiriert von Tools wie SwissTargetPrediction.

## Über das Projekt

Dieses Projekt stellt eine Benutzeroberfläche bereit, um SMILES-Strings (Simplified Molecular Input Line Entry Specification) einzugeben und eine Liste wahrscheinlicher Zielproteine zu erhalten. Zusätzlich wird die chemische Struktur des Moleküls visualisiert.

Das Vorhersagemodell läuft direkt im Browser (Client-Side), nachdem es zuvor in Python trainiert und nach JavaScript exportiert wurde.

## Funktionsweise

1.  **Eingabe:** Der Nutzer gibt einen SMILES-String ein.
2.  **Datenabruf:** Das Frontend ruft Moleküleigenschaften (Molecular Weight, LogP, TPSA, etc.) von der PubChem API ab.
3.  **Vorhersage:** Ein Random Forest Classifier (trainiert auf ChEMBL-Daten) berechnet die Wahrscheinlichkeiten für verschiedene Zielproteine.
4.  **Visualisierung:** Die Struktur wird angezeigt und die Ergebnisse tabellarisch dargestellt.

## Verwendung

1.  Öffnen Sie die [Webseite](https://hendr15k.github.io/BindungRezeptor/).
2.  Geben Sie einen gültigen SMILES-String in das Eingabefeld ein (z.B. `CC(=O)OC1=CC=CC=C1C(=O)O` für Aspirin).
3.  Klicken Sie auf den Button **"Vorhersagen"**.
4.  Es erscheint die 2D-Struktur des Moleküls sowie eine Tabelle mit vorhergesagten Zielproteinen und deren Wahrscheinlichkeit.

**Hinweis:** Das Modell wurde auf einem kleinen Datensatz trainiert und dient Demonstrationszwecken.

## Technologien

*   HTML5 / CSS3 / JavaScript
*   PubChem API (für Bilder und Eigenschaften)
*   Python (scikit-learn, RDKit) für das Training
*   m2cgen (Model to Code Generator) für den Export nach JS

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
