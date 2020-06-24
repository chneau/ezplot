# ezplot
A plotter for population based results algorithm

## install

```bash
pip install -U git+https://github.com/chneau/ezplot
```

## cli usage

```bash
Usage: ezplot.py [OPTIONS] FILES...

  Process csv FILES to create meaningful plots.

Options:
  -f, --format TEXT             The output plots format ('png', 'pdf', 'svg', 
                                ...)  [default: png]

  -s, --size <FLOAT FLOAT>...   The output plots size  [default: 6.4, 4.8]    
  -c, --context TEXT            The output plot context (paper, notebook,     
                                talk, poster)  [default: talk]

  -r, --rcparam <TEXT TEXT>...  modify any matplotlib rcParams https://matplot
                                lib.org/tutorials/introductory/customizing.htm
                                l#a-sample-matplotlibrc-file

  --help                        Show this message and exit.
```

## example

```bash
$ ezplot examples/{1,2,3}\ elite.csv -r figure.dpi 200
plt.rcParams[figure.dpi] = 200
Plot size: (6.4, 4.8), format: png, context: talk
7 plots generated in 1.296875s.
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
