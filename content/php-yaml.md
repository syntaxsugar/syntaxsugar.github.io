Title: Install PHP Extension YAML
Date: 2015-10-04
Modified: 2015-10-04

Install the requirements

    :::bash
    $ sudo apt-get install php-pear libyaml-dev
    $ sudo pecl install yaml
 
Add extension to PHP and enable YAML
    
    :::bash
    $ sudo sh -c "echo 'extension=yaml.so' >> /etc/php5/mods-available/yaml.ini"
    $ sudo php5enmod yaml
    
Restart Apache2
    
    :::bash
    $ sudo service apache2 restart    
