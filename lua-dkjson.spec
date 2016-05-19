%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-dkjson
Version:        2.5
Release:        1%{?dist}
Summary:        David Kolf's JSON module for Lua 5.1/5.2

License:        MIT
URL:            http://dkolf.de/src/dkjson-lua.fsl/home
Source0:        dkjson.lua
Source1:        readme.txt

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif
Requires:       lua-lpeg


%description
This is a JSON module written in Lua. It supports UTF-8.

JSON (JavaScript Object Notation) is a format for serializing data based on the
syntax for JavaScript data structures. It is an ideal format for transmitting
data between different applications and commonly used for dynamic web pages. It
can also be used to save Lua data structures, but you should be aware that not
every Lua table can be represented by the JSON standard. For example tables
that contain both string keys and an array part cannot be exactly represented
by JSON. You can solve this by putting your array data in an explicit subtable.

dkjson is written in Lua without any dependencies, but when LPeg is available
dkjson uses it to speed up decoding.


%prep


%build


%install
install -d %{buildroot}%{luapkgdir}/
install -p -m644 %{SOURCE0} %{buildroot}%{luapkgdir}/
install -d %{buildroot}%{_datadir}/doc/%{name}-%{version}/
install -p -m644 %{SOURCE1} %{buildroot}%{_datadir}/doc/%{name}-%{version}/


%files
%doc %{_datadir}/doc/%{name}-%{version}/
%{luapkgdir}/dkjson.lua


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.5-1
- Public release
