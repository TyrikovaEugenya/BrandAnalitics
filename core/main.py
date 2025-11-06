import argparse
import csv
import sys
import config



def file_reader(paths: list) -> dict:
    summary_dict = {}
    if paths:
        for path in paths:
            try:
                with open(path, 'r', newline='') as csvfile:
                    dict_reader = csv.DictReader(csvfile)
                    for row in dict_reader:
                        if row['brand'] not in summary_dict:
                            ratings_arr = []
                            ratings_arr.append(row['rating'])
                            summary_dict[row['brand']] = ratings_arr
                        else:
                            summary_dict[row['brand']].append(row['rating'])
            except FileNotFoundError:
                print(f"Erorr: File not found {path}", file=sys.stderr)
                sys.exit(1)
            except PermissionError as e:
                raise RuntimeError(f"Permission denied reading '{path}': {e}") from e
            except csv.Error as e:
                raise RuntimeError(f"CSV parsing error in '{path}': {e}") from e
    else:
        print("Error: argument is empty", file=sys.stderr)   
        sys.exit(1)             
    return summary_dict


def dict_processor(summary_dict: dict) -> dict:
    processed_dict = {}
    for brand in summary_dict.keys():
        ratings = summary_dict[brand]
        ratings_count = ratings.len()
        ratings_summ = 0
        for i in range(ratings_count):
            ratings_summ += float(ratings[i])
            
        processed_dict[brand] = ratings_summ / ratings_count
        
    return processed_dict

def dict_printer(processed_dict: dict):
    

    
def main(parser):
    try:
        args = parser.parse_args()
        if args.report not in config.SUPPORTED_REPORTS:
            print(f"Error: Unsupported report type '{args.report}'. Supported: {config.SUPPORTED_REPORTS}", file=sys.stderr)
            sys.exit(1)
            
        if args.report == "average-rating":
            summary_dict = file_reader(args.files)
            processed_dict = dict_processor(summary_dict=summary_dict)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', type=str, nargs='+', required=True)
    parser.add_argument('--report', type=str)
    main(parser)
    