Summary:	Remedial AVI player
Summary(pl):	Remedial - odtwarzacz plików AVI
Name:		remedial
Version:	0.2.11
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://access.zonnet.nl/pbd/remedial/src/%{name}-%{version}.tar.gz
URL:		http://leapster.org/remedial/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	expat-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remedial is a front-end for the avifile libraries.

%description -l pl
Remedial to frontend do bibliotek avifile.

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

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_bindir}/remedial
# FIXME: wrong path
#%{_prefix}%{_sysconfdir}/remedial.xml
%{_mandir}/man1/remedial.1*
