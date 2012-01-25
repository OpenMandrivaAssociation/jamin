Name:		jamin
Summary:	Audio mastering from a mixed down multitrack source with JACK
Version:	0.95.0
Release:	%mkrel 11
License:	GPLv2+
Group:		Sound 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	%{name}-%{version}.tar.bz2
URL:		http://jamin.sourceforge.net/
BuildRequires:	perl(XML::Parser)
BuildRequires:	libjack-devel
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
%configure2_5x
%make

%install
%makeinstall_std

# we don't want this
rm -rf %{buildroot}%{_libdir}/ladspa/*.la

%find_lang %{name}
