Title: How to install Bower on Ubuntu 14.04 LTS
Date: 2014-05-18
Category: How to
Summary: Bower is package management solution. It runs on Node.js and uses Git to
    fetch and install most packages. In this tutotial we will install Bower on Ubuntu
    14.04 LTS.
Tags: Ubuntu, Bower

## Easy way

    :::bash
    $ sudo apt-get install git-core
    $ sudo apt-get install nodejs nodejs-legacy
    $ sudo apt-get install npm

-   Install Bower

        :::bash
        $ sudo npm install -g bower    

## Reference

-   [How To Install and Use Bower on your VPS](https://www.digitalocean.com/community/articles/how-to-install-and-use-bower-on-your-vps)        
-   [How To Install Node.js on an Ubuntu 14.04 server](https://www.digitalocean.com/community/articles/how-to-install-node-js-on-an-ubuntu-14-04-server)
-   [error /usr/bin/env: node: No such file or directory](http://stackoverflow.com/questions/20886217/browserify-error-usr-bin-env-node-no-such-file-or-directory)
    Ubuntu specific error. We need to make link `ln -s /usr/bin/nodejs /usr/bin/node` or better use *nodejs-legacy* package:

        :::Bash
        $ sudo apt-get install nodejs-legacy
