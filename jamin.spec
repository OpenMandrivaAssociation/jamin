Name:		jamin
Summary:	Audio mastering from a mixed down multitrack source with JACK
Version:	0.95.0
Release:	14
License:	GPLv2+
Group:		Sound 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://jamin.sourceforge.net/
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(jack)
BuildRequires:	fftw-devel
BuildRequires:	libxml2-devel
BuildRequires:	gtk2-devel
BuildRequires:	liblo-devel
Requires:	swh-plugins

%description
JAM is a tool for producing audio masters from a mixed down 
multitrack source. It runs in the JACK Audio Connection Kit, 
and uses LADSPA for its backend DSP work, specifically the 
swh plugins created by Steve Harris, JAM's main author.

Features:

 * Linear filters 
 * JACK i/o
 * 30band graphic EQ
 * 1023band graphic EQ
 * Spectrum analyser
 * 3band peak compressor
 * Lookahead brickwall limiter

Planned features (in rough order of difficulty):

 * Multiband stereo processing
 * Parametric EQ
 * Loudness maximiser
 * Presets and scenes

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/jamin
%{_bindir}/jamin-scene
%{_libdir}/ladspa/jamincont_1912.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.svg
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/mime/packages/%{name}.xml

#--------------------------------------------------------------------

%prep
%setup -q

#fix plugindir
sed -i -e 's|^plugindir =.*|plugindir = $(libdir)/ladspa|' controller/Makefile.in

%build
export LDFLAGS="-ldl"
%configure2_5x
%make

%install
%makeinstall_std

# we don't want this
rm -rf %{buildroot}%{_libdir}/ladspa/*.la

%find_lang %{name}


%changelog
* Wed Jan 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.95.0-11mdv2011.0
+ Revision: 768336
- see #65186 just rebuild

* Sun Oct 24 2010 Jani Välimaa <wally@mandriva.org> 0.95.0-10mdv2011.0
+ Revision: 589149
- clean and prettify .spec

* Sun Oct 24 2010 Jani Välimaa <wally@mandriva.org> 0.95.0-9mdv2011.0
+ Revision: 588986
- require swh-plugins (mdv#61409)

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.95.0-8mdv2010.1
+ Revision: 502929
- clean and fix rpmlint warning on spec

* Sun Jun 21 2009 Jérôme Brenier <incubusss@mandriva.org> 0.95.0-7mdv2010.0
+ Revision: 387551
- use configure2_5x
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.95.0-6mdv2009.0
+ Revision: 247382
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.0-4mdv2008.1
+ Revision: 116802
- Fix install on x86_64
- Fix Description
  Fix BuildRequires
  Remove old menu style

  + Thierry Vignaud <tv@mandriva.org>
    - fix hardcoded man page extension
    - import jamin

