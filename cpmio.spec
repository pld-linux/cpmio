Summary:	CPMIO - console access functions of an emulated CP/M computer
Summary(pl):	CPMIO - funcje dostêpu do konsoli emulowanego komputera CP/M
Name:		cpmio
Version:	1.1.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/Zxcc/%{name}-%{version}.tar.gz
# Source0-md5:	0e1bd22ab7eb4ef9d11e0931dea7cdfc
Patch0:		%{name}-shared.patch
URL:		http://www.seasip.demon.co.uk/Unix/Zxcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPMIO is a library intended to support the console access functions of
an emulated CP/M computer, on a Unix box.

%description -l pl
CPMIO to biblioteka maj±ca obs³ugiwaæ funkcje dostêpu do konsoli
emulowanego komputera CP/M na maszynie uniksowej.

%package devel
Summary:	Header files for cpmio library
Summary(pl):	Pliki nag³ówkowe biblioteki cpmio
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	readline-devel

%description devel
Header files for cpmio library.

%description devel -l pl
Pliki nag³ówkowe biblioteki cpmio.

%package static
Summary:	Static cpmio library
Summary(pl):	Statyczna biblioteka cpmio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static cpmio library.

%description static -l pl
Statyczna biblioteka cpmio.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--with-readline

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
