%define oname openAV-Sorcer
%define snapshot 20130702

Summary:	A wavetable LV2 plugin synth, targeted at the electronic / dubstep genre
Name:		openav-sorcer-lv2
Version:	0
Release:	0.%{snapshot}.1
License:	GPLv3+
Group:		Sound
Url:		https://github.com/harryhaaren/openAV-Sorcer
# from git
Source0:	%{oname}-%{snapshot}.tar.bz2
Patch0:		openAV-Sorcer-build.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
Requires:	lv2

%description
A wavetable LV2 plugin synth, targeted at the electronic / dubstep genre.

%prep
%setup -q -n %{oname}-%{snapshot}
%patch0 -p1

%build
%setup_compile_flags
./compileInstall.sh

%install
install -d %{buildroot}%{_libdir}/lv2/sorcer.lv2
install -t %{buildroot}%{_libdir}/lv2/sorcer.lv2 ./sorcer.lv2/*

%files
%{_libdir}/lv2/sorcer.lv2
