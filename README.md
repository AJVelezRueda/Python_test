## Runing the project

```bash
#create the environment
$ python3 -m venv .venv
#activate it by doing
$ source .venv/bin/activate
```

## Get the list of first 5 unique manufacturers
```bash
python data_retrieve.py
```
[Note] I supposed when hitting the last page the API will return `None` value for `next`