Title: Things to do after installing ubuntu 14.04 LTS
Date: 2014-05-06
Modified: 2014-05-08
Category: How to
Tags: Ubuntu

## Update your Ubuntu 14.04 LTS

    :::bash
    $ sudo apt-get update 
    $ sudo apt-get upgrade

## Install usefull Apps

### Install **Restricted Extras**
There are some *Restricted Extras* in Ubuntu which can't be install while 
installation of Ubuntu by default but you can install these Restricted
extras by yourself. 

    :::bash
    $ sudo apt-get install ubuntu-restricted-extras

-   Classic Menu Indicator

    [Classic Menu Indicator Package](http://packages.ubuntu.com/trusty/classicmenu-indicator)
    
        :::bash
        $ sudo apt-get install classicmenu-indicator


-   SMPlayer        
    SMPlayer is great front-end for MPlayer with built-in codecs.

    SMPlayer can search and download subtitles from opensubtitles.org

    [SMplayer Package](http://packages.ubuntu.com/trusty/smplayer)

        :::bash 
        $ sudo apt-get install smplayer

    
    Once the SMPlayer is installed, the totem is no longer needed.

        :::bash
        $ sudo apt-get remove totem


-   Skype

    Uncomment the following lines in */etc/apt/sources.list* to enable Cannnonical Partners repository.

    - `deb http://archive.canonical.com/ubuntu trusty partner`
    - `deb-src http://archive.canonical.com/ubuntu trusty partner`

    Refresh package lists and install Skype through *apt*:
     
        :::bash
        $ sudo apt-get update
        $ sudo apt-get install skype


-   Guake Terminal

    **Guake** is great drop-down terminal for Gnome written in Python.

    Show / hide with *F12* key.

    [Guake Terminal Ubuntu Package](https://apps.ubuntu.com/cat/applications/guake/)        

        :::bash
        $ sudo apt-get install guake
    

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

1.  Download GPG key and install it.

        :::bash
        $ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        $ sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
        $ sudo chmod 644 /etc/apt/sources.list.d/google-chrome.list

2.  Update package lists:

        :::bash
        $ sudo apt-get update

3.  install **stable** version of Google Chrome

        :::bash
        $ sudo apt-get install google-chrome-stable


## Chromium browser

    :::bash
    $ sudo apt-get install chromium-browser
        

## Unity tunning

-   Resize Unity launchers icons

    Open *System Settings / Appereance / Look*.

    Drag the marker either direction to increase or decrease the icon size
    on the Unity launcher.

    The default size of the Unity Launcher icons is 48px in case you want to go back to the original size..


-   Turn On Workspaces
    
    Open *System Settings / Appereance / Behavior*

    Now you can re-enable worspaces with the *Enable Workspaces* checkbox.

    *Add show desktop icon to the launcher*


-   Remove "Show Desktop" icon from the app switcher

    To disable the "Show Desktop" option in application
    switcher you can use **unity-tweak-tool**.

        :::bash
        $ sudo apt-get install unity-tweak-tool

    And then, *Unity Tweak Tool / Switcher / Display "Show Desktop" icon*

    To Show Desktop (Minimise all windows) now use Ctrl + Super + D



### Disable overlay Scrollbars
You can disable overlay scrollbars, if you don't like that

To disable overlay scrollbar:

    :::bash
    $ gsettings set com.canonical.desktop.interface scrollbar-mode normal

To get back overlay bar to default:

    :::bash
    $ gsettings reset com.canonical.desktop.interface scrollbar-mode

## Clean Up

    :::bash
    $ sudo apt-get -f install
    $ sudo apt-get autoremove
    $ sudo apt-get -y autoclean
    $ sudo apt-get -y clean

[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/
[virtualenv]: https://pypi.python.org/pypi/virtualenv
[oh-my-zsh]: http://ohmyz.sh/
