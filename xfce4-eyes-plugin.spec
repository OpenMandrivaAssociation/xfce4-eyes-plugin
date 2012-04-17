%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	An eyes plugin for the Xfce panel
Name: 		xfce4-eyes-plugin
Version: 	4.4.1
Release: 	%mkrel 3
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	libxfcegui4-devel >= 4.8.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-eyes-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
An eyes plugin for the Xfce panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel-plugins/eyes.desktop
