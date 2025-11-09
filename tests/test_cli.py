import pytest
from main import main

def test_cli_success():
    # Правильная команда
    argv = ['--files', 'source/products1.csv', 'source/products2.csv', '--report', 'average-rating']
    exit_code = main(argv)
    assert exit_code == 0


def test_cli_missing_files():
    argv = ['--report', 'average-rating']
    with pytest.raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code != 0  # обычно 2 для argparse


def test_cli_missing_report():
    argv = ['--files', 'a.csv']
    with pytest.raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code != 0


def test_cli_invalid_report():
    argv = ['--files', 'a.csv', '--report', 'invalid-report']
    with pytest.raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code != 0


def test_cli_no_arguments():
    argv = []
    with pytest.raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code != 0
    
def test_main_handles_unexpected_error(monkeypatch, capsys):
    def mock_file_reader(_):
        raise ValueError("Simulated failure")
    
    monkeypatch.setattr("main.file_reader", mock_file_reader)
    
    with pytest.raises(SystemExit) as exc_info:
        main(['--files', 'a.csv', '--report', 'average-rating'])
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Simulated failure" in captured.err