To Build and Deploy

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload dist/*
```