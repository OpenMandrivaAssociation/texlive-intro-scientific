Name:		texlive-intro-scientific
Version:	15878
Release:	2
Summary:	Introducing scientific/mathematical documents using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/intro-scientific
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
"Writing Scientific Documents Using LaTeX" is an article
introducing the use of LaTeX in typesetting scientific
documents. It covers the basics of creating a new LaTeX
document, special typesetting considerations, mathematical
typesetting and graphics. It also touches on bibliographic data
and BibTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/intro-scientific/Makefile
%doc %{_texmfdistdir}/doc/latex/intro-scientific/README
%doc %{_texmfdistdir}/doc/latex/intro-scientific/earth-moon.pdf
%doc %{_texmfdistdir}/doc/latex/intro-scientific/scidoc.pdf
%doc %{_texmfdistdir}/doc/latex/intro-scientific/scidoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
