# DuckDB to TSV

Exports all tables from a DuckDB database to individual TSV files.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python export_to_tsv.py
```

Outputs tab-separated `.tsv` files to `output/`, one per table.

## Project Structure

```
data/
  jobs_werkstudent_d1.duckdb   # Source database (gitignored)
output/                         # Generated TSV files (gitignored)
export_to_tsv.py                # Export script
requirements.txt                # Python dependencies
```
