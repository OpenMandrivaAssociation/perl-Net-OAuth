%define upstream_name    Net-OAuth
%define upstream_version 0.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    An OAuth protocol response for an Request Token
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Digest::HMAC_SHA1)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(Encode)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
OAUTH MESSAGES
    An OAuth message is a set of key-value pairs. The following message
    types are supported:

    Requests

    * * Request Token (Net::OAuth::RequestTokenRequest)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


