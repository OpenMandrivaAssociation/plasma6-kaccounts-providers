%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        Additional service providers for KAccounts framework
Name:           kaccounts-providers
Version:	22.08.0
Release:	1
License:        GPLv2+
Group:          System/Base
URL:            https://www.kde.org/
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:  libaccounts-glib-devel
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Package)

%description
Additional service providers for KAccounts framework.

%files -f %{name}.lang
%{_sysconfdir}/signon-ui/webkit-options.d/*
%{_qt5_plugindir}/kaccounts/ui/*.so
%{_datadir}/accounts/providers/kde
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud
%{_datadir}/metainfo/org.kde.kaccounts.owncloud.appdata.xml
%{_datadir}/accounts/services/kde/nextcloud-contacts.service
%{_datadir}/accounts/services/kde/nextcloud-storage.service
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud
%{_datadir}/metainfo/org.kde.kaccounts.nextcloud.appdata.xml
%{_datadir}/accounts/services/kde/owncloud-storage.service
%{_datadir}/icons/hicolor/*/apps/kaccounts-owncloud.png
%{_datadir}/icons/hicolor/*/apps/kaccounts-nextcloud.svg

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
