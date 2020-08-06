from pathlib import Path


def get_test_data_path() -> Path:
    data_path = Path(Path(__file__).parent.parent.parent, 'tests/data')
    assert data_path.exists()
    return Path(Path(__file__).parent.parent.parent, 'tests/data')


def get_test_data_file(filename: str) -> str:
    data_file = Path(get_test_data_path(), filename)
    if not data_file.is_file():
        raise FileNotFoundError(f"{data_file}")
    return str(data_file)


if __name__ == "__main__":
    print(get_test_data_path())