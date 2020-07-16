# openSUSE way
dotfiles for Sway on openSUSE

Please check [Manage-dotfiles-with-Git](https://news.opensuse.org/2020/03/27/Manage-dotfiles-with-Git/) on how to use dotfiles.

For this config please install these packages:
```
sudo zypper in openSUSEway
```

Add this to your ~/.profile:
```
set -a
. /etc/sway/env
set +a
```
that will import some recomended (optional) variables from `/etc/sway/env`

[Sway openSUSE wiki page](https://en.opensuse.org/Sway) for more details.

Another dotfiles examples:
* https://github.com/jjquin/swayarch
* https://github.com/jjquin/dotfiles
