#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	pdir	FCGI
Summary:	FCGI - Fast CGI module
Summary(pl.UTF-8):	FCGI - szybki moduł CGI
Name:		perl-FCGI
Version:	0.82
Release:	4
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/FCGI-%{version}.tar.gz
# Source0-md5:	f51a6cb522c0ff25043281532ad0479f
Source1:	%{name}-acinclude.m4
Patch0:		am.patch
URL:		https://metacpan.org/dist/FCGI
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-FCGI-Client >= 0.09
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a FastCGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

%description -l pl.UTF-8
To jest moduł FastCGI. Jest bazowany na module FCGI dostarczanym z
FastCGI Developer's Kit, ale nie wymaga rekompilacji Perla.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
cp -f %{SOURCE1} acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%configure
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/FCGI.pm
%dir %{perl_vendorarch}/auto/FCGI
%attr(755,root,root) %{perl_vendorarch}/auto/FCGI/FCGI.so
%{_mandir}/man3/FCGI.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
