%define name	jamin
%define version	0.95.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Audio mastering interface
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2

URL:		http://jamin.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig jackit-devel libxml2-devel gtk2-devel ladspa-devel
BuildRequires:	fftw-devel >= 3.0.1
BuildRequires:	liblo-devel
BuildRequires:  perl-XML-Parser
Requires:	jackit swh-plugins

%description
JAMin is the JACK Audio Connection Kit (JACK) Audio Mastering interface. JAMin
is designed to perform professional audio mastering of any number of input
streams. It uses LADSPA for its backend DSP work, specifically the swh plugins
created by Steve Harris.

Features:
Linear filters (though this seems to be going out of fashion, oh well)
JACK I/O
30 band graphic EQ
1023 band hand drawn EQ with parametric controls
Spectrum analyser
3 band peak compressor
Lookahead brickwall limiter
Multiband stereo processing
Presets and scenes
Loudness maximiser

%prep
%setup -q


%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="jamin" icon="sound_section.png" needs="x11" title="JAMIN" longtitle="Audio mastering interface" section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/jamin-scene
%{_bindir}/jamin
%{_libdir}/ladspa/%{name}cont_1912.la
%{_libdir}/ladspa/%{name}cont_1912.so
%{_menudir}/%name
%{_datadir}/%name
%{_mandir}/man1/jamin.1*
%{_datadir}/applications/jamin.desktop
%{_iconsdir}/jamin.svg
%{_datadir}/locale/ru/LC_MESSAGES/jamin.mo
%{_datadir}/mime/packages/jamin.xml


