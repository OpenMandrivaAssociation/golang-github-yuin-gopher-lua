# Run tests in check section
%bcond_without check

%global goipath         github.com/yuin/gopher-lua
%global commit          ca850f594eaafa5468da2bd53b865e4ee55be18b

%global common_description %{expand:
GopherLua: VM and compiler for Lua in Go.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.6%{?dist}
Summary: GopherLua: VM and compiler for Lua in Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.rst


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitca850f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180628gitca850f5
- Bump to commit ca850f594eaafa5468da2bd53b865e4ee55be18b

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git7d7bc87
- Update with the new Go packaging
- Upstream GIT revision 7d7bc87

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20171031git609c9cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20171031git609c9cd
- Upstream GIT revision 609c9cd

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170915giteb1c729
- First package for Fedora

