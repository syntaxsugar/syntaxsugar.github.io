Title: Adminer on Ubuntu
Date: 2014-09-17
Category: How to
Tagline: How to install Adminer on Ubuntu 14.04 LTS
Tags: Apache, PHP, Ubuntu, Database

<!-- PELICAN_BEGIN_SUMMARY -->
Adminer is full-featured database management tool written in PHP. conversely to
phpMyAdmin, it consisst of a single file ready to deply to the target server.
Adminer is available for MySQL, PostgreSQL, SQLite, MS SQL and Oracle.
<!-- PELICAN_END_SUMMARY -->

## Install Adminer on Ubuntu

Install Adminer on Ubuntu is very easy. Just type:

	:::bash
	$ sudo apt-get install adminer

Now Adminer should run on http://127.0.0.1/adminer/
But unfortunately, for same reason don`t run...

Need manualy make symlink to `/etc/apache2/conf-available/adminer.conf`

	:::bash
	$ sudo ln -s /etc/apache2/conf-available/adminer.conf /etc/adminer/apache.conf

And enable this conf.

	:::bash
	$ sudo a2enconf adminer.conf 
	Enabling conf adminer.
	To activate the new configuration, you need to run:
	  service apache2 reload

As system say: Reload apache

	:::bash
	$ sudo service apache2 reload
