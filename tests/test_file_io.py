import os
from pprint import pprint


from baseblock import FileIO


def test_temp():
    """ Test Ability to Write a Temp File """
    path = FileIO.temp({})
    assert os.path.exists(path)

    os.remove(path)
    assert not os.path.exists(path)


def test_local_directory_by_name():
    path = FileIO.local_directory_by_name('BastAI-Temp')
    assert os.path.exists(path)
    os.rmdir(path)
    assert not os.path.exists(path)


def test_parse_json():
    d_result = FileIO.parse_json("""{"x": "y"}""")
    assert d_result
    assert type(d_result) == dict


def test_load_all_files():

    input_dir = os.path.join(os.getcwd(), 'tests/test_dir')
    FileIO.exists_or_error(input_dir)
    d_files = FileIO.load_all_files(input_dir)
    pprint(d_files)


def test_load_all_folders():

    input_dir = os.path.join(os.getcwd(), 'tests/test_dir')
    FileIO.exists_or_error(input_dir)
    d_files = FileIO.load_all_folders(input_dir)
    pprint(d_files)


def test_parse_yaml():

    yaml_input = """
    test:
        - key1
        - key2
        - key3:
            - subkey1
    """

    d_result = FileIO.parse_yaml(yaml_input)
    assert d_result
    assert type(d_result) == dict


def test_join():
    assert FileIO.join('alpha/beta', 'gamma/delta',
                       'epsilon/digamma') == """alpha\\beta\\gamma\\delta\\epsilon\\digamma"""


def main():
    test_load_all_folders()


if __name__ == "__main__":
    main()
