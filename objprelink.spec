Summary:	Tool to optimize relocations in object files
Summary(pl):	Narzêdzie optymalizuj±ce relokacje w plikach objektów
Name:		objprelink
Version:	1
Release:	4
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://leon.bottou.com/objprelink/%{name}.c.gz
URL:		http://leon.bottou.com/objprelink/
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
