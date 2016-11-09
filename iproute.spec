%{!?dbq_version: %define cbq_version v0.7.3}
%{!?version:  %define version 4.1.35}
%{!?up_version:  %define up_version 4.1.0}
%{!?build_number:  %define build_number 1}

Summary: Advanced IP routing and network device configuration tools
Name: iproute
Version: %{version}
Release: %{build_number}%{?dist}
Group: Applications/System
Source: https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{up_version}.tar.xz
URL:    http://linux-net.osdl.org/index.php/Iproute2

License: GPLv2+ and Public Domain
BuildRequires: tex(latex) tex(dvips) linuxdoc-tools
BuildRequires: flex psutils db4-devel bison libmnl-devel
# introduction new iptables (xtables) which broke ipt
BuildRequires: iptables >= 1.4.5
BuildRequires: iptables-devel >= 1.4.5
Requires:      iptables >= 1.4.5

%description
The iproute package contains networking utilities (ip and rtmon, for
example) which are designed to use the advanced networking
capabilities of the Linux 2.4.x and 2.6.x kernel.

%package devel
Summary: iproute development files
Group: Development/Libraries
License: GPLv2+
Provides: iproute-static = %{version}-%{release}

%description devel
The libnetlink static library.

%package doc
Summary: ip and tc documentation with examples
Group:  Applications/System
License: GPLv2+

%description doc
The iproute documentation contains howtos and examples of settings.

%prep
%setup -q -n iproute2-%{up_version}

%build
export LIBDIR=/%{_libdir}
export IPT_LIB_DIR=/%{_lib}/xtables
./configure
make %{?_smp_mflags}
make -C doc

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/sbin \
     $RPM_BUILD_ROOT%{_sbindir} \
     $RPM_BUILD_ROOT%{_includedir} \
     $RPM_BUILD_ROOT%{_mandir}/man3 \
     $RPM_BUILD_ROOT%{_mandir}/man8 \
     $RPM_BUILD_ROOT/%{_sysconfdir}/iproute2 \
     $RPM_BUILD_ROOT%{_datadir}/tc \
     $RPM_BUILD_ROOT%{_libdir}/tc

install -m 755 ip/ip ip/ifcfg ip/rtmon tc/tc bridge/bridge $RPM_BUILD_ROOT/sbin
install -m 755 misc/ss misc/nstat misc/rtacct misc/lnstat misc/arpd $RPM_BUILD_ROOT%{_sbindir}
install -m 644 netem/normal.dist netem/pareto.dist netem/paretonormal.dist $RPM_BUILD_ROOT%{_datadir}/tc
install -m 644 man/man8/*.8 $RPM_BUILD_ROOT/%{_mandir}/man8
rm -r $RPM_BUILD_ROOT/%{_mandir}/man8/ss.8
iconv -f latin1 -t utf8 < man/man8/ss.8 > $RPM_BUILD_ROOT/%{_mandir}/man8/ss.8
install -m 644 man/man3/*.3 $RPM_BUILD_ROOT/%{_mandir}/man3
install -m 755 examples/cbq.init-%{cbq_version} $RPM_BUILD_ROOT/sbin/cbq
install -d -m 755 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq

# libnetlink
install -m644 include/libnetlink.h %{buildroot}%{_includedir}
install -m644 lib/libnetlink.a %{buildroot}%{_libdir}

cp -f etc/iproute2/* $RPM_BUILD_ROOT/%{_sysconfdir}/iproute2
rm -rf $RPM_BUILD_ROOT/%{_libdir}/debug/*

#create example avpkt file
cat <<EOF > $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq/cbq-0000.example
DEVICE=eth0,10Mbit,1Mbit
RATE=128Kbit
WEIGHT=10Kbit
PRIO=5
RULE=192.168.1.0/24
EOF

cat <<EOF > $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq/avpkt
AVPKT=3000
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/iproute2
%doc README README.decnet README.iproute2+tc README.distribution README.lnstat COPYING
/sbin/*
%{_mandir}/man8/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%dir %{_datadir}/tc
%{_datadir}/tc/*
%dir %{_sysconfdir}/sysconfig/cbq
%config(noreplace) %{_sysconfdir}/sysconfig/cbq/*

%files devel
%doc COPYING
%{_mandir}/man3/*
%{_libdir}/libnetlink.a
%{_includedir}/libnetlink.h

%files doc
%defattr(-,root,root,-)
%doc doc/*.ps
%doc examples

%changelog
