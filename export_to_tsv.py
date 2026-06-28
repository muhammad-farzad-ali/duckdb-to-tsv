import csv
import os
from pathlib import Path

import duckdb

DB_PATH = Path(__file__).parent / "data" / "jobs_werkstudent_d1.duckdb"
OUTPUT_DIR = Path(__file__).parent / "output"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    conn = duckdb.connect(str(DB_PATH), read_only=True)

    tables = conn.execute("SHOW TABLES").fetchall()

    for (table_name,) in tables:
        rows = conn.execute(f'SELECT * FROM "{table_name}"').fetchall()
        columns = [desc[0] for desc in conn.description]

        tsv_path = OUTPUT_DIR / f"{table_name}.tsv"
        with open(tsv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(columns)
            writer.writerows(rows)

        print(f"{table_name}: {len(rows)} rows -> {tsv_path}")

    conn.close()


if __name__ == "__main__":
    main()
