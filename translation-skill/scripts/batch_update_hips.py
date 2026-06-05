import os
import subprocess
import sys
import shutil

CENTRAL_DIST = "/home/codata/projects/the-minority-report/data/distribution"
GENERATOR    = "/home/codata/projects/the-minority-report/translation-skill/scripts/croissant_generator.py"
HIPS_ROOT    = "/home/codata/projects/the-minority-report/hips"

def find_html_for_dataset(hips_code, central_dist):
    """Return the path to the HTML file whose name starts with <hips_code>_, or None."""
    prefix = hips_code + "_"
    for fname in os.listdir(central_dist):
        if fname.startswith(prefix) and fname.endswith(".html"):
            return os.path.join(central_dist, fname)
    return None

def run_generator(csv_path, source_dir, output_dir, hips_code):
    """Run croissant_generator.py with given paths."""
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        sys.executable,
        os.path.abspath(GENERATOR),
        "--data-file",   csv_path,
        "--output-dir",  output_dir,
        "--source-file", source_dir,
        "--hips-code",   hips_code,
        "--root-folder", "."
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR generating metadata for {hips_code}")
        print(result.stderr)
        return False
    return True

def main():
    hips_root    = os.path.abspath(HIPS_ROOT)
    central_dist = os.path.abspath(CENTRAL_DIST)

    if not os.path.isdir(hips_root):
        print(f"HIPS directory not found: {hips_root}")
        sys.exit(1)
    if not os.path.isdir(central_dist):
        print(f"Central distribution dir not found: {central_dist}")
        sys.exit(1)

    # Fix permissions so root can read files created by codata (mode 600)
    print("Fixing file permissions on final_translations.csv files...")
    os.system(f"find {hips_root} -name 'final_translations.csv' -exec chmod o+r {{}} \\;")
    print("Permissions fixed.\n")

    processed    = 0
    skipped      = 0
    errors       = 0
    html_found   = 0

    for entry in sorted(os.scandir(hips_root), key=lambda e: e.name):
        if not entry.is_dir():
            continue

        hips_code  = entry.name
        csv_path   = os.path.join(entry.path, "data", "final_translations.csv")
        source_dir = os.path.join(entry.path, "data", "distribution")
        output_dir = os.path.join(entry.path, "output")

        if not os.path.isfile(csv_path):
            print(f"Skipping {hips_code}: final_translations.csv not found")
            skipped += 1
            continue

        # Copy matching HTML from central distribution into per-dataset distribution/
        os.makedirs(source_dir, exist_ok=True)
        html_src = find_html_for_dataset(hips_code, central_dist)
        if html_src:
            dest = os.path.join(source_dir, os.path.basename(html_src))
            shutil.copy2(html_src, dest)
            print(f"{hips_code}: HTML found → {os.path.basename(html_src)}")
            html_found += 1
        else:
            print(f"{hips_code}: no HTML in central distribution (CSV only)")

        ok = run_generator(csv_path, source_dir, output_dir, hips_code)
        if ok:
            status = "✓ self-contained" if html_src else "✓ CSV only"
            print(f"  {status} → {output_dir}/metadata.json")
            processed += 1
        else:
            errors += 1

    print(f"\nDone. Processed: {processed} | HTML embedded: {html_found} | Skipped: {skipped} | Errors: {errors}")

if __name__ == "__main__":
    main()
