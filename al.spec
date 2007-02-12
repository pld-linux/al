#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_with	tests		# perform "make check" (segfaults after tests)
#
Summary:	OSSP al - Assembly Line
Summary(pl.UTF-8):   OSSP al - biblioteka Assembly Line ("linii montażowej")
Name:		al
Version:	0.9.3
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/al/%{name}-%{version}.tar.gz
# Source0-md5:	ef943a29d1fb89ed4fd5556844cbc542
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

%description -l pl.UTF-8
OSSP al definiuje abstrakcyjne typy danych dla bufora danych, który
może łączyć, przemieszczać i ucinać porcje danych w strumieniu, ale
unika samego kopiowania. Została stworzona, aby obsługiwać wydajnie
strumienie komunikacyjne pomiędzy modułami oprogramowania. Udostępnia
w szczególności elastyczne semantyczne przypisywanie danych poprzez
oznaczanie porcji. Ma także wygodne metody przechodzenia porcji i
opcjonalną obsługę wyjątków w oparciu o OSSP ex.

%package devel
Summary:	OSSP al - Assembly Line - header files and development libraries
Summary(pl.UTF-8):   OSSP al - biblioteka Assembly Line - pliki nagłówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP al - Assembly Line - header files and development libraries.

%description devel -l pl.UTF-8
OSSP al - biblioteka Assembly Line - pliki nagłówkowe i biblioteki dla
deweloperów.

%package static
Summary:	OSSP al - Assembly Line - static libraries
Summary(pl.UTF-8):   OSSP al - biblioteka Assembly Line - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP al - Assembly Line - static libraries.

%description static -l pl.UTF-8
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
	%{?debug:--enable-debug} \
	--with-ex \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%endif
