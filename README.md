# Viper-ERC
ERC Token Standard implementation on Viper (primarily based on ERC20, adopting improvements/suggestions from EIPs )

# Viper Installation 
Don't panic if installation fails, Viper is still under development and constant changes. Installation will be much simplified/optimized after a stable version release. 

Take a deep breath and follow, please create an issue if any errors encountered. 

It is **strongly recommended** to install in **a virtual Python environment (normally either `virtualenv` or `venv`)**, so that new packages installed and dependencies built are strictly contained in your viper project and will not alter/affect your other dev environment set-up.

To find out how to set-up virtual environment, check out: [virtualenv guide](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)


- Ubuntu (16.04 LTS)
1. Package update:
```
sudo apt-get update 
sudo apt-get -y upgrade

```

2. For Viper to run, Python3.6 or later is required, know your python version, if the output is `Python 3.5.2`, then install python3.6, otherwise skip step 3
```
python3 -V
```

3. Install python3.6 and some necessary package (*if you haven't installed the package*)
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update

sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev python3.6-dev python3.6
```
4. Install `setuptools` package 
`pip3 install setuptools`

5. Before testing, make sure you already have pyethereum cloned on branch state_revamp
```
git clone https://github.com/ethereum/pyethereum/
git checkout state_revamp
python3.6 setup.py install (or: python setup.py install (both work)
```

6. Now, we are talking business, clone this Viper repo and install and test, and Walla!
```
git clone https://github.com/ethereum/viper.git
cd viper 
python3.6 setup.py install
python3.6 setup.py test
```

7. Oh, One more thing: by the time of writing, this bug has been fixed, but depending on when did you clone the Viper Repo, if during `python3.6 setup.py install`, there is an error with `tester2`, that's because of the following bug in `viper/tests/test_parser.py`.
```
change `tester2` into `tester`
```
MacOS


# Compile 
To compile your file, use:
```
viper yourFileName.v.py
```

**Note: Since .vy is not official a language supported by any syntax highlights or linter, it is recommended to name your viper file into `.v.py` to have a python highlights.**
