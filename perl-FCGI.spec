%include	/usr/lib/rpm/macros.perl
Summary:	FCGI perl module
Summary(pl):	Modu³ perla FCGI
Name:		perl-FCGI
Version:	0.67
Release:	2
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/FCGI-%{version}.tar.gz
Source1:	%{name}-acinclude.m4
URL:		http://www.fastcgi.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a FastCGI module for perl. It's based on the FCGI module
that comes with Open Market's FastCGI Developer's Kit, but does
not require you to recompile perl.

%description -l pl
To jest modu³ FastCGI. Jest bazowany na module FCGI dostarczanym
z FastCGI Developer's Kit, ale nie wymaga rekompilacji perla.

%prep
%setup -q -n FCGI-%{version}
cp -f %{SOURCE1} acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%configure
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* LICENSE.TERMS README echo.fpl
%{perl_vendorarch}/FCGI.pm
%dir %{perl_vendorarch}/auto/FCGI
%{perl_vendorarch}/auto/FCGI/FCGI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/FCGI/FCGI.so
%{_mandir}/man3/*
