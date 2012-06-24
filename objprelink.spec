Summary:	Tool to optimize relocations in object files
Summary(pl):	Narz�dzie optymalizuj�ce relokacje w plikach objekt�w
Name:		objprelink
Version:	1
Release:	5
License:	GPL
Group:		Development/Tools
Source0:	http://leon.bottou.com/objprelink/%{name}.c.gz
# Source0-md5:	53c4c235ec3da92e4a9fb50ffa54beeb
URL:		http://leon.bottou.com/objprelink/
BuildRequires:	binutils, /usr/lib/libiberty.a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} ppc

%description
This program replaces relocations in object files with less expensive
ones. This allows faster run-time dynamic linking.

%description -l pl
Ten program zamienia relokacje w plikach objekt�w na mniej wymagaj�ce.
Dzi�ki temu program jest szybciej konsolidowany w momencie
uruchomienia.

%prep
%setup -q -T -c
cp -f %{SOURCE0} .
gzip -d *.gz

%build
%{__cc} %{rpmcflags} -o objprelink objprelink.c -lbfd -liberty

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install objprelink $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
