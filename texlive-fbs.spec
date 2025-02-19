Name:		texlive-fbs
Version:	15878
Release:	2
Summary:	BibTeX style for Frontiers in Bioscience
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/fbs.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbs.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/fbs

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
