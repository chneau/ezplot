# ezplot
A plotter for population based results algorithm

## install

```bash
pip install -U git+https://github.com/chneau/ezplot
```

## uninstall

```bash
# on this directory
python setup.py install --record files.txt && rm -rf $(cat files.txt) files.txt

# installing not working?
rm -rf ezplot* # in python/lib/site-packages

# force reinstall
pip install --ignore-installed -U .
```

## learnings

```bash
# evil good
pip install pigar

# Generate requirements.txt for current directory.
pigar --without-referenced-comments -o ">="
```

- check the site-packages directory of python to remove bad remaining directories
