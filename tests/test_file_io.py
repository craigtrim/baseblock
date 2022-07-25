import os


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

def main():
    test_temp()


if __name__ == "__main__":
    main()
