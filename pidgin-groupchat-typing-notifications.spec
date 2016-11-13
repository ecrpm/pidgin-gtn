Name: pidgin-groupchat-typing-notifications
Version: 2
Release: 1%{?dist}
Summary: Adds typing notifications for group chats in Pidgin

License: GPLv3+
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)
BuildRequires: gcc

Requires: pidgin%{?_isa}

%description
Adds typing notifications for multi-user group chats in Pidgin.
Currently only tested as working with the Hangouts plugin, but
support for other protocols will come later.

%prep
%autosetup

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
# Executing base install from makefile...
%make_install

# Setting correct chmod...
chmod 755 %{buildroot}%{_libdir}/pidgin/grouptyping.so

%files
%{_libdir}/pidgin/grouptyping.so
%license LICENSE
%doc README.md

%changelog
* Sun Nov 13 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2-1
- Updated to version 2. Use normal releases instead of Git snapshots.

* Mon Nov 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.git33a75f9
- Small SPEC fixes.

* Sun Nov 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.git33a75f9
- Initial commit.
