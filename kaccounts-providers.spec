%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:        Additional service providers for KAccounts framework
Name:           kaccounts-providers
Version:        16.08.2
Release:        1
License:        GPLv2+
Group:          System/Base
URL:            https://www.kde.org/
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  libaccounts-glib-devel
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Package)

%description
Additional service providers for KAccounts framework

%files
%{_sysconfdir}/signon-ui/webkit-options.d/*
%{_qt5_plugindir}/kaccounts/ui/*.so
%{_datadir}/accounts/providers/kde
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud

#--------------------------------------------------------------------

%prep
%setup -q 
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
