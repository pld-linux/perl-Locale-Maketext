%define	pdir	Locale
%define	pnam	Maketext
%include	/usr/lib/rpm/macros.perl
Summary:	Locale-Maketext perl module
Summary(pl):	Modu³ perla Locale-Maketext
Name:		perl-Locale-Maketext
Version:	1.03
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-I18N-LangTags
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-Maketext - framework for software localization.

%description -l pl
Locale-Maketext udostêpnia funkcje pomocne przy lokalizacji programów.

%prep
%setup -q -n Locale-Maketext-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Locale/Maketext.pm
%{_mandir}/man3/*
