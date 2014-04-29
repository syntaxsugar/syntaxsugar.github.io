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

## Clean Up

    :::bash
    $ sudo apt-get -f install
    $ sudo apt-get autoremove
    $ sudo apt-get -y autoclean
    $ sudo apt-get -y clean
