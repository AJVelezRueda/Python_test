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
python data_retrieve.py
```
[Note] I supposed when hitting the last page the API will return `None` value for `next`

### Get random CSV
```bash
python random_csv_data_generator.py 8 sample.csv
```