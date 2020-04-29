# openSUSE way
dotfiles for Sway on openSUSE

Please check [Manage-dotfiles-with-Git](https://news.opensuse.org/2020/03/27/Manage-dotfiles-with-Git/) on how to use dotfiles.

For this config please install these packages:
```
sudo zypper in alacritty grim slurp fontawesome-fonts fontawesome-fonts-web sway swaybg swayidle swaylock mako pavucontrol waybar fzf brightnessctl pulseaudio pulseaudio-utils jq
```

`wofi` is an other application launcher option, if that isn't in Factory or repos, it is in the development project [X11:Wayland wofi](https://build.opensuse.org/package/show/X11:Wayland/wofi):
```
sudo zypper in wofi
```

Recommended packages for openSUSE way:
```
sudo zypper in gdm gdm-systemd sway gfxboot gfxboot-branding-openSUSE git jq libQt5WaylandClient5 libQt5WaylandCompositor5 setxkbmap command-not-found screen
```

[Sway openSUSE wiki page](https://en.opensuse.org/Sway) for more details.


Another dotfiles examples:
* https://github.com/jjquin/swayarch
* https://github.com/jjquin/dotfiles
