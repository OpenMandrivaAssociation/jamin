Name:          jamin
Summary:       Audio mastering from a mixed down multitrack source with JACK
Version:       0.95.0
Release:       %mkrel 1
License:       GPL
Group:	       Sound 
Source0:       %{name}-%{version}.tar.bz2
URL: 	       http://jamin.sourceforge.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: perl(XML::Parser)
BuildRequires: libjack-devel
BuildRequires: fftw-devel
BuildRequires: libxml2-devel
BuildRequires: gtk2-devel
BuildRequires: liblo-devel

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

%post
%{update_menus}

%postun
%{clean_menus}


%files
%defattr(-,root,root)
%{_bindir}/jamin
%{_bindir}/jamin-scene
%{_libdir}/ladspa/jamincont_1912.la
%{_libdir}/ladspa/jamincont_1912.so
%{_datadir}/applications/jamin.desktop
%{_datadir}/icons/jamin.svg
%{_datadir}/jamin/examples/RIAA_EQ.jam
%{_datadir}/jamin/examples/default.jam
%{_datadir}/jamin/examples/jamin_ui
%{_datadir}/jamin/examples/marble_jamin_ui
%{_datadir}/jamin/pixmaps/JAMin_icon.xpm
%{_datadir}/jamin/pixmaps/JAMin_splash.jpg
%{_datadir}/jamin/pixmaps/LED_green_off.xpm
%{_datadir}/jamin/pixmaps/LED_green_on.xpm
%{_datadir}/jamin/pixmaps/LED_red.xpm
%{_datadir}/jamin/pixmaps/LED_yellow.xpm
%{_datadir}/jamin/pixmaps/about_image.png
%{_datadir}/jamin/pixmaps/brushed-steel.png
%{_datadir}/jamin/pixmaps/marble.jpg
%{_datadir}/jamin/pixmaps/pause1.png
%{_datadir}/jamin/pixmaps/play1.png
%{_datadir}/jamin/pixmaps/thai-gold-knobs.png
%{_datadir}/jamin/pixmaps/thai-gold.png
%{_datadir}/locale/ru/LC_MESSAGES/jamin.mo
%{_mandir}/man1/jamin.1.lzma
%{_datadir}/mime/packages/jamin.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%configure
%make

%install
make DESTDIR=%buildroot  install

%clean

