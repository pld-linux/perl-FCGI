%include	/usr/lib/rpm/macros.perl
Summary:	FCGI perl module
Summary(pl):	Modu³ perla FCGI
Name:		perl-FCGI
Version:	0.45
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//FCGI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI - Fast CGI module.

%description -l pl
FCGI - szybki modu³ CGI.

%prep
%setup -q -n FCGI-%{version}

%build
%configure
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/FCGI/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/FCGI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz echo.fpl

%{perl_sitearch}/FCGI.pm

%dir %{perl_sitearch}/auto/FCGI
%{perl_sitearch}/auto/FCGI/.packlist
%{perl_sitearch}/auto/FCGI/FCGI.bs
%attr(755,root,root) %{perl_sitearch}/auto/FCGI/FCGI.so

%{_mandir}/man3/*
