Summary:	Tool to optimize relocations in object files.
Summary(pl):	Narzêdzie optymalizuj±ce relokacje w plikach objektów.
Name:		objprelink
Version:	1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.research.att.com/~leonb/objprelink/objprelink.c.gz
URL:		http://www.research.att.com/~leonb/objprelink/
BuildRequires:	binutils
BuildRequires:	binutils-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program replaces relocations in object files with less expensive
ones. This allows faster run-time dynamic linking.

%description -l pl
Ten program zamienia relokacje w plikach objektów na mniej wymagaj±ce.
Dziêki temu program jest szybciej linkowany w momencie uruchomienia.

%prep
cd %{_builddir}
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
cp %{SOURCE0} .
gzip -d *.gz

%build
cd %{name}-%{version}
#gcc -O2 -o objprelink objprelink.c /usr/lib/libbfd.a /usr/lib/libiberty.a
gcc $RPM_OPT_FLAGS -o objprelink objprelink.c -lbfd /usr/lib/libiberty.a

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}-%{version}/objprelink $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
