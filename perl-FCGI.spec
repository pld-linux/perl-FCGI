%include	/usr/lib/rpm/macros.perl
Summary:	FCGI perl module
Summary(pl):	Modu� perla FCGI
Name:		perl-FCGI
Version:	0.58
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/FCGI/FCGI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI - Fast CGI module.

%description -l pl
FCGI - szybki modu� CGI.

%prep
%setup -q -n FCGI-%{version}

%build
aclocal
autoconf
%configure
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz echo.fpl
%{perl_sitearch}/FCGI.pm
%dir %{perl_sitearch}/auto/FCGI
%{perl_sitearch}/auto/FCGI/FCGI.bs
%attr(755,root,root) %{perl_sitearch}/auto/FCGI/FCGI.so
%{_mandir}/man3/*
