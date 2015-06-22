Name:           c-ares
Version:        1.10.0
Release:        0
License:        MIT
Summary:        Library for asynchronous name resolves
Group:          Development/Libraries/C and C++
Source:         http://daniel.haxx.se/projects/c-ares/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	c-ares.manifest
BuildRequires:  pkg-config
BuildRequires:  libtool
Url:            http://daniel.haxx.se/projects/c-ares

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n libcares
Summary:        Library for asynchronous name resolves
Group:          Development/Libraries/C and C++

%description -n libcares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n libcares-devel
Summary:        Library for asynchronous name resolves
Group:          Development/Libraries/C and C++
Requires:       libcares = %{version}
Requires:       glibc-devel

%description -n libcares-devel
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
export CFLAGS=`echo $CFLAGS | sed -e 's/ -l[^ ]\+ / /g'`
autoreconf -fiv
%configure --enable-symbol-hiding --enable-nonblocking --enable-shared --disable-static --with-pic
sed -i -e 's@-g0@-g@g' Makefile
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig -n libcares

%postun -p /sbin/ldconfig -n libcares

%files -n libcares
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libcares.so.2*

%files -n libcares-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*
%{_libdir}/pkgconfig/libcares.pc

%changelog
