#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        Additional service providers for KAccounts framework
Name:           plasma6-kaccounts-providers
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
License:        GPLv2+
Group:          System/Base
URL:            https://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kaccounts-providers/-/archive/%{gitbranch}/kaccounts-providers-%{gitbranchd}.tar.bz2#/kaccounts-providers-%{git}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/kaccounts-providers-%{version}.tar.xz
%endif
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6QmlNetworkplugin)
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
%autosetup -p1 -n kaccounts-providers-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kaccounts-providers
