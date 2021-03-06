#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : arp-scan
Version  : 1.9
Release  : 2
URL      : https://github.com/royhills/arp-scan/releases/download/1.9/arp-scan-1.9.tar.gz
Source0  : https://github.com/royhills/arp-scan/releases/download/1.9/arp-scan-1.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: arp-scan-bin = %{version}-%{release}
Requires: arp-scan-data = %{version}-%{release}
Requires: arp-scan-license = %{version}-%{release}
Requires: arp-scan-man = %{version}-%{release}
BuildRequires : libpcap-dev

%description
to the arp-scan wiki at http://www.nta-monitor.com/wiki/ for up-to-date
information about installing and using arp-scan.

%package bin
Summary: bin components for the arp-scan package.
Group: Binaries
Requires: arp-scan-data = %{version}-%{release}
Requires: arp-scan-license = %{version}-%{release}

%description bin
bin components for the arp-scan package.


%package data
Summary: data components for the arp-scan package.
Group: Data

%description data
data components for the arp-scan package.


%package license
Summary: license components for the arp-scan package.
Group: Default

%description license
license components for the arp-scan package.


%package man
Summary: man components for the arp-scan package.
Group: Default

%description man
man components for the arp-scan package.


%prep
%setup -q -n arp-scan-1.9
cd %{_builddir}/arp-scan-1.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604091550
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604091550
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/arp-scan
cp %{_builddir}/arp-scan-1.9/COPYING %{buildroot}/usr/share/package-licenses/arp-scan/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arp-fingerprint
/usr/bin/arp-scan
/usr/bin/get-iab
/usr/bin/get-oui

%files data
%defattr(-,root,root,-)
/usr/share/arp-scan/ieee-iab.txt
/usr/share/arp-scan/ieee-oui.txt
/usr/share/arp-scan/mac-vendor.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/arp-scan/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/arp-fingerprint.1
/usr/share/man/man1/arp-scan.1
/usr/share/man/man1/get-iab.1
/usr/share/man/man1/get-oui.1
/usr/share/man/man5/mac-vendor.5
