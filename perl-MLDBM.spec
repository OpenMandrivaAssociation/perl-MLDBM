%define _requires_exceptions FreezeThaw

%define real_name MLDBM

Summary:	MLDBM - store multi-level hash structure in single level tied hash
Name:		perl-%{real_name}
Version:	2.01
Release:	%mkrel 7
License:	GPL or Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{real_name}
Source0:	http://www.cpan.org/authors/id/C/CH/CHAMAS/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module can serve as a transparent interface to any TIEHASH package
that is required to store arbitrary perl data, including nested references.
Thus, this module can be used for storing references and other arbitrary data
within DBM databases.

It works by serializing the references in the hash into a single string. In the
underlying TIEHASH package (usually a DBM database), it is this string that
gets stored.  When the value is fetched again, the string is deserialized to
reconstruct the data structure into memory.

For historical and practical reasons, it requires the Data::Dumper package,
available at any CPAN site. Data::Dumper gives you really nice-looking dumps of
your data structures, in case you wish to look at them on the screen, and
it was the only serializing engine before version 2.00.  However, as of version
2.00, you can use any of Data::Dumper, FreezeThaw or Storable to
perform the underlying serialization, as hinted at by the SYNOPSIS overview
above.  Using Storable is usually much faster than the other methods.

See the BUGS section for important limitations.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/MLDBM*
%{_mandir}/*/*


