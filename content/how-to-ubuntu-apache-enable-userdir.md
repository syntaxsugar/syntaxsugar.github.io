Title: How to enable UserDir in Ubuntu 12.04 LTS
Date: 2014-04-02
Category: How to
Tags: Apache, Ubuntu
Summary: Enable userdir, users can build websites with whis config.

## Configure for userdir

To enable the UserDir configuration on [Ubuntu 12.04 LTS](http://releases.ubuntu.com/12.04/), do the following:
Enable the userdir mod.

	:::bash
	$ sudo a2enmod userdir

Edit the userdir configuration file.

	:::bash
	$ sudo vim /etc/apache2/mods-enabled/userdir.conf

Change the **AllowOverride** line to:

	:::bash
	AllowOverride All

Change the **Options** line to:

	:::bash
	Options ExecCGI

Next, edit the php5 configuration file:

	:::bash
	$ sudo vim /etc/apache2/mods-enabled/php5.conf

Comment line *php_admin_value engine off**

Restart **apache2**

	:::bash
	$ sudo service apache2 restart
