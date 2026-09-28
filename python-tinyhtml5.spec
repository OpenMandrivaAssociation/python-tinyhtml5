Name:		python-tinyhtml5
Version:	2.1.0
Release:	1
Summary:	HTML parser based on the WHATWG HTML specification
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tinyhtml5/
Source0:	tinyhtml5-2.1.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(webencodings)
BuildArch:	noarch
%description
HTML parser based on the WHATWG HTML specification.

%files
%{py_sitedir}/*
