#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	MAC
Summary:	Net::MAC - Perl extension for representing and manipulating MAC addresses
Summary(pl):	Net::MAC - rozszerzenie Perla do przedstawiania i obróbki adresów MAC
Name:		perl-Net-MAC
Version:	1.1
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cabec28069bb6f8765f4ee54b561b1b
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

%description -l pl
Modu³ ten pozwala na:

  - przechowywanie adresu MAC w postaci obiektu
  - wyszukiwanie informacji na temat zapisanego adresu MAC
  - konwersjê adresu MAC w okre¶lony format

Istnieje kilka sposobów na przedstawianie adresów MAC w postaci
tekstowej. Prawdopodobnie najpopularniejszy to oddzielony dwukropkami
oktety w postaci szesnastkowej. Pracuj±c z urz±dzeniami Cisco mo¿na
siê jednak natkn±æ na na oddzielone kropkami 16-bitowe grupy w postaci
szesnastkowej. W ¶wiecie Windows, adresy s± zazwyczaj przedstawione w
postaci oddzielonych my¶lnikami oktetów w postaci szesnastkowej.
Adresy MAC w pliku ethers systemu SUN zazwyczaj s± w postaci nie
dope³nianych zerami, oddzielonych dwukropkami oktetów w postaci
szesnastkowej. Wreszcie niekiedy mo¿na spotkaæ ca³kowicie szalony
format oddzielonych kropkami oktetów w postaci dziesiêtnej (niektóre
MIB-y Cisco SNMP korzystaj± z tego). Dlatego potrzebna jest wspólna dla
wszystkich formatów metoda do wy¶wietlania i obróbki adresów MAC w
Perlu.

Istnieje zaskakuj±co du¿a z³o¿ono¶æ w procesie konwersji adresu MAC
pomiêdzy ró¿nymi formatami. Ten modu³ nie próbuje zrozumieæ wszystkich
metod na przedstawienie adresu MAC w ³añcuchu znaków, jednak wiêkszo¶æ
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
