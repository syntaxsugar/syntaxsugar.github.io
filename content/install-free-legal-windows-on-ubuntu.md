Title: Install free legal Windows on Ubuntu
Date: 2017-02-18
Modified: 2017-02-18
Category: How to
Tagline: How to install Windows on Ubuntu 16.04 LTS in VirtualBox
Tags: Ubuntu, Windows, VirtualBox

<!-- PELICAN_BEGIN_SUMMARY -->
Install a free legal Windows in VirtualBox in Linux
<!-- PELICAN_END_SUMMARY -->

1) First install VirtualBoxand its extensions pack.

    :::bash
	$ sudo apt-get install virtualbox virtualbox-qt virtualbox-ext-pack

2) Add yourself to the group vboxusers

    :::bash
	$ sudo adduser USERNAME vboxusers

3) Now download a free legal VM with Windows 7 Enterprise (IE17 on Win7).

[https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)

You can use this legal VM with Windows 7 for 90 days. After those 90 days, you
can etend the activation five times. So you can use the Windows 7 VM legally for
6 x 90 = 540 days on total.

Select Virtual machine: *IE11 on win7*
Select platform: *VirtualBox*

Now click on *Download .zip*

4) Unzip the VM (it`s a .ova file).

    :::bash
	$ unzip IE11.Win7.For.Windows.VirtualBox.zip

5) Launch Oracle VM Virtualbox and select in its panel:
	File - Import Appliance...

Import the *.ova* file.

6) Click on the import VM - click Settings - USB - select *USB 2.0 (EHCI) Controller*

7) Now click on Snapshots and create a snapshot - for renewed activation when the
five activation extensions have been exhausted.