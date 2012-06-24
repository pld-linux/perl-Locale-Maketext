%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Maketext
Summary:	Locale-Maketext perl module
Summary(pl):	Modu� perla Locale-Maketext
Name:		perl-Locale-Maketext
Version:	1.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-I18N-LangTags
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-Maketext - framework for software localization.

%description -l pl
Locale-Maketext udost�pnia funkcje pomocne przy lokalizacji program�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
