%global tl_name montserrat
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Montserrat sans serif, otf and pfb, with LaTeX support files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/montserrat
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/montserrat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/montserrat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Montserrat is a geometric sans-serif typeface designed by Julieta
Ulanovsky, inspired by posters and signage from her historical Buenos
Aires neighborhood of the same name. It is rather close in spirit to
Gotham and Proxima Nova, but has its own individual appearance -- more
informal, less extended, and more idiosyncratic. It is provided in a
total of nine different weights, each having eight figure styles and
small caps in both upright and italic shapes. There are two quite
different versions that don't fit into the usual LaTeX classifications.
The version having the appellation "Alternates" has letter shapes that
are much more rounded than the default version, reflecting the signage
in the neighborhood of Montserrat.

