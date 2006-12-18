Summary:	KNetStats - network monitor that show rx/tx LEDs
Summary(pl):	-
Name:		knetstats
Version:	1.6.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/knetstats/%{name}-%{version}.tar.bz2
# Source0-md5:	219f1a94170386621802355b33989ec9
URL:		http://knetstats.sourceforge.net
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple KDE network monitor that show rx/tx LEDs or numeric
information about the transfer rate of any network interface in a
system tray icon that's part of kde-extragear package.

Features:
- See network activity, transfer rate, speed chart, IP address, MAC
  address, etc of any network interface (including localloopback).
- Support multiple network interfaces.
- See simple statistics (packets and bytes received and transmitted).
- Configurable Update Interval, View mode, Icon themes, etc.
- GPL'ed, you can use and modify for free (Following GPL conditions)
- Carrier on/off detection.

%description -l pl
- -

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/%{name}
