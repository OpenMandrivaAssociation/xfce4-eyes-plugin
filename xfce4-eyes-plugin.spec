%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	An eyes plugin for the Xfce panel
Name:		xfce4-eyes-plugin
Version:	4.4.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1.0)
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-eyes-plugin

%description
An eyes plugin for the Xfce panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install

%makeinstall_std 

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel/plugins/eyes.desktop
