Summary:	Remedial AVI player
Name:		remedial
Version:	0.2.11
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://access.zonnet.nl/pbd/remedial/src/%{name}-%{version}.tar.gz
URL:		http://leapster.org/remedial/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	avifile-devel
BuildRequires:	expat-devel
BuildRequires:	qt-devel

%description
Remedial is a front-end for the avifile libraries.

%prep
%setup -q

%build
#CFLAGS="%{rpmcflags}"; export CFLAGS
%{__aclocal}
%{__autoconf}
%{__automake}
./am_edit --no-final
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

i%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_bindir}/remedial
%{_prefix}%{_sysconfdir}/remedial.xml
%{_mandir}/man1/remedial.1*
