Summary:	Remedial AVI player
Summary(pl):	Remedial - odtwarzacz plików AVI
Name:		remedial
Version:	0.2.15
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://access.zonnet.nl/pbd/remedial/src/%{name}-%{version}.tar.gz
# Source0-md5:	a6ad1d201855e8d3c0edd0fd1104c876
URL:		http://leapster.org/remedial/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	expat-devel
BuildRequires:	libao-devel
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
%{__make} install DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/remedial
%{_libdir}/%{name}/*
%{_sysconfdir}/remedial.xml
%{_mandir}/man1/remedial.1*
