%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name marathon

Name:           python-%{pypi_name}
Version:        0.8.7
Release:        1%{?dist}
Summary:        Python client library/interface to the Mesos Marathon REST API

# Note: The license is not bundled in the source release tarballs
# https://github.com/thefactory/marathon-python/issues/156
License:        MIT
URL:            https://github.com/thefactory/marathon-python
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/thefactory/marathon-python/%{version}/README.md
BuildArch:      noarch

%description
Marathon Client Library

Python interface to the Mesos Marathon REST API

%package -n python2-%{pypi_name}
Summary: Python client library/interface to the Mesos Marathon REST API
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-requests

%description -n python2-%{pypi_name}
Python client library/interface to the Mesos Marathon REST API

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary: Python interface to the Mesos Marathon REST API
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-requests

%description -n python3-%{pypi_name}
Python client library/interface to the Mesos Marathon REST API
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} README

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{pypi_name}
%doc README
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
%endif

%changelog
* Fri Oct 14 2016 David Moreau Simard <dmsimard@redhat.com> - 0.8.6-1
- First version
