#!/usr/bin/env python3
"""
Sincroniza lo que genera la rutina automática de Marea Creativa
(carruseles/<YYYY-MM-DD>/carrusel-N-tema/ y guiones/<YYYY-MM-DD>/*.txt)
hacia "Contenido Carrusel/Carrusel" y "Contenido Carrusel/Guiones",
sin duplicar ni pisar nada. Adaptado de sync_carruseles.py (Danny Mera Seguros).

Seguro de correr las veces que sea:
- Carruseles: para cada carrusel del repo, revisa si su contenido (por hash
  del primer PNG) ya existe en cualquier subcarpeta del día correspondiente.
  Si no, lo copia a la primera carpeta "Cn" libre.
- Guiones: para cada .txt del repo, revisa si su contenido (por hash del
  archivo) ya existe en la carpeta del día. Si no, lo copia con su nombre
  original (evitando pisar un archivo distinto con el mismo nombre).

Ignora carpetas de fecha que no sean exactamente YYYY-MM-DD (por ejemplo
"2026-09-18-ejemplo-manual", que es contenido de ejemplo, no generado por
la rutina diaria).
"""
import hashlib
import re
import shutil
import subprocess
from pathlib import Path

REPO = Path("/Users/danny/Marea Creativa")
CARRUSELES = REPO / "carruseles"
GUIONES = REPO / "guiones"
DEST_CARRUSELES = REPO / "Contenido Carrusel" / "Carrusel"
DEST_GUIONES = REPO / "Contenido Carrusel" / "Guiones"
LOG = REPO / "scripts" / "sync_contenido.log"

MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def file_hash(path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def day_folder_for(date_folder_name):
    m = DATE_RE.match(date_folder_name)
    if not m:
        return None
    anio, mes_num, dia = m.groups()
    mes_nombre = MESES[int(mes_num) - 1]
    return mes_nombre, anio, str(int(dia))


def first_image(folder):
    imgs = sorted(folder.glob("*.png")) or sorted(folder.glob("*.jpeg")) or sorted(folder.glob("*.jpg"))
    return imgs[0] if imgs else None


def already_saved_carrusel(day_folder, signature):
    if not day_folder.exists():
        return False
    for sub in day_folder.iterdir():
        if not sub.is_dir():
            continue
        img = first_image(sub)
        if img and file_hash(img) == signature:
            return True
    return False


def next_free_slot(day_folder):
    n = 1
    while (day_folder / f"C{n}").exists():
        n += 1
    return day_folder / f"C{n}"


def sync_carruseles():
    if not CARRUSELES.exists():
        log("No existe carpeta carruseles/, nada que hacer.")
        return 0

    copiados = 0
    for date_folder in sorted(CARRUSELES.iterdir()):
        if not date_folder.is_dir():
            continue
        parts = day_folder_for(date_folder.name)
        if not parts:
            continue
        mes_nombre, anio, dia = parts
        day_folder = DEST_CARRUSELES / f"{mes_nombre} {anio}" / dia

        for carrusel_folder in sorted(date_folder.iterdir(), key=lambda p: p.name):
            if not carrusel_folder.is_dir():
                continue
            img = first_image(carrusel_folder)
            if not img:
                continue
            signature = file_hash(img)

            if already_saved_carrusel(day_folder, signature):
                continue

            dest = next_free_slot(day_folder)
            dest.mkdir(parents=True, exist_ok=True)
            for f in carrusel_folder.glob("*.png"):
                shutil.copy2(f, dest / f.name)
            copiados += 1
            log(f"Carrusel copiado: {carrusel_folder} -> {dest}")

    return copiados


def already_saved_guion(day_folder, signature):
    if not day_folder.exists():
        return False
    for f in day_folder.glob("*.txt"):
        if file_hash(f) == signature:
            return True
    return False


def unique_name(day_folder, name):
    candidate = day_folder / name
    if not candidate.exists():
        return candidate
    stem, suffix = candidate.stem, candidate.suffix
    n = 2
    while (day_folder / f"{stem}-{n}{suffix}").exists():
        n += 1
    return day_folder / f"{stem}-{n}{suffix}"


def sync_guiones():
    if not GUIONES.exists():
        log("No existe carpeta guiones/, nada que hacer.")
        return 0

    copiados = 0
    for date_folder in sorted(GUIONES.iterdir()):
        if not date_folder.is_dir():
            continue
        parts = day_folder_for(date_folder.name)
        if not parts:
            continue
        mes_nombre, anio, dia = parts
        day_folder = DEST_GUIONES / f"{mes_nombre} {anio}" / dia

        for txt in sorted(date_folder.glob("*.txt")):
            signature = file_hash(txt)
            if already_saved_guion(day_folder, signature):
                continue
            day_folder.mkdir(parents=True, exist_ok=True)
            dest = unique_name(day_folder, txt.name)
            shutil.copy2(txt, dest)
            copiados += 1
            log(f"Guion copiado: {txt} -> {dest}")

    return copiados


def main():
    log(f"--- corrida {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()} ---")

    result = subprocess.run(
        ["git", "pull", "origin", "main", "--no-rebase", "--no-edit"],
        cwd=REPO, capture_output=True, text=True,
    )
    log("git pull: " + result.stdout.strip().replace("\n", " | ") + result.stderr.strip().replace("\n", " | "))

    n_carruseles = sync_carruseles()
    n_guiones = sync_guiones()
    log(f"Listo. Carruseles nuevos: {n_carruseles}. Guiones nuevos: {n_guiones}.")


if __name__ == "__main__":
    main()
