%bcond_without bootstrap
%global packname  sp
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9_95
Release:          1
Summary:          classes and methods for spatial data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-95.tar.gz
Requires:         R-methods R-graphics 
Requires:         R-utils R-lattice R-grid 
%if %{with bootstrap}
Requires:         R-lattice R-RColorBrewer
%else
Requires:         R-lattice R-RColorBrewer R-rgdal R-rgeos 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-graphics
BuildRequires:    R-utils R-lattice R-grid 
%if %{with bootstrap}
BuildRequires:    R-lattice R-RColorBrewer
%else
BuildRequires:    R-lattice R-RColorBrewer R-rgdal R-rgeos 
%endif

%description
A package that provides classes and methods for spatial data. The classes
document where the spatial location information resides, for 2D or 3D
data. Utility functions are provided, e.g. for plotting data as maps,
spatial selection, as well as methods for retrieving coordinates, for
subsetting, print, summary, etc.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
