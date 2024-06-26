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

<img src="oSC24/Team_openSUSEway.jpg" width="80%">

Note:
  General:

  - Started in 2020 by Denys
  - Presented at oSC in 2020, 2021, 2022
  - Small, growing contributor base ever since



## Features

<table>
  <tbody>
    <tr border-style:none>
      <td align="center"><ul>
          <li>sway</li>
          <li>waybar</li>
          <li>wofi</li>
          <li>alacritty</li>
        </ul>
      </td>
      <td>
      &emsp;&emsp;&emsp;&emsp;
      </td>
      <td align="center"><ul>
          <li>swaylock</li>
          <li>swaync</li>
          <li>wob</li>
          <li>greetd</li>
        </ul></td>
    </tr>
  </tbody>
</table>


## Sway

<img src="oSC24/sway.png">


## Sway

- openSUSE theme
- lock screen (swaylock)
- multimedia support (keys, touch, audio, etc)
- screenshots (grim)
- system mode menu
- floating windows

Note:
  Multimedia: talk about:

  - touch
  - media buttons
  - audio
  - bluetooth


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

<img src="oSC24/greetd.png">


## Live demo

Note:

  Features to show:

  - Waybar
    - Workspaces
    - Widgets (zypper, bluetooth, calendar, scratchpad)
  - notifications
    - push some with sway
  - Wob - volume, brightness
  - Screenshot menu
  - System menu



# Issues


## Installation

Needs to enable all services

```
sudo mv /etc/greetd/config.toml /etc/greetd/config.toml.org
sudo mv /etc/greetd/config.toml.way /etc/greetd/config.toml
sudo systemctl set-default graphical.target
sudo systemctl enable greetd
```

Note:
greetd-branding package?


## Hardcodes

- hardcoded paths
- user configuration management


## MicroOS

  - SELinux
  - transactions


### Other projects

  - Greybeard
  - Moldavite



## ARM

- openSUSE supports variety of ARM platforms
- ARM is rising

Note:
  JeOS

  - JeOS image + regular installations (1Gb xz, 3.9GB)
  - could create pre-built JeOS


## Boot

- gfxboot is not supported
- packages could be excluded:

  `%ifarch x86_64 %{ix86}`


## Packages

- some packages aren't built/supported
- needs additional config changes

Note:
  Possible issues:

  - alacritty was missing but now there
  - to minimize installation we might strip some packages: perl, python...
  - Mesa-dri-vc4 driver is needed for RPi 4



## Future

- Support other login managers
- Better installer integration
- Edit screenshots with Swappy
- Exponential brightness control
- Fix issues

Note:
  Other:

  - Simplify trying out openSUSEway desktop without greetd
  - Bluetooth
  - YaST


## How

- [GitHub](https://github.com/openSUSE/openSUSEway)
- [GitHub Project](https://github.com/openSUSE/openSUSEway/projects/1)
- [X11:Wayland/openSUSEway](https://build.opensuse.org/package/show/X11:Wayland/openSUSEway)
- [Telegram channel](https://t.me/openSUSEway)
- [openSUSE wiki Portal](https://en.opensuse.org/Portal:OpenSUSEway)

Happy to accept contributions :)



## Questions?
<p><img src="img/chameleon.svg" style="max-height:300px;"></p>
