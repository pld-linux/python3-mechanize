%define		module	mechanize
Summary:	Library for automating interaction with web pages
Summary(pl.UTF-8):	Biblioteka do automatycznej interakcji ze stronami WWW
Name:		python3-%{module}
Version:	0.4.8
Release:	2
License:	BSD, ZPL 2.1
Group:		Development/Languages/Python
Source0:	https://github.com/python-mechanize/mechanize/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	0be3c261b6f44fee05fe2e5febbe8f76
URL:		https://github.com/python-mechanize/mechanize/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for automating interaction with web pages.

%description -l pl.UTF-8
Biblioteka do automatycznej interakcji ze stronami WWW.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE ChangeLog README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/mechanize-*.egg-info
