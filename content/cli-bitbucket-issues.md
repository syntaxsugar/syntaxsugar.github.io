Title: Bitbucket Issues - CLI
Date: 2014-04-16 18:33:20 
Category: How to
Summary: How to install **bbi** - Command line interface to Bitbucket Issues.

[bbi](https://bitbucket.org/jsmits/bitbucket-issues-cli) provides an executable
called **bbi**, that can be used to access Bitbuckets issues from CLI.

## Installation
Install to $HOME dir, instead of system.

    :::bash
    pip install --user -e -e hg+https://bitbucket.org/jsmits/bitbucket-issues-cli#egg=bbi


Add local BIN to $PATH in *.zshrc* / *.bashrc*:

    :::bash
    # Local BIN directory
    [[ -d "$HOME/.local/bin" ]] && PATH=$PATH:$HOME/.local/bin
