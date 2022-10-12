install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build

mypy:
	poetry run mypy baseblock
	poetry run stubgen .\baseblock\ -o .

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

pyc:
	poetry run python -c "import compileall; compileall.compile_dir('baseblock', optimize=2, force=True, legacy=True)"
	poetry run python -c "import compileall; compileall.compile_dir('baseblock', optimize=2, force=True, legacy=False)"

freeze:
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make build
#	20221012; too many errors
#	make mypy
	make linters
	make pyc
	make freeze
