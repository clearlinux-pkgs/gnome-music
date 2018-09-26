#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-music
Version  : 3.30.1
Release  : 17
URL      : https://download.gnome.org/sources/gnome-music/3.30/gnome-music-3.30.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-music/3.30/gnome-music-3.30.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-music-bin
Requires: gnome-music-python3
Requires: gnome-music-lib
Requires: gnome-music-data
Requires: gnome-music-license
Requires: gnome-music-locales
Requires: gnome-music-python
Requires: libmediaart
Requires: pycairo-python3
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : desktop-file-utils
BuildRequires : gnome-online-accounts-dev
BuildRequires : grilo-plugins-dev
BuildRequires : itstool
BuildRequires : libdazzle-dev
BuildRequires : libsoup-dev
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(libmediaart-2.0)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(tracker-sparql-2.0)

%description
=====
libgd
=====
Introduction
============
libgd is a library used by various GNOME 3 styled applications.
However, it is not a typical library, since it doesn't guarantee
API/ABI stability, nor does it has official releases tarballs. Only
the files actually used by your project will be shipped with its
tarball. Only the necessary dependencies will be checked during
configure time and used at runtime.

%package bin
Summary: bin components for the gnome-music package.
Group: Binaries
Requires: gnome-music-data = %{version}-%{release}
Requires: gnome-music-license = %{version}-%{release}

%description bin
bin components for the gnome-music package.


%package data
Summary: data components for the gnome-music package.
Group: Data

%description data
data components for the gnome-music package.


%package doc
Summary: doc components for the gnome-music package.
Group: Documentation

%description doc
doc components for the gnome-music package.


%package lib
Summary: lib components for the gnome-music package.
Group: Libraries
Requires: gnome-music-data = %{version}-%{release}
Requires: gnome-music-license = %{version}-%{release}

%description lib
lib components for the gnome-music package.


%package license
Summary: license components for the gnome-music package.
Group: Default

%description license
license components for the gnome-music package.


%package locales
Summary: locales components for the gnome-music package.
Group: Default

%description locales
locales components for the gnome-music package.


%package python
Summary: python components for the gnome-music package.
Group: Default
Requires: gnome-music-python3 = %{version}-%{release}

%description python
python components for the gnome-music package.


%package python3
Summary: python3 components for the gnome-music package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gnome-music package.


%prep
%setup -q -n gnome-music-3.30.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537945213
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-music
cp LICENSE %{buildroot}/usr/share/doc/gnome-music/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang org.gnome.Music

%files
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Music/girepository-1.0/Gd-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-music

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Music.desktop
/usr/share/glib-2.0/schemas/org.gnome.Music.gschema.xml
/usr/share/icons/hicolor/16x16/apps/org.gnome.Music.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Music.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Music.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Music.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Music.png
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
/usr/share/metainfo/org.gnome.Music.appdata.xml
/usr/share/org.gnome.Music/gir-1.0/Gd-1.0.gir
/usr/share/org.gnome.Music/org.gnome.Music.gresource

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/C/gnome-music/index.page
/usr/share/help/C/gnome-music/introduction.page
/usr/share/help/C/gnome-music/legal.xml
/usr/share/help/C/gnome-music/play-music.page
/usr/share/help/C/gnome-music/playlist-create-albums.page
/usr/share/help/C/gnome-music/playlist-create-artists.page
/usr/share/help/C/gnome-music/playlist-create-songs.page
/usr/share/help/C/gnome-music/playlist-delete.page
/usr/share/help/C/gnome-music/playlist-remove-songs.page
/usr/share/help/C/gnome-music/playlist-repeat.page
/usr/share/help/C/gnome-music/playlist-shuffle.page
/usr/share/help/C/gnome-music/search.page
/usr/share/help/ca/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/ca/gnome-music/index.page
/usr/share/help/ca/gnome-music/introduction.page
/usr/share/help/ca/gnome-music/legal.xml
/usr/share/help/ca/gnome-music/play-music.page
/usr/share/help/ca/gnome-music/playlist-create-albums.page
/usr/share/help/ca/gnome-music/playlist-create-artists.page
/usr/share/help/ca/gnome-music/playlist-create-songs.page
/usr/share/help/ca/gnome-music/playlist-delete.page
/usr/share/help/ca/gnome-music/playlist-remove-songs.page
/usr/share/help/ca/gnome-music/playlist-repeat.page
/usr/share/help/ca/gnome-music/playlist-shuffle.page
/usr/share/help/ca/gnome-music/search.page
/usr/share/help/cs/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/cs/gnome-music/index.page
/usr/share/help/cs/gnome-music/introduction.page
/usr/share/help/cs/gnome-music/legal.xml
/usr/share/help/cs/gnome-music/play-music.page
/usr/share/help/cs/gnome-music/playlist-create-albums.page
/usr/share/help/cs/gnome-music/playlist-create-artists.page
/usr/share/help/cs/gnome-music/playlist-create-songs.page
/usr/share/help/cs/gnome-music/playlist-delete.page
/usr/share/help/cs/gnome-music/playlist-remove-songs.page
/usr/share/help/cs/gnome-music/playlist-repeat.page
/usr/share/help/cs/gnome-music/playlist-shuffle.page
/usr/share/help/cs/gnome-music/search.page
/usr/share/help/da/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/da/gnome-music/index.page
/usr/share/help/da/gnome-music/introduction.page
/usr/share/help/da/gnome-music/legal.xml
/usr/share/help/da/gnome-music/play-music.page
/usr/share/help/da/gnome-music/playlist-create-albums.page
/usr/share/help/da/gnome-music/playlist-create-artists.page
/usr/share/help/da/gnome-music/playlist-create-songs.page
/usr/share/help/da/gnome-music/playlist-delete.page
/usr/share/help/da/gnome-music/playlist-remove-songs.page
/usr/share/help/da/gnome-music/playlist-repeat.page
/usr/share/help/da/gnome-music/playlist-shuffle.page
/usr/share/help/da/gnome-music/search.page
/usr/share/help/de/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/de/gnome-music/index.page
/usr/share/help/de/gnome-music/introduction.page
/usr/share/help/de/gnome-music/legal.xml
/usr/share/help/de/gnome-music/play-music.page
/usr/share/help/de/gnome-music/playlist-create-albums.page
/usr/share/help/de/gnome-music/playlist-create-artists.page
/usr/share/help/de/gnome-music/playlist-create-songs.page
/usr/share/help/de/gnome-music/playlist-delete.page
/usr/share/help/de/gnome-music/playlist-remove-songs.page
/usr/share/help/de/gnome-music/playlist-repeat.page
/usr/share/help/de/gnome-music/playlist-shuffle.page
/usr/share/help/de/gnome-music/search.page
/usr/share/help/el/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/el/gnome-music/index.page
/usr/share/help/el/gnome-music/introduction.page
/usr/share/help/el/gnome-music/legal.xml
/usr/share/help/el/gnome-music/play-music.page
/usr/share/help/el/gnome-music/playlist-create-albums.page
/usr/share/help/el/gnome-music/playlist-create-artists.page
/usr/share/help/el/gnome-music/playlist-create-songs.page
/usr/share/help/el/gnome-music/playlist-delete.page
/usr/share/help/el/gnome-music/playlist-remove-songs.page
/usr/share/help/el/gnome-music/playlist-repeat.page
/usr/share/help/el/gnome-music/playlist-shuffle.page
/usr/share/help/el/gnome-music/search.page
/usr/share/help/es/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/es/gnome-music/index.page
/usr/share/help/es/gnome-music/introduction.page
/usr/share/help/es/gnome-music/legal.xml
/usr/share/help/es/gnome-music/play-music.page
/usr/share/help/es/gnome-music/playlist-create-albums.page
/usr/share/help/es/gnome-music/playlist-create-artists.page
/usr/share/help/es/gnome-music/playlist-create-songs.page
/usr/share/help/es/gnome-music/playlist-delete.page
/usr/share/help/es/gnome-music/playlist-remove-songs.page
/usr/share/help/es/gnome-music/playlist-repeat.page
/usr/share/help/es/gnome-music/playlist-shuffle.page
/usr/share/help/es/gnome-music/search.page
/usr/share/help/fr/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/fr/gnome-music/index.page
/usr/share/help/fr/gnome-music/introduction.page
/usr/share/help/fr/gnome-music/legal.xml
/usr/share/help/fr/gnome-music/play-music.page
/usr/share/help/fr/gnome-music/playlist-create-albums.page
/usr/share/help/fr/gnome-music/playlist-create-artists.page
/usr/share/help/fr/gnome-music/playlist-create-songs.page
/usr/share/help/fr/gnome-music/playlist-delete.page
/usr/share/help/fr/gnome-music/playlist-remove-songs.page
/usr/share/help/fr/gnome-music/playlist-repeat.page
/usr/share/help/fr/gnome-music/playlist-shuffle.page
/usr/share/help/fr/gnome-music/search.page
/usr/share/help/gl/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/gl/gnome-music/index.page
/usr/share/help/gl/gnome-music/introduction.page
/usr/share/help/gl/gnome-music/legal.xml
/usr/share/help/gl/gnome-music/play-music.page
/usr/share/help/gl/gnome-music/playlist-create-albums.page
/usr/share/help/gl/gnome-music/playlist-create-artists.page
/usr/share/help/gl/gnome-music/playlist-create-songs.page
/usr/share/help/gl/gnome-music/playlist-delete.page
/usr/share/help/gl/gnome-music/playlist-remove-songs.page
/usr/share/help/gl/gnome-music/playlist-repeat.page
/usr/share/help/gl/gnome-music/playlist-shuffle.page
/usr/share/help/gl/gnome-music/search.page
/usr/share/help/hr/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/hr/gnome-music/index.page
/usr/share/help/hr/gnome-music/introduction.page
/usr/share/help/hr/gnome-music/legal.xml
/usr/share/help/hr/gnome-music/play-music.page
/usr/share/help/hr/gnome-music/playlist-create-albums.page
/usr/share/help/hr/gnome-music/playlist-create-artists.page
/usr/share/help/hr/gnome-music/playlist-create-songs.page
/usr/share/help/hr/gnome-music/playlist-delete.page
/usr/share/help/hr/gnome-music/playlist-remove-songs.page
/usr/share/help/hr/gnome-music/playlist-repeat.page
/usr/share/help/hr/gnome-music/playlist-shuffle.page
/usr/share/help/hr/gnome-music/search.page
/usr/share/help/hu/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/hu/gnome-music/index.page
/usr/share/help/hu/gnome-music/introduction.page
/usr/share/help/hu/gnome-music/legal.xml
/usr/share/help/hu/gnome-music/play-music.page
/usr/share/help/hu/gnome-music/playlist-create-albums.page
/usr/share/help/hu/gnome-music/playlist-create-artists.page
/usr/share/help/hu/gnome-music/playlist-create-songs.page
/usr/share/help/hu/gnome-music/playlist-delete.page
/usr/share/help/hu/gnome-music/playlist-remove-songs.page
/usr/share/help/hu/gnome-music/playlist-repeat.page
/usr/share/help/hu/gnome-music/playlist-shuffle.page
/usr/share/help/hu/gnome-music/search.page
/usr/share/help/ko/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/ko/gnome-music/index.page
/usr/share/help/ko/gnome-music/introduction.page
/usr/share/help/ko/gnome-music/legal.xml
/usr/share/help/ko/gnome-music/play-music.page
/usr/share/help/ko/gnome-music/playlist-create-albums.page
/usr/share/help/ko/gnome-music/playlist-create-artists.page
/usr/share/help/ko/gnome-music/playlist-create-songs.page
/usr/share/help/ko/gnome-music/playlist-delete.page
/usr/share/help/ko/gnome-music/playlist-remove-songs.page
/usr/share/help/ko/gnome-music/playlist-repeat.page
/usr/share/help/ko/gnome-music/playlist-shuffle.page
/usr/share/help/ko/gnome-music/search.page
/usr/share/help/pl/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/pl/gnome-music/index.page
/usr/share/help/pl/gnome-music/introduction.page
/usr/share/help/pl/gnome-music/legal.xml
/usr/share/help/pl/gnome-music/play-music.page
/usr/share/help/pl/gnome-music/playlist-create-albums.page
/usr/share/help/pl/gnome-music/playlist-create-artists.page
/usr/share/help/pl/gnome-music/playlist-create-songs.page
/usr/share/help/pl/gnome-music/playlist-delete.page
/usr/share/help/pl/gnome-music/playlist-remove-songs.page
/usr/share/help/pl/gnome-music/playlist-repeat.page
/usr/share/help/pl/gnome-music/playlist-shuffle.page
/usr/share/help/pl/gnome-music/search.page
/usr/share/help/pt_BR/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/pt_BR/gnome-music/index.page
/usr/share/help/pt_BR/gnome-music/introduction.page
/usr/share/help/pt_BR/gnome-music/legal.xml
/usr/share/help/pt_BR/gnome-music/play-music.page
/usr/share/help/pt_BR/gnome-music/playlist-create-albums.page
/usr/share/help/pt_BR/gnome-music/playlist-create-artists.page
/usr/share/help/pt_BR/gnome-music/playlist-create-songs.page
/usr/share/help/pt_BR/gnome-music/playlist-delete.page
/usr/share/help/pt_BR/gnome-music/playlist-remove-songs.page
/usr/share/help/pt_BR/gnome-music/playlist-repeat.page
/usr/share/help/pt_BR/gnome-music/playlist-shuffle.page
/usr/share/help/pt_BR/gnome-music/search.page
/usr/share/help/ro/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/ro/gnome-music/index.page
/usr/share/help/ro/gnome-music/introduction.page
/usr/share/help/ro/gnome-music/legal.xml
/usr/share/help/ro/gnome-music/play-music.page
/usr/share/help/ro/gnome-music/playlist-create-albums.page
/usr/share/help/ro/gnome-music/playlist-create-artists.page
/usr/share/help/ro/gnome-music/playlist-create-songs.page
/usr/share/help/ro/gnome-music/playlist-delete.page
/usr/share/help/ro/gnome-music/playlist-remove-songs.page
/usr/share/help/ro/gnome-music/playlist-repeat.page
/usr/share/help/ro/gnome-music/playlist-shuffle.page
/usr/share/help/ro/gnome-music/search.page
/usr/share/help/sv/gnome-music/figures/gnome-music-3.12.png
/usr/share/help/sv/gnome-music/index.page
/usr/share/help/sv/gnome-music/introduction.page
/usr/share/help/sv/gnome-music/legal.xml
/usr/share/help/sv/gnome-music/play-music.page
/usr/share/help/sv/gnome-music/playlist-create-albums.page
/usr/share/help/sv/gnome-music/playlist-create-artists.page
/usr/share/help/sv/gnome-music/playlist-create-songs.page
/usr/share/help/sv/gnome-music/playlist-delete.page
/usr/share/help/sv/gnome-music/playlist-remove-songs.page
/usr/share/help/sv/gnome-music/playlist-repeat.page
/usr/share/help/sv/gnome-music/playlist-shuffle.page
/usr/share/help/sv/gnome-music/search.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Music/libgd.so

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/gnome-music/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f org.gnome.Music.lang
%defattr(-,root,root,-)

