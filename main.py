import argparse
import sys
import config
from data_loader import file_reader
from reports.average_rating import generate_average_rating_report, print_average_rating

    
def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--files',
                        type=str,
                        nargs='+',
                        required=True
    )
    parser.add_argument('--report',
                        type=str,
                        required=True,
                        choices=config.SUPPORTED_REPORTS,
                        help=f"Report type. Supported: {', '.join(config.SUPPORTED_REPORTS)}"
    )
    
    try:
        args = parser.parse_args(argv)
        data = file_reader(args.files)
        
        match args.report:
            case "average-rating":
                result = generate_average_rating_report(data)
                print_average_rating(result)
                return 0
            case _:
                print(f"Unsupported report: {args.report}", file=sys.stderr)
                sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
    