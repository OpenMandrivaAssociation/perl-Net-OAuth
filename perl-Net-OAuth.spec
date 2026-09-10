%define upstream_name    Net-OAuth
%define upstream_version 0.33

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	An OAuth protocol response for an Request Token
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/keeth/Net-OAuth
Source0:	https://cpan.metacpan.org/authors/id/R/RR/RRWO/Net-OAuth-0.33.tar.gz

BuildRequires:	make
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

