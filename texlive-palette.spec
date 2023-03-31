Name:		texlive-palette
Version:	60119
Release:	2
Summary:	Create palettes for colors and symbols that can be swapped in
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/palette
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/palette.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/palette.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/palette.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package `palette` contains two files: `colorpalette.sty`
and `symbolpalette`. One deals with colors and the other deals
with symbols; the implementation is quite similar. With this
package you can create themes. Each of these themes have a set
of colors, and you can create palettes based on this theme with
specific color values for each of the theme's color slots. The
active palette for each theme can be swapped in to make
experimenting with colors easier or give users choices as to
which theme they pick.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/palette
%{_texmfdistdir}/tex/latex/palette
%doc %{_texmfdistdir}/doc/latex/palette

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
