%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        1.22

%forgemeta

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}
Source2:        %{pkgname}.desktop

BuildRequires:  meson gcc
BuildRequires:  java-devel >= 11
BuildRequires:  desktop-file-utils

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)

Requires:       adb

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:     libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgesetup

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install
desktop-file-install %{S:2}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{pkgname}.desktop

%files
%license LICENSE
%doc README.md DEVELOP.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png
%{_datadir}/applications/%{pkgname}.desktop

%changelog
* Thu Jan 13 2022 sixg0000d <sixg0000d@gmail.com> 1.21-4
- add scrcpy.desktop

* Sun Nov 14 2021 zeno <zeno@bafh.org> 1.20-3
- fix runtime dependencies
