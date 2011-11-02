Name:		texlive-intro-scientific
Version:	5
Release:	1
Summary:	Introducing scientific/mathematical documents using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/intro-scientific
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}