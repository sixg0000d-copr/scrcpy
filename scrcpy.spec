%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        2.1.1

%forgemeta

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}

# .desktop files are malformed
# https://github.com/Genymobile/scrcpy/issues/3633
Patch0:         0001-Fix-exec-quotes-and-escapes.patch

BuildRequires:  meson gcc
BuildRequires:  java-devel >= 11
BuildRequires:  desktop-file-utils

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  vulkan-loader
# Always apply git patches correctly
BuildRequires:  git

Requires:       android-tools

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:     libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgeautosetup -S git

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{pkgname}{,-console}.desktop

%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/applications/%{pkgname}-console.desktop
%{_datadir}/bash-completion/completions/%{pkgname}
%{_datadir}/zsh/site-functions/_%{pkgname}

%changelog
* Mon Mar 13 2023 sixg0000d <sixg0000d@gmail.com> - 2.0-3
- New version
- Include missing for older Fedora versions

* Tue Feb 28 2023 sixg0000d <sixg0000d@gmail.com> - 1.25-3
- Fork from zeno/scrcpy
- Use original desktop files
- Fix desktop files exec quotes and escapes
