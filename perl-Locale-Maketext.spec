%include	/usr/lib/rpm/macros.perl
Summary:	Locale-Maketext perl module
Summary(pl):	Modu³ perla Locale-Maketext
Name:		perl-Locale-Maketext
Version:	0.17
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Locale/Locale-Maketext-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-I18N-LangTags
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-Maketext - framework for software localization.

%description -l pl
Locale-Maketext udostêpnia funkcje pomocne przy lokalizacji programów.

%prep
%setup -q -n Locale-Maketext-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Locale-Maketext
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Locale/Maketext.pm
%{perl_sitearch}/auto/Locale-Maketext

%{_mandir}/man3/*
