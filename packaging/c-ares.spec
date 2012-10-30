Url:            http://daniel.haxx.se/projects/c-ares
%define pkg_name c-ares

Name:           c-ares
Version:        1.7.5
Release:        1
License:        MIT
Summary:        Library for asynchronous name resolves
Group:          Development/Libraries/C and C++
Source:         http://daniel.haxx.se/projects/c-ares/%{pkg_name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  pkg-config
BuildRequires:  libtool

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
%setup -q -n %{pkg_name}-%{version}

%build
autoreconf -fiv
%configure --enable-symbol-hiding --enable-nonblocking --enable-shared --disable-static --with-pic
sed -i -e 's@-g0@-g@g' Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libcares
%defattr(-,root,root)
%{_libdir}/libcares.so.2*

%files -n libcares-devel
%defattr(-,root,root)
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*
%{_libdir}/pkgconfig/libcares.pc

%changelog
