#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Locale
%define		pnam	Maketext
Summary:	Locale::Maketext - framework for localization
Summary(pl.UTF-8):	Locale::Maketext - szkielet do lokalizacji programów
Name:		perl-Locale-Maketext
Version:	1.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd3428820f4155213a4de59e90564405
URL:		http://search.cpan.org/dist/Locale-Maketext/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 2.1-15
%if %{with tests}
BuildRequires:	perl-I18N-LangTags >= 0.31
%endif
Requires:	perl-I18N-LangTags >= 0.31
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
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Locale/Maketext.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Locale/Maketext/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Locale/Maketext.pm
%{perl_vendorlib}/Locale/Maketext
%{_mandir}/man3/Locale::Maketext*.3pm*
