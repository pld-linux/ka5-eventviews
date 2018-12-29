%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		eventviews
Summary:	Library for creating events
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d9840f1af87ca727367d51e1be9b0a2b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= 18.12.0
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-calendarsupport-devel >= 18.12.0
BuildRequires:	ka5-kcalcore-devel >= 18.12.0
BuildRequires:	ka5-kcalutils-devel >= 18.12.0
BuildRequires:	ka5-kmime-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	kdiagram-devel >= 1.4.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kguiaddons-devel >= 5.51.0
BuildRequires:	kf5-kholidays-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kservice-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It contains lib for creating events.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/eventviews.categories
/etc/xdg/eventviews.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5EventViews.so.5
%attr(755,root,root) %{_libdir}/libKF5EventViews.so.5.*.*
%{_datadir}/kservicetypes5/calendardecoration.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/EventViews
%{_includedir}/KF5/eventviews
%{_includedir}/KF5/eventviews_version.h
%{_libdir}/cmake/KF5EventViews
%attr(755,root,root) %{_libdir}/libKF5EventViews.so
%{_libdir}/qt5/mkspecs/modules/qt_EventViews.pri
