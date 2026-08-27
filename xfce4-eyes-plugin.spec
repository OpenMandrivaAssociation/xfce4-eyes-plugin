%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	An eyes plugin for the Xfce panel
Name:		xfce4-eyes-plugin
Version:	4.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	meson
BuildRequires:	make
BuildRequires:  intltool
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:  xfce4-dev-tools
Obsoletes:	xfce-eyes-plugin

%description
An eyes plugin for the Xfce panel.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install

%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel/plugins/eyes.desktop
