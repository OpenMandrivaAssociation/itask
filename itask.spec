%define	name itask
%define	version 0.0.0.2
%define release %mkrel 2
%define svn 20091011

%define epoch 1
%define libname %mklibname %{name} %epoch
%define libnamedev %mklibname %{name} %epoch -d

Summary: 	Application launcher and taskbar based on the good old engage
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Toys
URL:		http://code.google.com/p/itask-module/
Source: 	%{name}-ng-%{svn}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.050
BuildRequires:  evas-devel >= 0.9.9.050, esmart-devel >= 0.9.0.008
BuildRequires:  edje-devel >= 0.9.9.050
Buildrequires:  efreet-devel >= 0.5.0.50
BuildRequires:  eet-devel >= 1.1.0, e-devel >= 0.16.999.050
BuildRequires:  edje >= 0.9.9.050, etk-devel >= 0.1.0.042
Buildrequires:	gettext-devel %{mklibname cares}-devel
requires:       e >= 0.16.999.050

%description
this is an application launcher and taskbar based on the good old 
engage. the module requires that you have a composite manager 
like kompmgr, xcompmgr or bling running. please have a look at the
README for setting things up. Check out Itask in action. I recommend
using the detour theme, since it makes e's internal border icons
zoom correctly.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}-ng-%{svn}

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}
for mo in `ls %buildroot%_datadir/locale/` ;
do Y=`echo -n $mo | sed -e "s|/||"`;
echo "%lang($Y) $(echo %_datadir/locale/${mo}/LC_MESSAGES/ng.mo)" >> %{_builddir}/%{name}-%{version}/%{name}.lang
done

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO INSTALL
#%_datadir/locale/*
%{_libdir}/enlightenment/modules/itask-ng/*
