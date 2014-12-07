# revision 15878
# category Package
# catalog-ctan /info/intro-scientific
# catalog-date 2009-02-22 10:18:48 +0100
# catalog-license lppl
# catalog-version 5th edition
Name:		texlive-intro-scientific
Version:	5
Release:	9
Summary:	Introducing scientific/mathematical documents using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/intro-scientific
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intro-scientific.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5-2
+ Revision: 752801
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5-1
+ Revision: 718727
- texlive-intro-scientific
- texlive-intro-scientific
- texlive-intro-scientific
- texlive-intro-scientific
- texlive-intro-scientific

