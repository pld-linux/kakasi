Summary:	KAKASI - kanji kana simple inverter
Summary(pl.UTF-8):	KAKASI - prosty konwerter kanji - kana
Name:		kakasi
Version:	2.3.4
Release:	4
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

%description -l ja.UTF-8
KAKASI は漢字かなまじり文をひらがな文やローマ字文に変換することを
目的として作成したプログラムと辞書の総称です。さらに、バージョン 2.3.0
からは、分かち書きパッチがマージされました。

%description -l pl.UTF-8
KAKASI to filtr konwertujący japońskie znaki Kanji na Hiragana,
Katakana lub Romaji(1), który może być pomocny przy czytaniu
japońskich dokumentów. Od wersji 2.3.0 zawiera poprawkę na dzielenie
słów.

%package devel
Summary:	KAKASI header files
Summary(pl.UTF-8):	Pliki nagłówkowe KAKASI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
KAKASI header files.

%description devel -l ja.UTF-8
KAKASIのヘッダファイル及びライブラリです。

%description devel -l pl.UTF-8
Pliki nagłówkowe KAKASI.

%package static
Summary:	KAKASI static library
Summary(pl.UTF-8):	Statyczna biblioteka KAKASI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
KAKASI static library.

%description static -l pl.UTF-8
Biblioteka statyczna KAKASI.

%package dict
Summary:	The base dictionary of KAKASI
Summary(pl.UTF-8):	Podstawowy słownik KAKASI
Group:		Applications/Text
Obsoletes:	kakasidict
Requires:	%{name} = %{version}-%{release}

%description dict
The base dictionary of KAKASI.

%description dict -l ja.UTF-8
KAKASIの基本辞書です。

%description dict -l pl.UTF-8
Podstawowy słownik KAKASI.

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
%attr(755,root,root) %ghost %{_libdir}/libkakasi.so.2
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
