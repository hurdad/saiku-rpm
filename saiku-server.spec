Name:		saiku-server
Version:	2.5
Release:	1%{?dist}
Summary:	Modular open-source analysis suite
Group:		System Environment/Daemons 
License:	Apache License 2.0
URL:		http://www.meteorite.bi/saiku
Source0:	http://meteorite.bi/downloads/%{name}-%{version}.tar.gz
Source1:	saiku-server
BuildArch:	noarch
Packager:	Alexander Hurd <hurdad@gmail.com>

%description
Modular open-source analysis suite offering lightweight OLAP which remains easily embeddable, extendable and configurable.

%prep
%setup -q -n saiku-server

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/saiku-server
%{__install} -d %{buildroot}%{_initddir}/
%{__cp} -av * %{buildroot}%{_datadir}/saiku-server
%{__cp} -p %{SOURCE1} %{buildroot}%{_initddir}

%pre
if ! /usr/bin/id saiku-server &>/dev/null; then
    /usr/sbin/useradd -r -s /bin/sh -c "saiku-server" saiku-server || \
        %logmsg "Unexpected error adding user \"saiku-server\". Aborting installation."
fi

%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel saiku-server || %logmsg "User \"saiku-server\" could not be deleted."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%doc README LICENSE
%defattr(-,saiku-server,saiku-server,-)
%{_datadir}
%{_sysconfdir}

%changelog

