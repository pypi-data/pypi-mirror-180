## CI Deployment

1. Update `setup.py` with new version
2. Update `CHANGELOG.md` with description of new version
2. Create new tag with same version

```
git tag v0.4.1 -m "v0.4.1"
git push --tags
```

3. Create new release using GitHub Web Site. Github action will run automatically to deploy to PyPi.

## Manual Deployment

```bash
pip install -r requirements-build.txt

python setup.py sdist bdist_wheel
twine check dist/*
# Publish
twine upload dist/*
```