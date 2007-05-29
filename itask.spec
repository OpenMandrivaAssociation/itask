%define	name itask
%define	version 0.0.0.1
%define release %mkrel 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	This is an application launcher and taskbar based on the good old engage.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Toys
URL:		http://code.google.com/p/itask-module/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.038
BuildRequires:  evas-devel >= 0.9.9.038, esmart-devel >= 0.9.0.008
BuildRequires:  edje-devel >= 0.5.0.038
BuildRequires:  eet-devel >= 0.9.10.038, %{mklibname e0}-devel >= 0.16.999.038
BuildRequires:  edje >= 0.5.0.038, etk-devel >= 0.1.0.003
requires:       e >= 0.16.999.038


%description
this is an application launcher and taskbar based on the good old 
engage. the module requires that you have a composite manager 
like kompmgr, xcompmgr or bling running. please have a look at the
README for setting things up. Check out Itask in action. I recommend
using the detour theme, since it makes e's internal border icons
zoom correctly.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO INSTALL
/*
