%global realname sd_notify
%global upstream systemd
%global upstream_version 1.1
%global debug_package %{nil}
%global output_dir _build/default/lib/sd_notify/ebin



Name:		erlang-%{realname}
Version:	%{upstream_version}
Release:	1%{?dist}
Summary:	Erlang interface to systemd notify subsystem
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
Source1:	erlang-sd_notify-rebar.config
BuildRequires:	erlang-rebar


%description
%{summary}.

%prep
%setup  -c .

%build
rebar3 compile


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 -p %{output_dir}/%{realname}.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 -p %{output_dir}/%{realname}.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin


%files
%doc LICENSE
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin/
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.beam


%changelog
* Tue Jul 7 2020 Gabriele Santomaggio <g.santomaggio@gmail.com> - 1.1
- build for 1.1 - Update build for Erlang 23.0

* Thu Apr 13 2017 Gabriele Santomaggio <g.santomaggio@gmail.com> - 1.0
- build for 1.0

* Wed Dec 14 2016 Gabriele Santomaggio <g.santomaggio@gmail.com> - 0.14
- build for 0.14

* Sat Nov 5 2016 Gabriele Santomaggio <g.santomaggio@gmail.com> - 0.13
- build for 0.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-5
- Rebuild with Erlang 17.3.3

* Thu Oct  2 2014 John Eckersberg <eck@redhat.com> - 0.1-4
- Explicitly link shared library with libsystemd (#1148604)

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-3
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 03 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-1
- initial build


