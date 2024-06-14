<section data-background="img/hexagons.png" data-background-size="100%"
            data-background-position="50% 110%">
    <h1>openSUSEway</h1>
    <h3>sway DE: status update</h3>
    <div class="title-name">Denys Kondratenko</div>
    <div class="title-mail">stdden@opensuse.org</div>
    <aside class="notes">
        <ul>
            <li>Thank you for contributions! (icon, improvements, issues, packages)</li>
            <li>Previous talks: oSC20, oSC21</li>
            <li>excuses: new work, family</li>
        </ul> 
    </aside>
</section>



## Why
- sway: i3 compatible tiling Wayland [compositor](https://en.wikipedia.org/wiki/Compositing_window_manager)
- openSUSEway tries to get as close to DE as possible
  - packages, patterns
  - configs
  - themes

Note:
A compositing window manager, or compositor, is a window manager that provides applications with an off-screen buffer for each window. 
The window manager composites the window buffers into an image representing the screen and writes the result into the display memory.

https://wiki.archlinux.org/title/Wayland

Display servers using the Wayland protocol are called compositors because they also act as compositing window managers



## What do you need?
- https://en.opensuse.org/Portal:OpenSUSEway
- https://en.opensuse.org/Sway
- https://github.com/opensuse/opensuseway

Note:
go to the links
show that it is available during install



## Imperfections or honestly Issues
- installation that enables all services
- SELinux
- hardcoded paths
- user configuration management

Note:
Ppl that use Sway are already quite skilled, they tend to ignore and fix issues by themselves 


## Installation
- greetd is used as login manager
- current way requires xdm and update-alternatives
- procrastinating to go that way, happily accept contribution
- maybe Fedora way - systemd presets?

Note:
Way `display-manager.service` work on openSUSE. Currently to have your Login Manager(LM) or Display Manager (DM) enable you need to add `xdm` package as a dependency.
That package provides `display-manager.service` with a fancy (in a systemd work and my taste) `sysconfig`? way to start the DM:
https://build.opensuse.org/package/view_file/openSUSE:Factory/xdm/HOWTO.xdm?expand=1

Installer as well relies on `xdm` to determine if `graphical.target` should be enforced:
https://github.com/yast/yast-services-manager/blob/25f659aaa9b2fac2d2b8150f92f1512f319fc5cb/src/modules/services_manager_target.rb#L131

Fedora:
https://fedoraproject.org/wiki/Features/DisplayManagerRework
https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/85-display-manager.preset


## SELinux
- [greetd panic](https://github.com/openSUSE/openSUSEway/issues/55)
- affects systems where SELinux is enforced


## hardcoded paths
- [UsrEtc pam.d](https://todo.sr.ht/~kennylevinsen/greetd/19)
- [UsrEtc config](https://todo.sr.ht/~kennylevinsen/greetd/20)

Note:
- pam: this needs to be fixed upstream in Rust, maybe provide a build flag?
- pam: maybe there some Rust lib that detects it, need Rust experts


## user configuration management
- [Modularize config](https://github.com/openSUSE/openSUSEway/issues/49)
- user config utility / package manager to:
  - add configuration to the user's `.config`
  - add flapak flathub repo


Note:
dotfiles are the way, maybe some automation around it ? 

but not always a way.

It is probably more general issue:
- enable/start user services
- custom tools (kubectl)
toolbox not always works



## openSUSE way next steps
- remove imperfections
- MicroOS Desktop
- Fedora



## Questions?
<p><img src="img/chameleon.svg" style="max-height:300px;"></p>