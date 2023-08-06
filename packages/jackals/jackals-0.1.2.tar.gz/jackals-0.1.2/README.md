# Publish

```
rm -rf dist/
rm -rf build/
rm -rf .eggs/

python3 -m build
python3 setup.py sdist
python3 setup.py bdist_wheel --universal
twine upload dist/*

```

# Install

```
pip install -i https://test.pypi.org/simple/ jackals
```