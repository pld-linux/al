#
# Conditional build:
%bcond_with	tests	# perform "make check" (segfaults after tests)
#
Summary:	OSSP al - Assembly Line
Summary(pl):	OSSP al - biblioteka Assembly Line ("linii monta¿owej")
Name:		al
Version:	0.9.1
Release:	0.3
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/al/%{name}-%{version}.tar.gz
# Source0-md5:	eba90e56fe7248466b66306a65868ae7
Patch0:		%{name}-ac.patch
URL:		http://www.ossp.org/pkg/lib/al/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ex-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP al defines an abstract data type of a data buffer that can
assemble, move and truncate chunks of data in a stream but avoids
actual copying. It was built to deal efficiently with communication
streams between software modules. It especially provides flexible
semantical data attribution through by-chunk labeling. It also has
convenient chunk traversal methods and optional OSSP ex based
exception handling.

%description -l pl
OSSP al definiuje abstrakcyjne typy danych dla bufora danych, który
mo¿e ³±czyæ, przemieszczaæ i ucinaæ porcje danych w strumieniu, ale
unika samego kopiowania. Zosta³a stworzona, aby obs³ugiwaæ wydajnie
strumienie komunikacyjne pomiêdzy modu³ami oprogramowania. Udostêpnia
w szczególno¶ci elastyczne semantyczne przypisywanie danych poprzez
oznaczanie porcji. Ma tak¿e wygodne metody przechodzenia porcji i
opcjonaln± obs³ugê wyj±tków w oparciu o OSSP ex.

%package devel
Summary:	OSSP al - Assembly Line - header files and development libraries
Summary(pl):	OSSP al - biblioteka Assembly Line - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP al - Assembly Line - header files and development libraries.

%description devel -l pl
OSSP al - biblioteka Assembly Line - pliki nag³ówkowe i biblioteki dla
deweloperów.

%package static
Summary:	OSSP al - Assembly Line - static libraries
Summary(pl):	OSSP al - biblioteka Assembly Line - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP al - Assembly Line - static libraries.

%description static -l pl
OSSP al - biblioteka Assembly Line - biblioteki statyczne.

%prep
%setup -q
%patch0 -p1

%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-ex
%{__make}

%{?with_tests:%{__make} check}

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
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
