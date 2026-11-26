# convert-Pdf2Md

Script Python qui convertit des fichiers PDF en Markdown, avec extraction des images en PNG.

## Installation

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Utilisation

```powershell
# Un seul PDF
python pdf2md.py cours.pdf

# Tous les PDF d'un dossier
python pdf2md.py dossier\
```

## Résultat

Pour chaque PDF, à côté du fichier source :

- `nom.md` : le contenu converti en Markdown ;
- `nom_images/` : les images extraites (PNG, 150 dpi). Les espaces du nom sont remplacés par `_` et les parenthèses ou crochets par `-`.

Les marges haute et basse (40 pt) sont ignorées pour écarter les en-têtes et pieds de page. L'OCR est désactivé : un PDF scanné sans texte ne sera pas converti correctement.

## Dépendances

- Python 3
- [pymupdf4llm](https://pypi.org/project/pymupdf4llm/)

## Dépannage

### `warning: LF will be replaced by CRLF the next time Git touches it`

Cet avertissement s'affiche lors d'un `git add` ou d'un `git commit` sous Windows. Il est sans conséquence : le fichier est stocké avec des fins de ligne LF dans le dépôt, et Git les convertit en CRLF dans le dossier de travail (réglage `core.autocrlf=true`).

Pour ne plus voir l'avertissement :

```powershell
# Désactiver la conversion (garder LF partout)
git config core.autocrlf false
```

Ou ajouter un fichier `.gitattributes` avec `* text=auto` pour fixer le comportement dans le dépôt.
