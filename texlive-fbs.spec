# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/fbs.bst
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-fbs
Version:	20080819
Release:	1
Summary:	BibTeX style for Frontiers in Bioscience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/fbs.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbs.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
A BibTeX style file made with custom-bib to fit Frontiers in
Bioscience requirements: - all authors, no et al, full author
names, initials abbreviated; - only abbreviated journal name
italicised, no abbreviation dots; - only year, no month, at end
of reference; and - DOI excluded, ISSN excluded.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/fbs/fbs.bst
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
