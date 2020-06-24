# ezplot
A plotter for population based results algorithm

## uninstall

```bash
# on this directory
python setup.py install --record files.txt && rm -rf $(cat files.txt) files.txt

# force reinstall
pip install --ignore-installed -U .
```

## learnings

```bash
# evil good
pip install pigar
pigar --without-referenced-comments -o ">=" # Generate requirements.txt for current directory.
```

- check the site-packages directory of python to remove bad remaining directories
```
