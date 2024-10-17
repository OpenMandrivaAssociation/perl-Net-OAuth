%define upstream_name    Net-OAuth
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.28
Release:	3

Summary:	An OAuth protocol response for an Request Token
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-OAuth-0.28.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Digest::HMAC_SHA1)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
OAUTH MESSAGES
    An OAuth message is a set of key-value pairs. The following message
    types are supported:

    Requests

    * * Request Token (Net::OAuth::RequestTokenRequest)

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.270.0-2mdv2011.0
+ Revision: 658865
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 552702
- adding missing buildrequires:
- update to 0.27

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 539194
- import perl-Net-OAuth


* Mon Apr 26 2010 cpan2dist 0.25-1mdv
- initial mdv release, generated with cpan2dist

