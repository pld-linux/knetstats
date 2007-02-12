Summary:	KNetStats - network monitor that show RX/TX LEDs
Summary(pl.UTF-8):   KNetStats - monitor sieci pokazujący diody RX/TX
Name:		knetstats
Version:	1.6.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/knetstats/%{name}-%{version}.tar.bz2
# Source0-md5:	219f1a94170386621802355b33989ec9
URL:		http://knetstats.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple KDE network monitor that show RX/TX LEDs or numeric
information about the transfer rate of any network interface in a
system tray icon that's part of kde-extragear package.

Features:
- See network activity, transfer rate, speed chart, IP address, MAC
  address, etc. of any network interface (including local loopback).
- Support multiple network interfaces.
- See simple statistics (packets and bytes received and transmitted).
- Configurable Update Interval, View mode, Icon themes, etc.
- GPL'ed, you can use and modify for free (Following GPL conditions)
- Carrier on/off detection.

%description -l pl.UTF-8
Prosty monitor sieci dla KDE pokazujący w zasobniku systemowym diody
RX/TX lub informacje liczbowe o szybkości przesyłania danych przez
dowolny interfejs sieciowy. Jest to część pakietu kde-extragear.

Możliwości:
- pokazywanie aktywności sieci, szybkości przesyłania danych, wykresu
  szybkości, adresu IP, adresu MAC itp. dowolnego interfejsu
  sieciowego (włącznie z loopbackiem)
- obsługa wielu interfejsów sieciowych
- proste statystyki (pakiety i bajty odebrane i wysłane)
- konfigurowana częstotliwość uaktualniania, tryb przeglądania, motywy
  ikon itp.
- licencja GPL pozwalająca używać i modyfikować program bezpłatnie (na
  warunkach GPL)
- wykrywanie obecności nośnej

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
