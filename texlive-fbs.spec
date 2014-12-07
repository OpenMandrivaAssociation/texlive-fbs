# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/fbs.bst
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-fbs
Version:	20080819
Release:	9
Summary:	BibTeX style for Frontiers in Bioscience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/fbs.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbs.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A BibTeX style file made with custom-bib to fit Frontiers in
Bioscience requirements: - all authors, no et al, full author
names, initials abbreviated; - only abbreviated journal name
italicised, no abbreviation dots; - only year, no month, at end
of reference; and - DOI excluded, ISSN excluded.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/fbs/fbs.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080819-2
+ Revision: 751795
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080819-1
+ Revision: 718422
- texlive-fbs
- texlive-fbs
- texlive-fbs
- texlive-fbs

