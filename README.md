# Zielprotein Vorhersage (Target Prediction)

Willkommen auf der Webseite zur Vorhersage potenzieller Zielproteine von Molekülen basierend auf ihrer SMILES-Repräsentation. Dieses Projekt ist inspiriert von Tools wie SwissTargetPrediction.

## Über das Projekt

Dieses Projekt stellt eine Benutzeroberfläche bereit, um SMILES-Strings (Simplified Molecular Input Line Entry Specification) einzugeben und eine Liste wahrscheinlicher Zielproteine zu erhalten. Zusätzlich wird die chemische Struktur des Moleküls visualisiert.

Die Webseite ist für GitHub Pages optimiert und läuft vollständig im Browser.

## Verwendung

1.  Öffnen Sie die [Webseite](https://hendr15k.github.io/BindungRezeptor/).
2.  Geben Sie einen gültigen SMILES-String in das Eingabefeld ein (z.B. `CC(=O)OC1=CC=CC=C1C(=O)O` für Aspirin).
3.  Klicken Sie auf den Button **"Vorhersagen"**.
4.  Es erscheint die 2D-Struktur des Moleküls sowie eine Tabelle mit vorhergesagten Zielproteinen und deren Wahrscheinlichkeit.

**Hinweis:** Die aktuelle Version verwendet eine Simulation für die Vorhersagewerte, da kein komplexes Backend-Modell integriert ist. Die Molekülbilder werden über die PubChem API geladen.

## Technologien

*   HTML5
*   CSS3
*   JavaScript
*   PubChem API (für Bilder)

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
