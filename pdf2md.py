import os, re, sys, pathlib, pymupdf4llm

source = pathlib.Path(sys.argv[1]).resolve()
pdfs = [source] if source.is_file() else sorted(source.glob("*.pdf"))

for pdf in pdfs:
    print(f"Conversion : {pdf.name}")
    # pymupdf4llm crée le dossier d'images tel quel, mais enregistre les images dans
    # un chemin « nettoyé » (espaces -> _, parenthèses/crochets -> -) relatif au cwd.
    # On fournit donc un nom déjà nettoyé et on se place dans le dossier du PDF.
    os.chdir(pdf.parent)
    image_dir = re.sub(r"[()\[\]]", "-", pdf.stem).replace(" ", "_") + "_images"
    md = pymupdf4llm.to_markdown(
        str(pdf),
        use_ocr=False,
        write_images=True,
        image_path=image_dir,
        image_format="png",
        dpi=150,
        margins=(0, 40, 0, 40),   # ignore en-têtes/pieds de page
    )
    pdf.with_suffix(".md").write_text(md, encoding="utf-8")

print("Terminé.")
