Title: PhpStorm on Ubuntu
Date: 2014-08-31
Category: Misc
Tagline: How to install PhpStorm on Ubuntu 14.04 LTS
Tags: PhpStorm, PHP, Ubuntu

JetBrains PhpStorm is a commercial, cross-platform IDE for PHP built on JetBrains' IntelliJ IDEA platform.
PhpStorm is built on IntelliJ IDEA, which is written in Java.

## Install Oracle Java JDK

-   Step 1: Remove existing OpenJDK

        :::bash
        $ sudo apt-get purge openjdk*

-   Step 2: Install Oracle Java 8

        :::bash
        $ sudo add-apt-repository ppa:webupd8team/java
        $ sudo apt-get update
        $ sudo apt-get install oracle-java8-installer

-   Step 3: Set Java Environment Variable

        :::bash
        $ sudo apt-get install oracle-java8-set-default


## Download *PhpStorm* package and move to /opt directory

    :::bash
    $ cd /tmp
    $ curl -s -L http://download.jetbrains.com/webide/PhpStorm-7.1.4.tar.gz | tar -xz
    $ sudo mv PhpStorm-133.1777 /opt/phpstorm

## Run PhpStorm and Create desktop entry

    :::bash
    $ /opt/phpstorm/bin/phpstorm.sh

Now run "Tools > Create Desktop entry"
