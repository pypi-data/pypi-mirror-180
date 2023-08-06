
# Test


# Publish



```
python3 -m build

python3 setup.py sdist
python3 setup.py bdist_wheel --universal

#  python3 -m twine upload --repository jackals dist/*
twine upload dist/*

```

username : pbonazzi
password : pyetro23.py

```
python3 -m pip install --index-url https://test.pypi.org/project/jackals --no-deps jackals
```