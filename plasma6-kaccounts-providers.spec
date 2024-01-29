%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        Additional service providers for KAccounts framework
Name:           plasma6-kaccounts-providers
Version:	24.01.90
Release:	3
License:        GPLv2+
Group:          System/Base
URL:            https://www.kde.org/
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/kaccounts-providers-%{version}.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:  libaccounts-glib-devel
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Package)

%description
Additional service providers for KAccounts framework.

%files -f kaccounts-providers.lang
%{_sysconfdir}/signon-ui/webkit-options.d/*
%{_qtdir}/plugins/kaccounts/ui/*.so
%{_datadir}/accounts/providers/kde
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud
%{_datadir}/accounts/services/kde/nextcloud-contacts.service
%{_datadir}/accounts/services/kde/nextcloud-storage.service
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud
%{_datadir}/accounts/services/kde/owncloud-storage.service
%{_datadir}/icons/hicolor/*/apps/kaccounts-owncloud.png
%{_datadir}/icons/hicolor/*/apps/kaccounts-nextcloud.svg

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n kaccounts-providers-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kaccounts-providers
