#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Maketext
Summary:	Locale::Maketext - framework for localization
Summary(pl):	Locale::Maketext - szkielet do lokalizacji programów
Name:		perl-Locale-Maketext
Version:	1.03
Release:	7
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
%if %{?_without_test:0}%{!?_without_test:1}
BuildRequires:	perl-I18N-LangTags
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a common feature of applications (whether run directly, or via the
Web) for them to be "localized" -- i.e., for them to a present an English
interface to an English- speaker, a German interface to a German-speaker,
and so on for all languages it's programmed with.

Locale::Maketext is a framework for software localization; it provides
you with the tools for organizing and accessing the bits of text and
text-processing code that you need for producing localized applications.

%description -l pl
Czêsto spotykan± cech± programów (uruchamianych bezpo¶rednio lub przez WWW)
jest ich lokalizacja, czyli umiejêtno¶æ prezentowania angielskiego interfejsu
u¿ytkownikowi anglojêzycznemu, niemiekiego -- niemieckojêzycznemu i tak dalej
dla wszystkich jêzyków, dla których istniej± t³umaczenia.

Locale::Maketext jest szkieletem do tworzenia zlokalizowanych programów;
udostêpnia Ci narzêdzia do organizowania i odwo³ywania siê do fragmentów
tekstu, oraz potrzebnego Ci przy tworzeniu zlokalizowanego oprogramowania
kodu przetwarzaj±cego tekst.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_vendorlib}/Locale/Maketext
%{perl_vendorlib}/Locale/Maketext.pm
%{_mandir}/man3/*
