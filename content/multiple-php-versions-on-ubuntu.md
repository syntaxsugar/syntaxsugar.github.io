Title: Multiple PHP versions on Ubuntu
Date: 2014-09-13
Category: Misc
Tagline: How to install multiple PHP versions on Ubuntu 14.04 LTS with PHPFarm
Tags: PHPFarm, Apache, PHP, Ubuntu

Many of the site which work on, are running on old versions of PHP. Usually is not 
possible to upgrade. Thats reason, why I need to have several different versions of
PHP.  
PHPFarm allow multiple versions of PHP to be run concurerentry on the same machine.

## PHPFarm

We install it into `/opt` directory which is for 3rd party software in the linux
file hirearchy.

	:::bash
	$ sudo git clone https://github.com/cweiske/phpfarm.git /opt/phpfarm

### Compile Options

Now you are almost ready to compile PHP. The last task is to sort out the compile
options.

For a vanilla PHP you don't need to specify any compile options, however this will
leave you with a PHP that doesn`t have support for many of the things you need for
running web applications - such as support for databases, GD, curl, bzip2, etc.

Here is my *custom-options-5.4.sh* file:

	#!/bin/bash
	#gcov='--enable-gcov'
	configoptions="\
	--enable-bcmath \
	--with-mysqli \
	--with-curl \
	--with-gd \
	--enable-calendar \
	--enable-exif \
	--enable-ftp \
	--enable-mbstring \
	--enable-pcntl \
	--enable-soap \
	--enable-sockets \
	--enable-wddx \
	--enable-zip \
	--with-zlib \
	--with-gettext \
	--with-openssl \
	--with-pdo-mysql \
	--with-mcrypt \
	--enable-soap \
	--with-bz2 \
	--with-mysql \
	--with-iconv \
	$gcov"


### Compile Time

To now finally compile the version we just have to run the *compile.sh* file as root
and wait for the compile process to finish.

	:::bash
	$ cd /opt/phpfarm/src
	$ sudo ./compile.sh 5.4.32

This will download PHP 5.4.32 and buil it, using any custom compile options you have
set up.
When the compilation is complete you will find the PHP install in the `inst` directory
within PHPFarm and within the `bin` directory, which will include symlinks to your
compiled PHP files.

### Verify PHP

To verify we`ve correctly compile our version we can now run the PHP binary.

	:::bash
	$ /opt/phpfarm/inst/bin/php-5.4.32 -v
	PHP 5.4.32 (cli) (built: Sep 13 2014 21:05:58) (DEBUG)
	Copyright (c) 1997-2014 The PHP Group
	Zend Engine v2.4.0, Copyright (c) 1998-2014 Zend Technologies
	$ /opt/phpfarm/inst/bin/php-cgi-5.4.32 -v
	PHP 5.4.32 (cgi-fcgi) (built: Sep 13 2014 21:06:05) (DEBUG)
	Copyright (c) 1997-2014 The PHP Group
	Zend Engine v2.4.0, Copyright (c) 1998-2014 Zend Technologies
	

## Setup Apache

Enable the *fastcgi* module.

	:::bash
	$ sudo a2enmod fastcgi
	Enabling module fastcgi.
	To activate the new configuration, you need to run:
	  service apache2 restart


### Configure Apache

Now we have to configure Apache to use this as a FastCGI Handler. To do this we
add those lines *before* the “IncludeOptional mods-enabled/*.load” line.

	:::bash
	$ sudo vim /etc/apache2/apache2.conf

Add this:
 
	FastCgiServer /var/www/cgi-bin/php-cgi-5.4.32 -idle-timeout 240
	ScriptAlias /cgi-bin-php/ /var/www/cgi-bin/


Next we have to comment the second last line of the configuration of the FastCGI
module in `/etc/apache2/mods-available/fastcgi.conf`

	:::bash
	$ sudo vim /etc/apache2/mods-enabled/fastcgi.conf

And comment this line:

	FastCgiIpcDir /var/lib/apache2/fastcgi

This is how the file look now:

	<IfModule mod_fastcgi.c>
	  AddHandler fastcgi-script .fcgi
	  #FastCgiWrapper /usr/lib/apache2/suexec
	  #FastCgiIpcDir /var/lib/apache2/fastcgi
	</IfModule>



## Prepare file structure

	:::bash
	$ cd /var/www

If the `cgi-bin` isn`t already here create it

	:::bash
	$ sudo mkdir cgi-bin

For each version of PHP you intend to use make one of these files. Replace the ending with the version number
For PHP 5.4.32 we make file `php-cgi-5.4.32`

	:::bash
	$ sudo vim /var/www/cgi-bin/php-cgi-5.4.32

And fill the file with this:

	#!/bin/bash
	PHPRC="/opt/phpfarm/src/php-5.4.32/lib/php.ini"
	export PHPRC
 
	PHP_FCGI_CHILDREN=3
	export PHP_FCGI_CHILDREN
 
	PHP_FCGI_MAX_REQUESTS=5000
	export PHP_FCGI_MAX_REQUESTS
 
	exec /opt/phpfarm/inst/bin/php-cgi-5.4.32


We also need to make sure the file is actually executable:

	:::bash
	$ sudo chmod +x /var/www/cgi-bin/php-cgi-5.4.32


## Setup Virtualhost

The next step is to set up an Apache VirtualHost to use PHPfarm.
Add this snippet to your virtualhost configuration:

	AddHandler php-cgi .php
	Action php-cgi /cgi-bin-php/php-cgi-5.4.30
	<FilesMatch "\.php$">
		SetHandler php-cgi
	</FilesMatch>

For example my file `/etc/apache2/sites-available/test.dev.conf`:

	<VirtualHost 127.0.0.1:80>
		ServerName test.dev 
		DocumentRoot /var/www/test/httpdocs

		<Directory /var/www/test/httpdocs>
			Options Indexes FollowSymlinks Includes ExecCGI
			AllowOverride All
			Order allow,deny
			Allow from all
			Require all granted

			AddHandler php-cgi .php
			Action php-cgi /cgi-bin-php/php-cgi-5.4.32
			<FilesMatch "\.php$">
				SetHandler php-cgi
			</FilesMatch>
		</Directory>

		ErrorLog /var/www/test/log/error.log
		LogLevel info
		CustomLog /var/www/test/log/access.log combined
	</VirtualHost>

## Finish

Activate your site.

	:::bash
	$ sudo a2ensite test.dev.conf

Restart Apache

	:::bash
	$ sudo service apache2 restart


Now website test.dev should run on PHP 5.4.32
