## Runing the project

```bash
#create the environment
$ python3 -m venv .venv
#activate it by doing
$ source .venv/bin/activate
## Install requirements
$ pip install -r requirements.tx
```

## Get the list of first 5 unique manufacturers
```bash
python3 data_retrieve.py
```
[Note] I supposed when hitting the last page the API will return `None` value for `next`

### Get random CSV
```bash
## Running example
python3 random_csv_data_generator.py 8 sample.csv

## Running test
pytest
```

### Convert pipe into csv separated data files

```bash
python3 pipe_to_csv_separated_values.py ./test/resources/sample_data.txt sample_out.csv
```