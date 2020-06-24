# ezplot
A plotter for population based results algorithm  
Tested with success on:
- `Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32`
- `Python 3.7.3 (default, Dec 20 2019, 18:57:59) [GCC 8.3.0] on linux`
- `Python 3.8.2 (default, Apr 27 2020, 15:53:34) [GCC 9.3.0] on linux`

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
