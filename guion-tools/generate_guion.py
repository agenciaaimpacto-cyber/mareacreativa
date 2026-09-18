#!/usr/bin/env python3
"""
Genera un guion de video (.txt) para grabar, a partir de un archivo JSON.
Dos formatos soportados: "camara" (hablado a camara) y "voz_en_off".

Uso:
  python3 generate_guion.py guion.json output_dir/

Formato de guion.json:
{
  "formato": "camara",
  "pilar": "espejo",
  "titulo": "La agenda vacia de mañana",
  "hook": "Si ahora mismo revisaste tu agenda de mañana con miedo, este es para ti.",
  "desarrollo": [
    "Sabes exactamente lo que se siente: un dia bueno y al otro dia nada.",
    "No es que no sepas hacer tu pega. Es que la gente que te necesita no te esta encontrando."
  ],
  "cta": "Si esto te paso hoy, escribenos. Partimos por entender tu negocio, no por venderte nada.",
  "notas_produccion": "Grabar con luz natural, camara a la altura de los ojos."
}

Duracion objetivo (definido el 17-sep-2026, ver contenido/banco-contenido.md):
  - camara:      30-45 segundos
  - voz_en_off:  45-60 segundos
"""
import json
import os
import sys

DURACION = {
    "camara": "30-45 segundos",
    "voz_en_off": "45-60 segundos",
}

NOTAS_FORMATO = {
    "camara": (
        "Hablado a camara. Mirar directo al lente, tono conversacional (como si le "
        "hablaras a una persona, no a una audiencia). Hook en los primeros 3 segundos: "
        "decirlo de pie o con un gesto que corte el scroll, no sentado y estatico."
    ),
    "voz_en_off": (
        "Voz en off sobre visuales/texto en pantalla. Cortar de escena/plano cada 2-3 "
        "segundos para mantener el ritmo. El hook debe coincidir con el primer corte de "
        "imagen, no con un plano largo."
    ),
}


def build_script(data):
    formato = data["formato"]
    duracion = DURACION.get(formato, "30-60 segundos")
    lines = []
    lines.append(f"GUION — {data.get('titulo', 'Sin titulo')}")
    lines.append(f"Formato: {formato} | Pilar: {data.get('pilar', '-')} | Duracion objetivo: {duracion}")
    lines.append("=" * 60)
    lines.append("")
    lines.append("[HOOK — primeros 3 segundos]")
    lines.append(data["hook"])
    lines.append("")
    lines.append("[DESARROLLO]")
    for i, beat in enumerate(data.get("desarrollo", []), start=1):
        lines.append(f"{i}. {beat}")
    lines.append("")
    lines.append("[CIERRE / CTA]")
    lines.append(data["cta"])
    lines.append("")
    lines.append("-" * 60)
    lines.append("NOTA DE FORMATO:")
    lines.append(NOTAS_FORMATO.get(formato, ""))
    if data.get("notas_produccion"):
        lines.append("")
        lines.append("NOTAS DE PRODUCCION:")
        lines.append(data["notas_produccion"])
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 3:
        print("Uso: generate_guion.py guion.json output_dir/")
        sys.exit(1)
    guion_path, out_dir = sys.argv[1], sys.argv[2]
    with open(guion_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    os.makedirs(out_dir, exist_ok=True)
    slug = data.get("titulo", "guion").lower()
    slug = "".join(c if c.isalnum() else "-" for c in slug).strip("-")
    out_path = os.path.join(out_dir, f"{slug}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_script(data))
    print(f"Guardado {out_path}")


if __name__ == "__main__":
    main()
