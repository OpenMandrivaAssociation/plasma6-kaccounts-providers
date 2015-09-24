#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#

%define rel 1

Summary:        Additional service providers for KAccounts framework
Name:           kaccounts-providers
Version: 15.08.1
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

BuildArch:      noarch

URL:            https://www.kde.org/

BuildRequires:  kf5-macros
BuildRequires:  pkgconfig(Qt5Widgets)

BuildRequires:  libaccounts-glib-devel
BuildRequires:  intltool
BuildRequires:  kaccounts-integration-devel
 
%description
Additional service providers for KAccounts framework

%files 
%_sysconfdir/signon-ui/webkit-options.d/*
%_kf5_datadir/accounts/providers/google.provider

#--------------------------------------------------------------------

%prep
%setup -q 
%autopatch -p1

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build



%changelog
* Fri Sep 18 2015 neoclust <neoclust> 15.08.1-1.mga6
+ Revision: 880395
- New version 15.08.1

* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865913
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863688
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 862048
- New version 15.07.90

* Fri Jul 31 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 859728
- New version 15.07.80

* Wed Jul 22 2015 neoclust <neoclust> 15.04.3-1.mga6
+ Revision: 856187
- imported package kaccounts-providers

