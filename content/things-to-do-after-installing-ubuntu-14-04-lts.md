Title: Things to do after installing ubuntu 14.04 LTS
Category: How to
Tags: Ubuntu

## Update your Ubuntu 14.04 LTS

    :::bash
    $ sudo apt-get update 
    $ sudo apt-get upgrade

## Install usefull Apps

Install **Multimedia Codecs**

    :::bash
    $ sudo apt-get install ubuntu-restricted-extras

Install some extra AppIndicators (applets)
Install **The Classic Menu Indicator**

    :::bash
    $ sudo add-apt-repository ppa:diesch/testing
    $ sudo apt-get update
    $ sudo apt-get install classicmenu-indicator

Replace videoplayer **Totem** with **SMPlayer**
Complete remove totem (*totem*, *totem-common*, *totem-plugins*)

    :::bash
    $ sudo apt-get remove totem

Install **SMPlayer**

    :::bash
    $ sudo apt-get install smplayer

## ZSH shell

### Install ZSH

    :::bash
    $ sudo apt-get install zsh

This will install *zsh* and *zsh-common* packages.

### Setup [oh-my-zsh][oh-my-zsh]

    :::bash
    $ wget --no-check-certificate http://install.ohmyz.sh -O - | sh
    $ chsh -s /bin/zsh

## Python Development

### Python headers files
Install package *python-dev*. This package includes header files, a static
library and development tools for building Python modules, extending the
Python interpreter or embedding Python in applications.

To install this package, enter:

    :::bash
    $ sudo apt-get install python-dev

### Virtualenv
Install [virtualenvwrapper][virtualenvwrapper] - extension to [virtualenv][virtualenv]
for managing multiple virtual Python environments

    :::bash
    $ sudo apt-get install virtualenvwrapper

### Pycharm

    :::bash
    $ sudo apt-get install openjdk-7-jdk
    $ cd ~/Downloads
    $ wget http://download.jetbrains.com/python/pycharm-professional-3.1.3.tar.gz
    $ cd /opt
    $ sudo cp ~/Downloads/pycharm-professional-3.1.3.tar.gz .
    $ sudo tar xvzf pycharm-professional-3.1.3.tar.gz .
    $ sudo mv pycharm-3.1.3/ pycharm/
    $ /opt/pycharm/bin/pycharm.sh


## Clean Up

    :::bash
    $ sudo apt-get -f install
    $ sudo apt-get autoremove
    $ sudo apt-get -y autoclean
    $ sudo apt-get -y clean

[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/
[virtualenv]: https://pypi.python.org/pypi/virtualenv
[oh-my-zsh]: http://ohmyz.sh/