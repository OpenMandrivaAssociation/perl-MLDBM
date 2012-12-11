%define upstream_name    MLDBM
%define upstream_version 2.04

# why not?
#define _requires_exceptions FreezeThaw

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	MLDBM - store multi-level hash structure in single level tied hash
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/C/CH/CHAMAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/MLDBM*
%{_mandir}/*/*


%changelog
* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.1
+ Revision: 515752
- update to 2.04

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 512614
- update to 2.03

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 510092
- update to 2.02

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 407801
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.01-10mdv2009.0
+ Revision: 257846
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.01-9mdv2009.0
+ Revision: 245879
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.01-7mdv2008.1
+ Revision: 136288
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 2.01-7mdv2007.0
+ Revision: 108473
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-MLDBM

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 2.01-6mdk
- fixup

