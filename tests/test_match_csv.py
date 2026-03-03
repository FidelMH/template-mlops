import pandas as pd
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from modules.mon_module import add, sub, square, print_data


@pytest.fixture
def sample_df():
    return pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])

def test_add(a, b, expected):
    assert add(a, b) == expected


def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5
    assert sub(3, 3) == 0


def test_square():
    assert square(3) == 9
    assert square(0) == 0
    assert square(-4) == 16


def test_print_data(sample_df, capsys):
    result = print_data(sample_df)
    assert result == 2
    captured = capsys.readouterr()
    assert "Alice" in captured.out


def test_csv_loading():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "app", "moncsv.csv")
    df = pd.read_csv(csv_path)
    assert len(df) == 5
    assert list(df.columns) == ["name", "age", "score"]
