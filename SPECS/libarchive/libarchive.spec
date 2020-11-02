Summary:    Multi-format archive and compression library
Name:       libarchive
Version:    3.3.1
Release:    7%{?dist}
License:    BSD 2-Clause License
URL:        http://www.libarchive.org/
Group:      System Environment/Development
Vendor:     VMware, Inc.
Distribution:   Photon
Source0:    http://www.libarchive.org/downloads/%{name}-%{version}.tar.gz
%define sha1 libarchive=d5616f81804aba92547629c08a3ccff86c2844ae
Patch0:     libarchive-CVE-2018-1000877.patch
Patch1:     libarchive-CVE-2018-1000878.patch
Patch2:     libarchive-CVE-2018-1000879.patch
Patch3:     libarchive-CVE-2018-1000880.patch
Patch4:     libarchive-CVE-2019-1000019.patch
Patch5:     libarchive-CVE-2019-1000020.patch
Patch6:     libarchive-CVE-2019-18408.patch
Patch7:     libarchive-CVE-2019-19221.patch
Patch8:     libarchive-CVE-2020-21674.patch
BuildRequires:  xz-libs
BuildRequires:  xz-devel
Requires:       xz-libs
%description
Multi-format archive and compression library

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}-%{release}
%description	devel
It contains the libraries and header files to create applications 

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export CFLAGS="%{optflags}"
./configure  --prefix=%{_prefix} --disable-static

make %{?_smp_mflags}

%install
rm -rf %{buildroot}%{_infodir}
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_bindir}
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}
%{_mandir}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*   Mon Nov 02 2020 Ankit Jain <ankitja@vmware.com> 3.3.1-7
-   Fix for CVE-2020-21674
*   Wed Feb 05 2020 Ankit Jain <ankitja@vmware.com> 3.3.1-6
-   Fix for CVE-2019-19221
*   Fri Nov 08 2019 Ankit Jain <ankitja@vmware.com> 3.3.1-5
-   Fix for CVE-2019-18408
*   Tue May 21 2019 Ankit Jain <ankitja@vmware.com> 3.3.1-4
-   Fix for CVE-2018-1000879,CVE-2018-1000880,CVE-2019-1000019
-   CVE-2019-1000020
*   Mon Mar 04 2019 Ankit Jain <ankitja@vmware.com> 3.3.1-3
-   Fix for CVE-2018-1000877 and CVE-2018-1000878
*   Fri Sep 15 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.3.1-2
-   Add xz-libs and xz-devel to BuildRequires and Requires
*   Mon Apr 03 2017 Divya Thaluru <dthaluru@vmware.com> 3.3.1-1
-   Upgrade version to 3.3.1
*   Tue Sep 27 2016 Alexey Makhalov <amakhalov@vmware.com> 3.2.1-1
-   Update version to 3.2.1
*   Thu Sep 22 2016 Anish Swaminathan <anishs@vmware.com> 3.1.2-7
-   Adding patch for security fix CVE-2016-6250
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.1.2-6
-   GA - Bump release of all rpms
*   Mon Oct 12 2015 Xiaolin Li <xiaolinl@vmware.com> 3.1.2-5
-   Moving static lib files to devel package.
*   Fri Oct 9 2015 Xiaolin Li <xiaolinl@vmware.com> 3.1.2-4
-   Removing la files from packages.
*   Fri Aug 14 2015 Alexey Makhalov <amakhalov@vmware.com> 3.1.2-3
-   Adding patches for security fixes CVE-2013-2011 and CVE-2015-2304.
*   Wed Jul 8 2015 Alexey Makhalov <amakhalov@vmware.com> 3.1.2-2
-   Added devel package, dist tag. Use macroses part.
*   Fri Jun 5 2015 Touseef Liaqat <tliaqat@vmware.com> 3.1.2-1
-   Initial build.  First version
