%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name marathon

Name:           python-%{pypi_name}
Version:        0.8.6
Release:        1%{?dist}
Summary:        Python client library/interface to the Mesos Marathon REST API

License:        MIT
URL:            https://github.com/thefactory/marathon-python
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/thefactory/marathon-python/master/LICENSE
Source2:        https://raw.githubusercontent.com/thefactory/marathon-python/master/README.md
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

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}

BuildRequires: python-sphinx
BuildRequires: python-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Python client library/interface to the Mesos Marathon REST API

This package contains the documentation.

%package -n python2-%{pypi_name}-tests
Summary:    Tests for python-%{pypi_name}
Requires:   python2-%{pypi_name} = %{version}-%{release}

%description -n python2-%{pypi_name}-tests
Python client library/interface to the Mesos Marathon REST API

This package contains the test files.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary: Python interface to the Mesos Marathon REST API
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-requests

%description -n python3-%{pypi_name}
Python client library/interface to the Mesos Marathon REST API

%package -n python3-%{pypi_name}-tests
Summary:    Tests for python-%{pypi_name}
Requires:   python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
Python client library/interface to the Mesos Marathon REST API

This package contains the test files.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} LICENSE
cp %{SOURCE2} README

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# Generate HTML docs
sphinx-build docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{pypi_name}
%doc html README
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html README

%files -n python2-%{pypi_name}-tests
%license LICENSE
%{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc html README
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests
%endif

%changelog
* Fri Oct 14 2016 David Moreau Simard <dmsimard@redhat.com> - 0.8.6-1
- First version
