%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	An eyes plugin for the Xfce panel
Name:		xfce4-eyes-plugin
Version:	4.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	libxfce4ui-devel >= 4.9.0
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
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes/themes/*/*
%{_datadir}/xfce4/panel-plugins/eyes.desktop


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 4.4.1-3mdv2012.0
+ Revision: 791554
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 4.4.1-2
+ Revision: 790051
- Rebuild for xfce 4.10

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-1
+ Revision: 632789
- update to new version 4.4.1
- update url for Source0
- drop old scriplets

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-11mdv2011.0
+ Revision: 615598
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-10mdv2010.1
+ Revision: 543424
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 4.4.0-9mdv2010.0
+ Revision: 446019
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-8mdv2009.1
+ Revision: 349453
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-7mdv2009.1
+ Revision: 294994
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 4.4.0-6mdv2009.0
+ Revision: 262357
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.4.0-5mdv2009.0
+ Revision: 256864
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-3mdv2008.1
+ Revision: 110118
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING
- spec file clean
- use upstream name

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-2mdv2008.0
+ Revision: 31033
- add %%post and %%postun scripts

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-1mdv2008.0
+ Revision: 30530
- Import xfce-eyes-plugin

