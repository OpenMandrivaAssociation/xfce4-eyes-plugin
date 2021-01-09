%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	An eyes plugin for the Xfce panel
Name:		xfce4-eyes-plugin
Version:	4.5.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:  intltool
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)
BuildRequires:  xfce4-dev-tools
Obsoletes:	xfce-eyes-plugin

%description
An eyes plugin for the Xfce panel.

%prep
%autosetup -p1
libtoolize --force
aclocal -I %{_datadir}/xfce4/dev-tools/m4macros
autoconf

%build
%configure
%make_build

%install

%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel/plugins/eyes.desktop
