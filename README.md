# verify_hash
Python script for verifying file hashes
Install the package using python pipenv
>pip install pipenv

>pipenv install

>pipenv run python .\verify_hash.cli.py --help
>pipenv run python .\verify_hash.cli_file.py --help

Build wheel
>hatch build

After installing the wheel you can run with
>verify-dir --help
>verify-file --help