#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-music
Version  : 40.0
Release  : 48
URL      : https://download.gnome.org/sources/gnome-music/40/gnome-music-40.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-music/40/gnome-music-40.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-music-bin = %{version}-%{release}
Requires: gnome-music-data = %{version}-%{release}
Requires: gnome-music-lib = %{version}-%{release}
Requires: gnome-music-license = %{version}-%{release}
Requires: gnome-music-locales = %{version}-%{release}
Requires: gnome-music-python = %{version}-%{release}
Requires: gnome-music-python3 = %{version}-%{release}
Requires: libmediaart
Requires: pycairo-python3
Requires: pygobject
BuildRequires : appstream-glib
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : desktop-file-utils
BuildRequires : gnome-online-accounts-dev
BuildRequires : grilo-plugins-dev
BuildRequires : itstool
BuildRequires : libdazzle-dev
BuildRequires : libmediaart
BuildRequires : libsoup-dev
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(grilo-plugins-0.3)
BuildRequires : pkgconfig(libdazzle-1.0)
BuildRequires : pkgconfig(libmediaart-2.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(tracker-sparql-2.0)
BuildRequires : pkgconfig(tracker-sparql-3.0)
BuildRequires : pygobject

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
%setup -q -n gnome-music-40.0
cd %{_builddir}/gnome-music-40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619113362
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-music
cp %{_builddir}/gnome-music-40.0/LICENSE %{buildroot}/usr/share/package-licenses/gnome-music/9c5c5b98b412c4716f04530b90c221a11d5ba18a
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang org.gnome.Music

%files
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Music/girepository-1.0/Gd-1.0.typelib
/usr/lib64/org.gnome.Music/girepository-1.0/Gfm-0.1.typelib
/usr/lib64/org.gnome.Music/pkgconfig/gfm-0.1.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-music

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Music.desktop
/usr/share/glib-2.0/schemas/org.gnome.Music.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Music.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
/usr/share/metainfo/org.gnome.Music.appdata.xml
/usr/share/org.gnome.Music/gir-1.0/Gd-1.0.gir
/usr/share/org.gnome.Music/gir-1.0/Gfm-0.1.gir
/usr/share/org.gnome.Music/org.gnome.Music.gresource

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/ca/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/cs/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/da/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/de/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/el/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/es/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/eu/gnome-music/figures/gnome-music-3.32.png
/usr/share/help/eu/gnome-music/index.page
/usr/share/help/eu/gnome-music/introduction.page
/usr/share/help/eu/gnome-music/legal.xml
/usr/share/help/eu/gnome-music/play-music.page
/usr/share/help/eu/gnome-music/playlist-create-albums.page
/usr/share/help/eu/gnome-music/playlist-create-artists.page
/usr/share/help/eu/gnome-music/playlist-create-songs.page
/usr/share/help/eu/gnome-music/playlist-delete.page
/usr/share/help/eu/gnome-music/playlist-remove-songs.page
/usr/share/help/eu/gnome-music/playlist-repeat.page
/usr/share/help/eu/gnome-music/playlist-shuffle.page
/usr/share/help/eu/gnome-music/search.page
/usr/share/help/fr/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/gl/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/hr/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/hu/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/id/gnome-music/figures/gnome-music-3.32.png
/usr/share/help/id/gnome-music/index.page
/usr/share/help/id/gnome-music/introduction.page
/usr/share/help/id/gnome-music/legal.xml
/usr/share/help/id/gnome-music/play-music.page
/usr/share/help/id/gnome-music/playlist-create-albums.page
/usr/share/help/id/gnome-music/playlist-create-artists.page
/usr/share/help/id/gnome-music/playlist-create-songs.page
/usr/share/help/id/gnome-music/playlist-delete.page
/usr/share/help/id/gnome-music/playlist-remove-songs.page
/usr/share/help/id/gnome-music/playlist-repeat.page
/usr/share/help/id/gnome-music/playlist-shuffle.page
/usr/share/help/id/gnome-music/search.page
/usr/share/help/it/gnome-music/figures/gnome-music-3.32.png
/usr/share/help/it/gnome-music/index.page
/usr/share/help/it/gnome-music/introduction.page
/usr/share/help/it/gnome-music/legal.xml
/usr/share/help/it/gnome-music/play-music.page
/usr/share/help/it/gnome-music/playlist-create-albums.page
/usr/share/help/it/gnome-music/playlist-create-artists.page
/usr/share/help/it/gnome-music/playlist-create-songs.page
/usr/share/help/it/gnome-music/playlist-delete.page
/usr/share/help/it/gnome-music/playlist-remove-songs.page
/usr/share/help/it/gnome-music/playlist-repeat.page
/usr/share/help/it/gnome-music/playlist-shuffle.page
/usr/share/help/it/gnome-music/search.page
/usr/share/help/ko/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/nl/gnome-music/figures/gnome-music-3.32.png
/usr/share/help/nl/gnome-music/index.page
/usr/share/help/nl/gnome-music/introduction.page
/usr/share/help/nl/gnome-music/legal.xml
/usr/share/help/nl/gnome-music/play-music.page
/usr/share/help/nl/gnome-music/playlist-create-albums.page
/usr/share/help/nl/gnome-music/playlist-create-artists.page
/usr/share/help/nl/gnome-music/playlist-create-songs.page
/usr/share/help/nl/gnome-music/playlist-delete.page
/usr/share/help/nl/gnome-music/playlist-remove-songs.page
/usr/share/help/nl/gnome-music/playlist-repeat.page
/usr/share/help/nl/gnome-music/playlist-shuffle.page
/usr/share/help/nl/gnome-music/search.page
/usr/share/help/pl/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/pt_BR/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/ro/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/sv/gnome-music/figures/gnome-music-3.32.png
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
/usr/share/help/uk/gnome-music/figures/gnome-music-3.32.png
/usr/share/help/uk/gnome-music/index.page
/usr/share/help/uk/gnome-music/introduction.page
/usr/share/help/uk/gnome-music/legal.xml
/usr/share/help/uk/gnome-music/play-music.page
/usr/share/help/uk/gnome-music/playlist-create-albums.page
/usr/share/help/uk/gnome-music/playlist-create-artists.page
/usr/share/help/uk/gnome-music/playlist-create-songs.page
/usr/share/help/uk/gnome-music/playlist-delete.page
/usr/share/help/uk/gnome-music/playlist-remove-songs.page
/usr/share/help/uk/gnome-music/playlist-repeat.page
/usr/share/help/uk/gnome-music/playlist-shuffle.page
/usr/share/help/uk/gnome-music/search.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Music/libgd.so
/usr/lib64/org.gnome.Music/libgfm-0.1.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-music/9c5c5b98b412c4716f04530b90c221a11d5ba18a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f org.gnome.Music.lang
%defattr(-,root,root,-)

