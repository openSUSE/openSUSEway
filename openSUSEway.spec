#
# spec file for package openSUSEway
#
# Copyright (c) 2025 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sway_version %(rpm -q --queryformat "%%{version}" sway)
%define waybar_version %(rpm -q --queryformat "%%{version}" waybar)

Name:           openSUSEway
Version:        0.17.0
Release:        0
Summary:        The openSUSEway desktop environment meta package
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/openSUSEway
Source0:        %{name}-%{version}.tar.gz
Source1:        openSUSEway.rpmlintrc

BuildArch:      noarch
BuildRequires:  aaa_base
BuildRequires:  pkgconfig(systemd)

# system
Requires:       wget
Requires:       glibc-locale
Requires:       aaa_base
Requires:       bzip2
Requires:       command-not-found
Requires:       curl
Requires:       git
Requires:       grep
Requires:       gzip
Requires:       jq
Requires:       less
Requires:       sudo
Requires:       tar

# basic DE
Requires:       (gtkgreet or wlgreet)
Requires:       pipewire
Requires:       sway-marker
Recommends:     grim
Recommends:     slurp
Recommends:     firefox
Recommends:     bluetuith
Suggests:       mpv
Suggests:       vifm
Suggests:       vim
Suggests:       imv

# basic multi-media
Requires:       clipman
Requires:       wl-clipboard
Requires:       mpris-ctl

# branding
Requires:       waybar-branding-openSUSE
Requires:       sway-branding-openSUSE
Requires:       greetd-branding-openSUSE
%ifarch x86_64 %{ix86}
Requires:       gfxboot-branding-openSUSE
%endif

# xdg portals and utils
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-wlr
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-utils

# Appearance
Requires:       adwaita-icon-theme
Requires:       gtk3-metatheme-adwaita
Requires:       metatheme-adwaita-common
Recommends:     libqt5-qtwayland
Recommends:     qt5ct
Recommends:     adwaita-qt5

# Fonts
Requires:       adobe-sourcecodepro-fonts
Requires:       adobe-sourcesanspro-fonts
Requires:       adobe-sourceserifpro-fonts
Requires:       dejavu-fonts
Requires:       ghostscript-fonts-other
Requires:       ghostscript-fonts-std
Requires:       google-carlito-fonts
Requires:       google-droid-fonts
Requires:       google-opensans-fonts
Requires:       google-roboto-fonts
Requires:       noto-coloremoji-fonts
Requires:       noto-emoji-fonts
Requires:       noto-sans-fonts
Requires:       cantarell-fonts

%description
This meta-package aggregates openSUSEway desktop environment packages.

%package -n     patterns-openSUSEway
%pattern_graphicalenvironments
Summary:        The openSUSEway desktop environment pattern
Group:          Metapackages
Provides:       pattern() = openSUSEway
Provides:       pattern-icon() = pattern-sway
Provides:       pattern-order() = 1460
Provides:       pattern-visible()
URL:            https://github.com/openSUSE/openSUSEway
BuildRequires:  patterns-rpm-macros
Requires:       openSUSEway

%description -n patterns-openSUSEway
This pattern installs the openSUSE look and feel for sway.

%package -n     sway-branding-openSUSE
Summary:        openSUSE branding of sway
Group:          System/GUI/Other
BuildRequires:  sway
Requires:       SwayNotificationCenter
Requires:       brightnessctl
Requires:       fontawesome-fonts
Requires:       jq
Requires:       pamixer
Requires:       patterns-sway-sway
Requires:       pavucontrol
Requires:       playerctl
Requires:       polkit-gnome
Requires:       polkit-default-privs
Requires:       sway
Requires:       wallpaper-branding-openSUSE
Requires:       wob
Provides:       sway-branding = %{version}
Conflicts:      sway-branding
Supplements:    (sway and branding-openSUSE)

#BRAND: /etc/sway/config and /etc/sway/config.d/
#BRAND: contain openSUSE config and branding

%description -n sway-branding-openSUSE
This package provides the openSUSE look and feel for sway.

%package -n     waybar-branding-openSUSE
Summary:        openSUSE branding of waybar
Group:          System/GUI/Other
BuildRequires:  waybar
Provides:       waybar-branding = %{version}
Conflicts:      waybar-branding
Supplements:    (waybar and branding-openSUSE)
Requires:       adobe-sourcesanspro-fonts
Requires:       fontawesome-fonts

#BRAND: /etc/xdg/waybar/config.jsonc and /etc/xdg/waybar/style.css
#BRAND: contain openSUSE config and branding

%description -n waybar-branding-openSUSE
This package provides the openSUSE look and feel for waybar.

%package -n     greetd-branding-openSUSE
Summary:        openSUSE branding of greetd
Group:          System/Management
BuildRequires:  greetd
Provides:       greetd-branding = %{version}
Conflicts:      greetd-branding
Supplements:    (greetd and branding-openSUSE)

#BRAND: /etc/greetd/config, /etc/greetd/environments, /etc/greetd/sway-config,
#BRAND: and /etc/greetd/style.css contain openSUSE config and branding

%description -n greetd-branding-openSUSE
This package provides the openSUSE look and feel for greetd.

%prep
%autosetup -p1 -n openSUSEway-%{version}

%build

%install

## openSUSEway package
### qt5ct config to configure dark theme
install -D -p -m 644 qt5ct.conf %{buildroot}%{_sysconfdir}/xdg/qt5ct/qt5ct.conf

## greetd
install -D -p -m 644 greetd/config.toml     %{buildroot}%{_sysconfdir}/greetd/config.toml
install -D -p -m 644 greetd/environments    %{buildroot}%{_sysconfdir}/greetd/environments
install -D -p -m 644 greetd/style.css       %{buildroot}%{_sysconfdir}/greetd/style.css
install -D -p -m 644 greetd/sway-config     %{buildroot}%{_sysconfdir}/greetd/sway-config

## openSUSEway pattern package
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern openSUSEway to be installed.' >%{buildroot}%{_defaultdocdir}/patterns/openSUSEway.txt

## Sway
install -D -p -m 644 .config/sway/config %{buildroot}%{_sysconfdir}/sway/config
install -D -p -m 644 .config/sway/env %{buildroot}%{_sysconfdir}/sway/env
install -D -p -m 644 .config/sway/config.d/50-openSUSE.conf %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE.conf
install -D -p -m 644 .config/sway/config.d/55-openSUSE-windows.conf %{buildroot}%{_sysconfdir}/sway/config.d/55-openSUSE-windows.conf

install -D -p -m 644 sway/sway-session.target %{buildroot}%{_prefix}/lib/systemd/user/sway-session.target
install -D -p -m 644 sway/sway.service %{buildroot}%{_prefix}/lib/systemd/user/sway.service
install -D -p -m 644 sway/sway.desktop %{buildroot}%{_datadir}/wayland-sessions/sway.desktop.brand
install -D -p -m 755 sway/sway-run.sh %{buildroot}%{_bindir}/sway-run.sh

### alacritty
# so far doesn't have special branding package and it doesn't support system wide config
install -D -p -m 644 .config/alacritty/alacritty.toml %{buildroot}%{_sysconfdir}/alacritty/alacritty.toml

## wofi
install -D -p -m 644 .config/wofi/config %{buildroot}%{_sysconfdir}/wofi/config
install -D -p -m 644 .config/wofi/style.css %{buildroot}%{_sysconfdir}/wofi/style.css
#set wofi config and style to the system dir
sed -i -e "s|wofi --show.*|wofi --conf=%{_sysconfdir}/wofi/config --style=%{_sysconfdir}/wofi/style.css|g" %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE.conf

## waybar
install -D -p -m 644 .config/waybar/config.jsonc %{buildroot}%{_sysconfdir}/xdg/waybar/config.jsonc
install -D -p -m 644 .config/waybar/style.css %{buildroot}%{_sysconfdir}/xdg/waybar/style.css

## wob
install -D -p -m 644 .config/wob/wob.ini %{buildroot}%{_sysconfdir}/sway/wob/wob.ini

## swaync
install -D -p -m 644 .config/swaync/config.json %{buildroot}%{_sysconfdir}/sway/swaync/config.json
install -D -p -m 644 .config/swaync/style.css %{buildroot}%{_sysconfdir}/sway/swaync/style.css

## swaylock
install -D -p -m 644 .config/swaylock/openSUSEway.conf %{buildroot}%{_sysconfdir}/swaylock/openSUSEway.conf

%pre -n openSUSEway
# bug #1176195, don't force enviroment, cleaning up old installations
test -e %{_sysconfdir}/profile.d/openSUSEway.sh && rm %{_sysconfdir}/profile.d/openSUSEway.sh || true
test -e %{_prefix}/lib/environment.d/50-openSUSEway.conf && rm %{_prefix}/lib/environment.d/50-openSUSEway.conf || true

%pre -n sway-branding-openSUSE
%service_add_pre sway-session.target sway.service

%post -n sway-branding-openSUSE
test -e %{_datadir}/wayland-sessions/sway.desktop && \
    mv -n %{_datadir}/wayland-sessions/sway.desktop %{_datadir}/wayland-sessions/sway.desktop.orig || true
cp %{_datadir}/wayland-sessions/sway.desktop.brand %{_datadir}/wayland-sessions/sway.desktop
%service_add_post sway-session.target sway.service

%preun -n sway-branding-openSUSE
%service_del_preun sway-session.target sway.service

%postun -n sway-branding-openSUSE
test -e %{_datadir}/wayland-sessions/sway.desktop.orig && \
    mv %{_datadir}/wayland-sessions/sway.desktop.orig %{_datadir}/wayland-sessions/sway.desktop || true
%service_del_postun sway-session.target sway.service

%files
%dir %{_sysconfdir}/xdg/qt5ct/
%config(noreplace) %{_sysconfdir}/xdg/qt5ct/qt5ct.conf

%files -n greetd-branding-openSUSE
%dir %{_sysconfdir}/greetd/
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/greetd/config.toml
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/greetd/sway-config
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/greetd/environments
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/greetd/style.css

%files -n patterns-openSUSEway
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/openSUSEway.txt

%files -n sway-branding-openSUSE
%dir %{_sysconfdir}/sway
%config %{_sysconfdir}/sway/config
%config %{_sysconfdir}/sway/env
%dir %{_sysconfdir}/sway/config.d
%config %{_sysconfdir}/sway/config.d/50-openSUSE.conf
%config %{_sysconfdir}/sway/config.d/55-openSUSE-windows.conf
%{_prefix}/lib/systemd/user/sway-session.target
%{_prefix}/lib/systemd/user/sway.service
%{_datadir}/wayland-sessions/sway.desktop.brand
%{_bindir}/sway-run.sh

%dir %{_sysconfdir}/alacritty
%config(noreplace) %{_sysconfdir}/alacritty/alacritty.toml

%dir %{_sysconfdir}/wofi
%config(noreplace) %{_sysconfdir}/wofi/config
%config(noreplace) %{_sysconfdir}/wofi/style.css

%dir %{_sysconfdir}/sway/wob
%config %{_sysconfdir}/sway/wob/wob.ini

%dir %{_sysconfdir}/sway/swaync
%config %{_sysconfdir}/sway/swaync/config.json
%config %{_sysconfdir}/sway/swaync/style.css

%dir %{_sysconfdir}/swaylock
%config(noreplace) %{_sysconfdir}/swaylock/openSUSEway.conf

%files -n waybar-branding-openSUSE
%dir %{_sysconfdir}/xdg/waybar
%config(noreplace) %{_sysconfdir}/xdg/waybar/config.jsonc
%config(noreplace) %{_sysconfdir}/xdg/waybar/style.css

%changelog
