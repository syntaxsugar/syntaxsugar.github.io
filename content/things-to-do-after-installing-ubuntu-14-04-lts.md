Title: Things to do after installing ubuntu 14.04 LTS
Date: 2014-05-06
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


## Google Chrome
Download GPG key and install it.

    :::bash
    $ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    $ sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    $ sudo chmod 644 /etc/apt/sources.list.d/google-chrome.list

Update packages list:

    :::bash
    $ sudo apt-get update

And install **stable** version Google Chrome

    :::bash
    $ sudo apt-get install google-chrome-stable

## Unity

### Turn On Workspaces
Open *Settings / Appereance / Behavior*

Now you can re-enable worspaces with the *Enable Workspaces* checkox.

And *Add show desktop icon to the launcher*

### Remove "Show Desktop" from the app switcher
To disable the "Show Desktop" option in application
switcher you can use **unity-tweak-tool**.

    :::bash
    $ sudo apt-get install unity-tweak-tool

And then, *Unity Tweak Tool / Switcher / Display "Show Desktop" icon*

## Clean Up

    :::bash
    $ sudo apt-get -f install
    $ sudo apt-get autoremove
    $ sudo apt-get -y autoclean
    $ sudo apt-get -y clean

[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/
[virtualenv]: https://pypi.python.org/pypi/virtualenv
[oh-my-zsh]: http://ohmyz.sh/
