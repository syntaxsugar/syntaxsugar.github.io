Title: How To install Phalcon on Ubuntu 14.04 LTS
Date: 2015-09-03
Modified: 2015-09-03

Install the requirements for Phalcon.

    :::bash
    $ sudo apt-get install php5-dev libpcre3-dev gcc make php5-mysql git-core autoconf
 
Clone the framework repo onto your system.

    :::bash
    $ git clone git://github.com/phalcon/cphalcon.git
    
Compile extension.
    
    :::bash
    $ cd cphalcon/build
    $ sudo ./install
    
Add extension to PHP and enable phalcon
    
    :::bash
    $ sudo echo "extension=phalcon.so" >> /etc/php5/mods-available/phalcon.ini
    $ sudo php5enmod phalcon
    
Restart Apache2
    
    :::bash
    $ sudo service apache2 restart    

Install specific version.

    :::bash
    $ git tag
    
    phalcon-v1.3.3
    phalcon-v1.3.4
    phalcon-v2.0.0
    phalcon-v2.0.7
    phalcon-v2.0.8

    $ git checkout tag/phalcon-v2.0.0

Install 2.0.2 version

    :::bash
    $ wget https://github.com/phalcon/cphalcon/archive/phalcon-v2.0.2.tar.gz
    $ tar xvzf phalcon-v2.0.2/
    $ cd build/
    $ sudo ./install
