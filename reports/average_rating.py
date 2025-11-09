import sys
import tabulate

def print_average_rating(processed_dict: dict):
    if not processed_dict:
        print("No data to display.", file=sys.stderr)
        return
    
    sorted_items = sorted(
        processed_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )
    
    table_data = [
        [idx, brand, f"{avg_rating:.2f}"]
        for idx, (brand, avg_rating) in enumerate(sorted_items, start=1)
    ]
    
    print(tabulate.tabulate(
        table_data,
        headers=["", "Brand", "Average Rating"],
        tablefmt="github"
    ))
    
def generate_average_rating_report(data: list[dict]) -> dict:
    summary_dict = {}
    for row in data:
        if row['brand'] not in summary_dict:
            ratings_arr = []
            ratings_arr.append(row['rating'])
            summary_dict[row['brand']] = ratings_arr
        else:
            summary_dict[row['brand']].append(row['rating'])
            
    processed_dict = {}
    for brand in summary_dict.keys():
        ratings = summary_dict[brand]
        ratings_count = len(ratings)
        ratings_summ = 0
        for i in range(ratings_count):
            ratings_summ += float(ratings[i])
            
        processed_dict[brand] = ratings_summ / ratings_count
        
    return processed_dict