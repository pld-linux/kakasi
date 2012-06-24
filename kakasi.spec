Summary:	KAKASI - kanji kana simple inverter
Summary(pl):	KAKASI - prosty konwerter kanji - kana
Name:		kakasi
Version:	2.3.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://kakasi.namazu.org/pub/kakasi/stable/%{name}-%{version}.tar.gz
# Source0-md5:	4eff51aafbd56c9635791a20c03efa8f
URL:		http://kakasi.namazu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAKASI is the language processing filter to convert Kanji characters
to Hiragana, Katakana or Romaji(1) and may be helpful to read Japanese
documents. Word-splitting patch has merged from version 2.3.0.

%description -l ja
KAKASI �ϴ������ʤޤ���ʸ��Ҥ餬��ʸ����޻�ʸ���Ѵ����뤳�Ȥ�
��Ū�Ȥ��ƺ��������ץ����ȼ������ΤǤ�������ˡ��С������ 2.3.0
����ϡ�ʬ�����񤭥ѥå����ޡ�������ޤ�����

%description -l pl
KAKASI to filtr konwertuj�cy japo�skie znaki Kanji na Hiragana,
Katakana lub Romaji(1), kt�ry mo�e by� pomocny przy czytaniu
japo�skich dokuemnt�w. Od wersji 2.3.0 zawiera poprawk� na dzielenie
s��w.

%package devel
Summary:	KAKASI header files
Summary(pl):	Pliki nag��wkowe KAKASI
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
KAKASI header files.

%description devel -l ja
KAKASI�Υإå��ե�����ڤӥ饤�֥��Ǥ���

%description devel -l pl
Pliki nag��wkowe KAKASI.

%package static
Summary:	KAKASI static library
Summary(pl):	Statyczna biblioteka KAKASI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
KAKASI static library.

%description static -l pl
Biblioteka statyczna KAKASI.

%package dict
Summary:	The base dictionary of KAKASI
Summary(pl):	Podstawowy s�ownik KAKASI
Group:		Applications/Text
Obsoletes:	kakasidict
Requires:	%{name} = %{version}

%description dict
The base dictionary of KAKASI.

%description dict -l ja
KAKASI�δ��ܼ���Ǥ���

%description dict -l pl
Podstawowy s�ownik KAKASI.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
install doc/kakasi.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%lang(ja) %doc NEWS ONEWS README-ja TODO doc/JISYO doc/README.lib doc/README.wakati
%attr(755,root,root) %{_bindir}/[^k]*
%attr(755,root,root) %{_bindir}/kakasi
%attr(755,root,root) %{_libdir}/libkakasi.so.*.*
%lang(ja) %{_mandir}/ja/man1/kakasi.1*
%dir %{_datadir}/kakasi
%{_datadir}/kakasi/itaijidict

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kakasi-config
%attr(755,root,root) %{_libdir}/libkakasi.so
%{_libdir}/libkakasi.la
%{_includedir}/libkakasi.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libkakasi.a

%files dict
%defattr(644,root,root,755)
%{_datadir}/kakasi/kanwadict
