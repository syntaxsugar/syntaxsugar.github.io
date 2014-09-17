Title: How to install Bower on Ubuntu 14.04 LTS
Date: 2014-05-18
Category: How to
Tags: Ubuntu, Bower

Bower is package management solution. It runs on Node.js and uses Git to
fetch and install most packages. In this tutorial we will install Bower on Ubuntu
14.04 LTS.


## Install bower on your Ubuntu

Bower requires git to be installed as some bower packages require it.
First thing is to install Git. You can install it with the following command:

	:::bash
	$ sudo apt-get install git-core

*Bower* depends on Node and npm so first you will need install NodeJs.

    :::bash
    $ sudo apt-get install nodejs

Now is NodeJs installed and executable as `/usr/bin/nodejs`

If you try run `/usr/bin/env node` this end with error:

	:::bash
	$ /usr/bin/env node
	/usr/bin/env: node: No such file or directory

Forget something like symlink. (`ln -s /usr/bin/nodejs /usr/bin/node`)
Just install *nodejs-legacy*. This package create a symlink for you.

	:::bash
    $ sudo apt-get install npm-legacy

Now NodejS work fine.

	:::bash
	$ /usr/bin/env node                 
	>

## Install npm

	:::bash
	$ sudo apt-get install npm


## Install Bower

	:::bash
    $ sudo npm install -g bower    

Check Bower version

	:::bash
	$ bower -v
	1.3.10

## Reference

-   [How To Install and Use Bower on your VPS](https://www.digitalocean.com/community/articles/how-to-install-and-use-bower-on-your-vps)        
-   [How To Install Node.js on an Ubuntu 14.04 server](https://www.digitalocean.com/community/articles/how-to-install-node-js-on-an-ubuntu-14-04-server)
-   [error /usr/bin/env: node: No such file or directory](http://stackoverflow.com/questions/20886217/browserify-error-usr-bin-env-node-no-such-file-or-directory)

    Ubuntu specific error. We need to make link `ln -s /usr/bin/nodejs /usr/bin/node` or better use *nodejs-legacy* package:

        :::bash
        $ sudo apt-get install nodejs-legacy
