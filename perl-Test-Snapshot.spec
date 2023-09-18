#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	Test
%define		pnam	Snapshot
Summary:	Test::Snapshot - test against data stored in automatically-named file
Name:		perl-Test-Snapshot
Version:	0.06
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	19ebfa678a7a4f7f186e438bedb2a95c
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/dist/Test-Snapshot
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-Text-Diff
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Not connected with Test::Snapshots, which is based on a similar
concept but for running executables.

Implements a function to automate the storing and updating of expected
test outputs. This is based on the idea known in frontend development
circles as "snapshot testing", hence the module name.

These snapshots will be stored in files whose names are automatically
generated from:

If that file is not present, it will be treated as though it contains
an undef.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Snapshot.pm
%{_mandir}/man3/Test::Snapshot.3*
