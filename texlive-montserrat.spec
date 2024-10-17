Name:		texlive-montserrat
Version:	54512
Release:	2
Summary:	Montserrat sans serif, otf and pfb, with LaTeX support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/montserrat
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/montserrat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/montserrat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Montserrat is a geometric sans-serif typeface designed by
Julieta Ulanovsky, inspired by posters and signage from her
historical Buenos Aires neighborhood of the same name. It is
rather close in spirit to Gotham and Proxima Nova, but has its
own individual appearance -- more informal, less extended, and
more idiosyncratic. It is provided in a total of nine different
weights, each having eight figure styles and small caps in both
upright and italic shapes. There are two quite different
versions that don't fit into the usual LaTeX classifications.
The version having the appellation "Alternates" has letter
shapes that are much more rounded than the default version,
reflecting the signage in the neighborhood of Montserrat.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/montserrat
%{_texmfdistdir}/fonts/vf/public/montserrat
%{_texmfdistdir}/fonts/type1/public/montserrat
%{_texmfdistdir}/fonts/tfm/public/montserrat
%{_texmfdistdir}/fonts/opentype/public/montserrat
%{_texmfdistdir}/fonts/map/dvips/montserrat
%{_texmfdistdir}/fonts/enc/dvips/montserrat
%doc %{_texmfdistdir}/doc/fonts/montserrat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
