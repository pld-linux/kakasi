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
KAKASI ¤Ï´Á»ú¤«¤Ê¤Þ¤¸¤êÊ¸¤ò¤Ò¤é¤¬¤ÊÊ¸¤ä¥í¡¼¥Þ»úÊ¸¤ËÊÑ´¹¤¹¤ë¤³¤È¤ò
ÌÜÅª¤È¤·¤ÆºîÀ®¤·¤¿¥×¥í¥°¥é¥à¤È¼­½ñ¤ÎÁí¾Î¤Ç¤¹¡£¤µ¤é¤Ë¡¢¥Ð¡¼¥¸¥ç¥ó 2.3.0
¤«¤é¤Ï¡¢Ê¬¤«¤Á½ñ¤­¥Ñ¥Ã¥Á¤¬¥Þ¡¼¥¸¤µ¤ì¤Þ¤·¤¿¡£

%description -l pl
KAKASI to filtr konwertuj±cy japoñskie znaki Kanji na Hiragana,
Katakana lub Romaji(1), który mo¿e byæ pomocny przy czytaniu
japoñskich dokuemntów. Od wersji 2.3.0 zawiera poprawkê na dzielenie
s³ów.

%package devel
Summary:	KAKASI header files
Summary(pl):	Pliki nag³ówkowe KAKASI
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
KAKASI header files.

%description devel -l ja
KAKASI¤Î¥Ø¥Ã¥À¥Õ¥¡¥¤¥ëµÚ¤Ó¥é¥¤¥Ö¥é¥ê¤Ç¤¹¡£

%description devel -l pl
Pliki nag³ówkowe KAKASI.

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
Summary(pl):	Podstawowy s³ownik KAKASI
Group:		Applications/Text
Obsoletes:	kakasidict
Requires:	%{name} = %{version}

%description dict
The base dictionary of KAKASI.

%description dict -l ja
KAKASI¤Î´ðËÜ¼­½ñ¤Ç¤¹¡£

%description dict -l pl
Podstawowy s³ownik KAKASI.

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
