import sys
import csv

def file_reader(paths: list) -> dict:
    all_rows = []
    if paths:
        for path in paths:
            try:
                with open(path, 'r', newline='') as csvfile:
                    dict_reader = csv.DictReader(csvfile)
                    all_rows.extend(list(dict_reader))
            except FileNotFoundError:
                print(f"Error: File not found {path}", file=sys.stderr)
                sys.exit(1)             
    return all_rows