Title: Create PyCharm package on Ubuntu
Date: 2014-05-13 22:30
Category: Ubuntu
Summary: How to create Ubuntu package for PyCharm.
Tags: Ubuntu, PyCharm


## Install all the packages needed for creating a .deb package

    $ sudo apt-get install build-essential autoconf automake autotools-dev dh-make debhelper devscripts fakeroot xutils lintian pbuilder
    $ sudo apt-get install packaging-dev

## Setting up the directory structure

- **Create the top directory**

Create a directory to work in first. We want to package the PyCharm app, so we'll chose a 
fifting name for it: **pycharm** - Make a directory called *pycharm* using:

    $ mkdir pycharm    

- **Create the packaging dir**

In the new *pycharm* directory create another directory to place the package files you'll be
creating. The name of this directory should consider with the version of the package using a 
dash between the package name and the package version. The resulting directory is *pycharm/pycharm-3.1.3*

- **Create the original files dir**

In the new *pycharm-3.1.3* directory extract the downloaded archive into a new *pycharm_3.1.3* subdirectory.

    $ pwd
    /home/paiti/Downloads/packages/pycharm/pycharm-3.1.3
    $ wget http://download.jetbrains.com/python/pycharm-professional-3.1.3.tar.gz
    $ tar xvzf pycharm-professional-3.1.3.tar.gz
    $ mv pycharm-3.1.3/ pycharm_3.1.3/
    $ rm -rf pycharm-professional-3.1.3.tar.gz


## Debianizing the package

- **Create the package control files.**

In the `pycharm/pycharm-3.1.3/`' directory run `dh_make --single --native`. The dh_make command will create the
debian directory and populate the example templates.

- **Remove the unnecessary files.**

For this application, in the *debian* directory remove all files with the *.ex* and *.EX* extensions
and all *README.* files as they are not needed for the native application being built.

    $ pwd
    /home/paiti/Downloads/packages/pycharm/pycharm-3.1.3
    $ cd  debian/
    $ rm -rf *.ex *.EX README.*

- **Create the installation script.**

During installation of the application the files need to be copied into the */opt/jetbrains/pycharm* directory.
Edit (Create a new file) *pycharm/pycharm-3.1.3/debian/install* adding the lines below to place the
files in their proper location during installation.

    pycharm_3.1.3/* opt/jetbrains/pycharm


## building the package

- **Update the changelog.**

Ensure you are in the *pycharm/pycharm-3.1.3/* directory and run `dch` to update the *changelog*.

The package name at the top of the *changelog* should be `pycharm (3.1.3-0ubuntu1) UNRELEASED; urgency=medium`

**3.1.3-0ubuntu1** - means that there was not a debian package yet and this is the 1st ubuntu version of
package 3.1.3 [ubuntu package version naming](http://www.ducea.com/2006/06/17/ubuntu-package-version-naming-explanation/)

1.  **Build the binary package**

    From the directory *pycharm/pycharm-3.1.3* run `debuild -b -uc -us` to build unsigned binary package.

2.  **Check out the output**

    The output is a file named *pycharm_3.1.3-0ubuntu1_amd64.deb*

3.  **Install and verify the binary package.**

    In order to verify the build worked run:

    
        $ sudo dpkg -i pycharm_3.1.3_amd64.deb


