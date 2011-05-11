#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	FCGI
Summary:	FCGI - Fast CGI module
Summary(pl.UTF-8):	FCGI - szybki moduł CGI
Name:		perl-FCGI
Version:	0.71
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/FCGI-%{version}.tar.gz
# Source0-md5:	26bc4ea53ccc9c9c16695e88e46a1cfb
Source1:	%{name}-acinclude.m4
URL:		http://www.fastcgi.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.fpl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{pdir}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* LICENSE.TERMS README
%{perl_vendorarch}/FCGI.pm
%dir %{perl_vendorarch}/auto/FCGI
%{perl_vendorarch}/auto/FCGI/FCGI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/FCGI/FCGI.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.fpl
