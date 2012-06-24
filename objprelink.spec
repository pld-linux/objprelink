Summary:	Tool to optimize relocations in object files
Summary(pl):	Narz�dzie optymalizuj�ce relokacje w plikach objekt�w
Name:		objprelink
Version:	1
Release:	2
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://www.research.att.com/~leonb/objprelink/%{name}.c.gz
URL:		http://www.research.att.com/~leonb/objprelink/
BuildRequires:	binutils
BuildRequires:	binutils-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program replaces relocations in object files with less expensive
ones. This allows faster run-time dynamic linking.

%description -l pl
Ten program zamienia relokacje w plikach objekt�w na mniej wymagaj�ce.
Dzi�ki temu program jest szybciej linkowany w momencie uruchomienia.

%prep
%setup -q -T -c
cp -f %{SOURCE0} .
gzip -d *.gz

%build
%{__cc} %{rpmcflags} -o objprelink objprelink.c -lbfd /usr/lib/libiberty.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install objprelink $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
