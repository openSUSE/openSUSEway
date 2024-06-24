<section data-background="img/hexagons.png" data-background-size="100%"
            data-background-position="50% 110%">
    <h1>openSUSEway</h1>
    <h3>a Sway Desktop Environment for openSUSE</h3>
    <h3></h3>
    <div class="title-name">&emsp;&emsp;&ensp;Filippo Bonazzi and Denys Kondratenko</div>
    <div class="title-mail">filippo.bonazzi@suse.com &emsp;&emsp;&ensp;stdden@opensuse.org&nbsp;&nbsp;</div>
</section>



## Why

1. Tiling
   - simple, lightweight, keyboard-centric, good-looking, fun
2. Wayland
   - modern, secure, simple
3. Sway
   - 1 + 2 = 3
4. openSUSE

Note:
note


## What

- coherent collection of tools and configs
- openSUSE look out of the box
- simple to override*

Note:
  exec section in the main config:
   - notification daemon
   - screen lock
   - wob


## Who

Show picture from last year here?

Get consent from everybody

Note:
  - Started in 2020 by Denys
  - Presented at oSC in 2020, 2021, 2022
  - Small, growing contributor base ever since



## Features

- sway
- waybar
- wofi
- alacritty
- swaylock
- swaync
- wob
- greetd


## Sway

<img src="oSC24/sway.png">


## Sway

- openSUSE theme
- lock screen (swaylock)
- multimedia support (keys, touch, audio, etc)
- screenshots (grim)
- system mode menu
- Floating windows

Note:
  Multimedia: talks about touch, media buttons, audio, bluethoos


## Waybar

- Numbered workspaces, Geeko marks active
- Window title
- Tray area
- Widgets
  - zypper
  - scratchpad
  - calendar


## Wofi

<img src="oSC24/wofi.png" width="80%">

We are searching for a replacement


## Swaync

<img src="oSC24/swaync.png" width="30%">

<img src="oSC24/swaync1.png" width="37%">


## Greetd

TODO: add screenshots


## Live demo

Note:
  - Waybar
    - Workspaces
    - Widgets (zypper, bluetooth, calendar, Scratchpad)
    - notifications
      - push some with sway
    - Wob - volume, brithness
    - Screenshot menu
    - System menu



## Issues

installation needs to enable all services

```
sudo mv /etc/greetd/config.toml /etc/greetd/config.toml.org
sudo mv /etc/greetd/config.toml.way /etc/greetd/config.toml
sudo systemctl set-default graphical.target
sudo systemctl enable greetd
```


## Hardcodes

- hardcoded paths
- user configuration management


## MicroOS

  - SELinux
  - transactions


## Other projects

  - Greybeard
  - Moldavite



## ARM

- openSUSE supports variaty of ARM platforms
- ARM is rising


## Boot

- gfxboot is not supported
- packages could be excluded with `%ifarch x86_64 %{ix86}`


## Packages

- some packages aren't built/supported
  - alacritty
- needs additional config changes



## Future

- Support other login managers
- Better installer integration
- Edit screenshots with Swappy
- Exponential brightness control
- Fix issues

Note:
  - Simplify trying out openSUSEway desktop without greetd
  - Bluetooth
  - YaST


## How

- [GitHub](https://github.com/openSUSE/openSUSEway)
- [GitHub Project](https://github.com/openSUSE/openSUSEway/projects/1)
- [X11:Wayland/openSUSEway](https://build.opensuse.org/package/show/X11:Wayland/openSUSEway)

Happy to accept contributions :)



## Questions?
<p><img src="img/chameleon.svg" style="max-height:300px;"></p>
