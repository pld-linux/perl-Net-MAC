#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	MAC
Summary:	Net::MAC - Perl extension for representing and manipulating MAC addresses
Summary(pl.UTF-8):	Net::MAC - rozszerzenie Perla do przedstawiania i obróbki adresów MAC
Name:		perl-Net-MAC
Version:	1.5
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed7fbdd88aa7f9ef566cf3e029fb0ad3
URL:		http://search.cpan.org/dist/Net-MAC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module that allows you to

  - store a MAC address in a Perl object
  - find out information about a stored MAC address
  - convert a MAC address into a specified format

There are quite a few different ways that MAC addresses may be
represented in textual form. The most common is arguably
colon-delimited octets in hexadecimal form. When working with Cisco
devices, however, you are more likely to encounter addresses that are
dot-delimited 16-bit groups in hexadecimal form. In the Windows world,
addresses are usually dash-delimited octets in hexadecimal form. MAC
addresses in a Sun ethers file are usually non-zero-padded,
colon-delimited hexadecimal octets. And sometimes, you come across the
totally insane dot-delimited octets in decimal form (certain Cisco
SNMP MIBS actually use this). Hence the need for a common way to
represent and manipulate MAC addresses in Perl.

There is a surprising amount of complexity involved in converting MAC
addresses between types. This module does not attempt to understand
all possible ways of representing a MAC address in a string, though
most of the common ways of representing MAC addresses are supported.

%description -l pl.UTF-8
Moduł ten pozwala na:

  - przechowywanie adresu MAC w postaci obiektu
  - wyszukiwanie informacji na temat zapisanego adresu MAC
  - konwersję adresu MAC w określony format

Istnieje kilka sposobów na przedstawianie adresów MAC w postaci
tekstowej. Prawdopodobnie najpopularniejszy to oddzielony dwukropkami
oktety w postaci szesnastkowej. Pracując z urządzeniami Cisco można
się jednak natknąć na na oddzielone kropkami 16-bitowe grupy w postaci
szesnastkowej. W świecie Windows, adresy są zazwyczaj przedstawione w
postaci oddzielonych myślnikami oktetów w postaci szesnastkowej.
Adresy MAC w pliku ethers systemu SUN zazwyczaj są w postaci nie
dopełnianych zerami, oddzielonych dwukropkami oktetów w postaci
szesnastkowej. Wreszcie niekiedy można spotkać całkowicie szalony
format oddzielonych kropkami oktetów w postaci dziesiętnej (niektóre
MIB-y Cisco SNMP korzystają z tego). Dlatego potrzebna jest wspólna dla
wszystkich formatów metoda do wyświetlania i obróbki adresów MAC w
Perlu.

Istnieje zaskakująco duża złożoność w procesie konwersji adresu MAC
pomiędzy różnymi formatami. Ten moduł nie próbuje zrozumieć wszystkich
metod na przedstawienie adresu MAC w łańcuchu znaków, jednak większość
z popularnych metod przedstawiania adresów jest wspierana.

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
%doc README
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
