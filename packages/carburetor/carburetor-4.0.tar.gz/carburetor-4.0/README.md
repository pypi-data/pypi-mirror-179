# Carburetor

[![Translation status](https://hosted.weblate.org/widgets/carburetor/-/translations/svg-badge.svg)](https://hosted.weblate.org/engage/carburetor/?utm_source=widget)

This is a graphical settings app for tractor which is a package uses Python stem library to provide a connection through the onion proxy and sets up proxy in user session, so you don't have to mess up with TOR on your system anymore. 

## Install
On Ubuntu based distros, make sure that you have `software-properties-common` package installed an then do as following:

    sudo add-apt-repository ppa:tractor-team/tractor
    sudo apt update
    sudo apt install carburetor

If you are using a distro other than Ubuntu, please check if the release name in the relevant file located in `/etc/apt/sources.list.d/` is a supported one (e.g. jammy).

On Debian systems you may use up to the `hirsute` channel binaries, since it doesn't support the new compression algorithm. May be I try to setup a CI/CD pipeline for releasing Debian .debs.

For othe distros, the recommended method is by using [Python package index](https://pypi.org/project/carburetor/). However anyone is welcome in contributing native package build recepies for their distribution.

## Run
you can run `carburetor` by command line or through your desktop environment.
