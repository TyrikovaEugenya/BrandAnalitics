import pytest
from reports.average_rating import generate_average_rating_report, print_average_rating

def test_generate_average_rating_basic():
    data = [
        {"brand": "Apple", "rating": "5.0"},
        {"brand": "Apple", "rating": "3.0"},
        {"brand": "Samsung", "rating": "4.0"},
    ]
    result = generate_average_rating_report(data)
    assert result == {"Apple": 4.0, "Samsung": 4.0}
    
def test_generate_average_rating_multiple_files_merged():
    data = [
        {"brand": "A", "rating": "1.0"},
        {"brand": "B", "rating": "2.0"},
        {"brand": "A", "rating": "3.0"},
        {"brand": "B", "rating": "4.0"},
        {"brand": "A", "rating": "5.0"},
    ]
    result = generate_average_rating_report(data)
    assert result == {"A": 3.0, "B": 3.0}
    
def test_print_average_rating_empty_dict(capsys):
    print_average_rating({})
    out, err = capsys.readouterr()
    assert "No data to display." in err
