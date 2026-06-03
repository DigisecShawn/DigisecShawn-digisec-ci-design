from pathlib import Path
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "assets/logo/png/logo-eng-black.png",
    "assets/logo/png/logo-eng-white.png",
    "assets/logo/png/auxiliary-logo-gray.png",
    "assets/logo/png/logo-ch-black.png",
    "assets/logo/png/logo-ch-en-black.png",
    "assets/logo/png/auxiliary-mark-orange.png",
    "assets/logo/source/DIGISEC-print-assets.ai",
    "assets/logo/source/DIGISEC-brand-guidelines.ai",
]

errors = []
print("DIGISEC brand asset validation")
print("=" * 34)
for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"Missing required file: {rel}")
        continue
    if path.suffix.lower() == ".png":
        try:
            with Image.open(path) as image:
                width, height = image.size
                print(f"OK  {rel}  {width}x{height}  {image.mode}")
        except Exception as exc:
            errors.append(f"Invalid PNG: {rel}: {exc}")
    else:
        print(f"OK  {rel}")

if errors:
    print("\nValidation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("\nAll required DIGISEC brand assets are present and readable.")
