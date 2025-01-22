#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Class-C3
Version  : 0.35
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-0.35.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-0.35.tar.gz
Summary  : 'A pragma to use the C3 method resolution order algorithm'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-C3-license = %{version}-%{release}
Requires: perl-Class-C3-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Class::C3 - A pragma to use the C3 method resolution order algorithm
SYNOPSIS
# NOTE - DO NOT USE Class::C3 directly as a user, use MRO::Compat instead!
package ClassA;
use Class::C3;
sub hello { 'A::hello' }

%package dev
Summary: dev components for the perl-Class-C3 package.
Group: Development
Provides: perl-Class-C3-devel = %{version}-%{release}
Requires: perl-Class-C3 = %{version}-%{release}

%description dev
dev components for the perl-Class-C3 package.


%package license
Summary: license components for the perl-Class-C3 package.
Group: Default

%description license
license components for the perl-Class-C3 package.


%package perl
Summary: perl components for the perl-Class-C3 package.
Group: Default
Requires: perl-Class-C3 = %{version}-%{release}

%description perl
perl components for the perl-Class-C3 package.


%prep
%setup -q -n Class-C3-0.35
cd %{_builddir}/Class-C3-0.35

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-C3
cp %{_builddir}/Class-C3-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-C3/2976cf4612c9dab9cc7fc350c53b3e72db20906f || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::C3.3
/usr/share/man/man3/Class::C3::next.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-C3/2976cf4612c9dab9cc7fc350c53b3e72db20906f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
