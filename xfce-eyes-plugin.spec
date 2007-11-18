Summary: 	An eyes plugin for the Xfce panel
Name: 		xfce-eyes-plugin
Version: 	4.4.0
Release: 	%mkrel 2
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-eyes-plugin/xfce4-eyes-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
An eyes plugin for the Xfce panel.

%prep
%setup -qn xfce4-eyes-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-eyes-plugin

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-eyes-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel-plugins/eyes.desktop