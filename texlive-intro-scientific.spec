%global tl_name intro-scientific
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5th.edition
Release:	%{tl_revision}.1
Summary:	Introducing scientific/mathematical documents using LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/intro-scientific
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"Writing Scientific Documents Using LaTeX" is an article introducing the
use of LaTeX in typesetting scientific documents. It covers the basics
of creating a new LaTeX document, special typesetting considerations,
mathematical typesetting and graphics. It also touches on bibliographic
data and BibTeX.

