#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Maketext
Summary:	Locale::Maketext - framework for localization
Summary(pl.UTF-8):	Locale::Maketext - szkielet do lokalizacji programów
Name:		perl-Locale-Maketext
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ce7df98688f33c15c8b15fb25190dd7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-I18N-LangTags >= 0.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a common feature of applications (whether run directly, or via
the Web) for them to be "localized" - i.e., for them to a present an
English interface to an English-speaker, a German interface to a
German-speaker, and so on for all languages it's programmed with.

Locale::Maketext is a framework for software localization; it provides
you with the tools for organizing and accessing the bits of text and
text-processing code that you need for producing localized
applications.

%description -l pl.UTF-8
Często spotykaną cechą programów (uruchamianych bezpośrednio lub przez
WWW) jest ich lokalizacja, czyli umiejętność prezentowania
angielskiego interfejsu użytkownikowi anglojęzycznemu, niemieckiego -
niemieckojęzycznemu i tak dalej dla wszystkich języków, dla których
istnieją tłumaczenia.

Locale::Maketext jest szkieletem do tworzenia zlokalizowanych
programów; udostępnia Ci narzędzia do organizowania i odwoływania się
do fragmentów tekstu, oraz potrzebnego Ci przy tworzeniu
zlokalizowanego oprogramowania kodu przetwarzającego tekst.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/Guts*
%{_mandir}/man3/*
