Name:           ocaml
Version:        3.10.2
Release:        3%{?dist}

Summary:        Objective Caml compiler and programming environment

Group:          Development/Languages
License:        QPL and (LGPLv2+ with exceptions)
URL:            http://www.ocaml.org
Source0:        http://caml.inria.fr/distrib/ocaml-3.10/ocaml-%{version}.tar.bz2
Source1:        http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.html.tar.gz
Source2:        http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.pdf
Source3:        http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.info.tar.gz
Source4:        ocaml-find-requires.sh
Source5:        ocaml-find-provides.sh
Patch0:         ocaml-rpath.patch
Patch1:         ocaml-user-cflags.patch
Patch2:         ocaml-3.10.0-tclver.patch
Patch3:         ocaml-3.10.1-ppc64.patch
Patch4:         ocaml-3.10.1-map32bit.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ncurses-devel
BuildRequires:  gdbm-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  emacs
BuildRequires:  gawk
BuildRequires:  perl
BuildRequires:  util-linux-ng
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  chrpath
Requires:       gcc
Requires:       ncurses-devel
Requires:       gdbm-devel
Provides:       ocaml(compiler) = %{version}
ExclusiveArch:  alpha armv4l %{ix86} ia64 x86_64 ppc sparc ppc64

%define _use_internal_dependency_generator 0
%define __find_requires %{SOURCE4} -i Asttypes -i Outcometree -i Cmo_format -i Parsetree -c -f %{buildroot}%{_bindir}/ocamlobjinfo
%define __find_provides %{SOURCE5} -f %{buildroot}%{_bindir}/ocamlobjinfo

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive toplevel system,
parsing tools (Lex,Yacc,Camlp4), a replay debugger, a documentation generator,
and a comprehensive library.


%package runtime
Group:          System Environment/Libraries
Summary:        Objective Caml runtime environment
Requires:       util-linux-ng
Provides:       ocaml(runtime) = %{version}

%description runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package contains the runtime environment needed to run Objective
Caml bytecode.


%package source
Group:          Development/Languages
Summary:        Source code for Objective Caml libraries
Requires:       ocaml = %{version}-%{release}

%description source
Source code for Objective Caml libraries.


%package x11
Group:          System Environment/Libraries
Summary:        X11 support for Objective Caml
Requires:       ocaml-runtime = %{version}-%{release}
Requires:       libX11-devel

%description x11
X11 support for Objective Caml.


%package labltk
Group:          System Environment/Libraries
Summary:        Tk bindings for Objective Caml
Requires:       ocaml-runtime = %{version}-%{release}

%description labltk
Labltk is a library for interfacing Objective Caml with the scripting
language Tcl/Tk.

This package contains the runtime files.


%package labltk-devel
Group:          Development/Libraries
Summary:        Development files for labltk
Requires:       ocaml = %{version}-%{release}
Requires:       %{name}-labltk = %{version}-%{release}
Requires:       libX11-devel

%description labltk-devel
Labltk is a library for interfacing Objective Caml with the scripting
language Tcl/Tk.

This package contains the development files.  It includes the ocaml
browser for code editing and library browsing.


%package camlp4
Group:          Development/Languages
Summary:        Pre-Processor-Pretty-Printer for Objective Caml
Requires:       ocaml-runtime = %{version}-%{release}

%description camlp4
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml, parsing a
source file and printing some result on standard output.

This package contains the runtime files.


%package camlp4-devel
Group:          Development/Languages
Summary:        Pre-Processor-Pretty-Printer for Objective Caml
Requires:       ocaml = %{version}-%{release}
Requires:       %{name}-camlp4 = %{version}-%{release}

%description camlp4-devel
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml, parsing a
source file and printing some result on standard output.

This package contains the development files.


%package ocamldoc
Group:          Development/Languages
Summary:        Documentation generator for Objective Caml.
Requires:       ocaml = %{version}-%{release}
Provides:	ocamldoc

%description ocamldoc
Documentation generator for Objective Caml.


%package emacs
Group:          Development/Languages
Summary:        Emacs mode for Objective Caml
Requires:       ocaml = %{version}-%{release}
Requires:       emacs

%description emacs
Emacs mode for Objective Caml.


%package docs
Group:          Development/Languages
Summary:        Documentation for Objective Caml
Requires:       ocaml = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info


%description docs
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package contains documentation in PDF and HTML format as well as
man pages and info files.


%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
%setup -q -T -D -a 3
%patch0 -p1 -b .rpath
%patch1 -p1 -b .cflags
%patch2 -p1 -b .tclver
%patch3 -p1 -b .ppc64
%patch4 -p1 -b .map32bit

cp %{SOURCE2} refman.pdf


%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
    -bindir %{_bindir} \
    -libdir %{_libdir}/ocaml \
    -x11lib %{_libdir} \
    -x11include %{_includedir} \
    -mandir %{_mandir}/man1
make world opt opt.opt
# %{?_smp_mflags} breaks the build
make -C emacs ocamltags
# make -C tools objinfo
(cd tools; ../boot/ocamlrun ../ocamlopt -nostdlib -I ../stdlib -I ../utils -I ../parsing -I ../typing -I ../bytecomp -I ../asmcomp -I ../driver -o objinfo config.cmx objinfo.ml)


%install
rm -rf $RPM_BUILD_ROOT
make install \
     BINDIR=$RPM_BUILD_ROOT%{_bindir} \
     LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
     MANDIR=$RPM_BUILD_ROOT%{_mandir}
perl -pi -e "s|^$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT%{_libdir}/ocaml/ld.conf

(
    # install emacs files
    cd emacs;
    make install \
         BINDIR=$RPM_BUILD_ROOT%{_bindir} \
         EMACSDIR=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
    make install-ocamltags BINDIR=$RPM_BUILD_ROOT%{_bindir}
)

(
    # install info files
    mkdir -p $RPM_BUILD_ROOT%{_infodir};
    cd infoman; cp ocaml*.gz $RPM_BUILD_ROOT%{_infodir}
)

cp tools/objinfo $RPM_BUILD_ROOT%{_bindir}/ocamlobjinfo

# install rpmbuild helper files
mkdir -p $RPM_BUILD_ROOT/usr/lib/rpm/
install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/rpm/
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT/usr/lib/rpm/

echo %{version} > $RPM_BUILD_ROOT%{_libdir}/ocaml/fedora-ocaml-release

# Remove rpaths from stublibs .so files.
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/*.so


%clean
rm -rf $RPM_BUILD_ROOT


%post docs
/sbin/install-info \
    --entry "* ocaml: (ocaml).   The Objective Caml compiler and programming environment" \
    --section "Programming Languages" \
    %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :


%preun docs
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%{_bindir}/ocaml
%{_bindir}/ocamlbuild
%{_bindir}/ocamlbuild.byte
%{_bindir}/ocamlbuild.native
%{_bindir}/ocamlc
%{_bindir}/ocamlc.opt
%{_bindir}/ocamlcp
%{_bindir}/ocamldebug
%{_bindir}/ocamldep
%{_bindir}/ocamldep.opt
%{_bindir}/ocamllex
%{_bindir}/ocamllex.opt
%{_bindir}/ocamlmklib
%{_bindir}/ocamlmktop
%{_bindir}/ocamlobjinfo
%{_bindir}/ocamlopt
%{_bindir}/ocamlopt.opt
%{_bindir}/ocamlprof
%{_bindir}/ocamlyacc
%{_libdir}/ocaml/addlabels
%{_libdir}/ocaml/scrapelabels
%{_libdir}/ocaml/camlheader
%{_libdir}/ocaml/camlheader_ur
%{_libdir}/ocaml/expunge
%{_libdir}/ocaml/extract_crc
%{_libdir}/ocaml/ld.conf
%{_libdir}/ocaml/Makefile.config
%{_libdir}/ocaml/*.a
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.cmx
%{_libdir}/ocaml/*.mli
%{_libdir}/ocaml/*.o
%{_libdir}/ocaml/vmthreads/*.mli
%{_libdir}/ocaml/vmthreads/*.a
%{_libdir}/ocaml/threads/*.a
%{_libdir}/ocaml/threads/*.cmxa
%{_libdir}/ocaml/threads/*.cmx
%{_libdir}/ocaml/caml
%{_libdir}/ocaml/ocamlbuild
%exclude %{_libdir}/ocaml/graphicsX11.mli


%files runtime
%defattr(-,root,root,-)
%{_bindir}/ocamlrun
%dir %{_libdir}/ocaml
%{_libdir}/ocaml/*.cmo
%{_libdir}/ocaml/*.cmi
%{_libdir}/ocaml/*.cma
%{_libdir}/ocaml/stublibs
%dir %{_libdir}/ocaml/vmthreads
%{_libdir}/ocaml/vmthreads/*.cmi
%{_libdir}/ocaml/vmthreads/*.cma
%dir %{_libdir}/ocaml/threads
%{_libdir}/ocaml/threads/*.cmi
%{_libdir}/ocaml/threads/*.cma
%{_libdir}/ocaml/fedora-ocaml-release
%attr(755,root,root) %{_prefix}/lib/rpm/*
%exclude %{_libdir}/ocaml/graphicsX11.cmi
%exclude %{_libdir}/ocaml/stublibs/dllgraphics.so
%exclude %{_libdir}/ocaml/stublibs/dlllabltk.so
%exclude %{_libdir}/ocaml/stublibs/dlltkanim.so
%doc README LICENSE Changes


%files source
%defattr(-,root,root,-)
%{_libdir}/ocaml/*.ml


%files x11
%defattr(-,root,root,-)
%{_libdir}/ocaml/graphicsX11.cmi
%{_libdir}/ocaml/graphicsX11.mli
%{_libdir}/ocaml/stublibs/dllgraphics.so


%files labltk
%defattr(-,root,root,-)
%{_bindir}/labltk
%dir %{_libdir}/ocaml/labltk
%{_libdir}/ocaml/labltk/*.cmi
%{_libdir}/ocaml/labltk/*.cma
%{_libdir}/ocaml/labltk/*.cmo
%{_libdir}/ocaml/stublibs/dlllabltk.so
%{_libdir}/ocaml/stublibs/dlltkanim.so


%files labltk-devel
%defattr(-,root,root,-)
%{_bindir}/ocamlbrowser
%{_libdir}/ocaml/labltk/labltktop
%{_libdir}/ocaml/labltk/pp
%{_libdir}/ocaml/labltk/tkcompiler
%{_libdir}/ocaml/labltk/*.a
%{_libdir}/ocaml/labltk/*.cmxa
%{_libdir}/ocaml/labltk/*.cmx
%{_libdir}/ocaml/labltk/*.mli
%{_libdir}/ocaml/labltk/*.o
%doc otherlibs/labltk/examples_labltk
%doc otherlibs/labltk/examples_camltk


%files camlp4
%defattr(-,root,root,-)
%dir %{_libdir}/ocaml/camlp4
%{_libdir}/ocaml/camlp4/*.cmi
%{_libdir}/ocaml/camlp4/*.cma
%{_libdir}/ocaml/camlp4/*.cmo
%dir %{_libdir}/ocaml/camlp4/Camlp4Filters
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmo
%dir %{_libdir}/ocaml/camlp4/Camlp4Parsers
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmo
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmi
%dir %{_libdir}/ocaml/camlp4/Camlp4Printers
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmo
%dir %{_libdir}/ocaml/camlp4/Camlp4Top
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmo


%files camlp4-devel
%defattr(-,root,root,-)
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%{_libdir}/ocaml/camlp4/*.a
%{_libdir}/ocaml/camlp4/*.cmxa
%{_libdir}/ocaml/camlp4/*.cmx
%{_libdir}/ocaml/camlp4/*.o
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.o
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.o
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.o
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Top/*.o
%{_mandir}/man1/*


%files ocamldoc
%defattr(-,root,root,-)
%{_bindir}/ocamldoc*
%{_libdir}/ocaml/ocamldoc
%doc ocamldoc/Changes.txt


%files docs
%defattr(-,root,root,-)
%doc refman.pdf htmlman
%{_infodir}/*
%{_mandir}/man3/*


%files emacs
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/*
%{_bindir}/ocamltags
%doc emacs/README


%changelog
* Wed Jun  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.10.2-3
- ocaml-ocamldoc provides ocamldoc (bz #449931).
- REMOVED provides of labltk, camlp4.  Those are libraries and all
  packages should now depend on ocaml-labltk / ocaml-camlp4 / -devel
  as appropriate.

* Thu May  8 2008 Richard W.M. Jones <rjones@redhat.com> - 3.10.2-2
- Pass MAP_32BIT to mmap (bz #445545).

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.10.2-1
- New upstream version 3.10.2 for Fedora 10.
- Cleaned up several rpmlint errors & warnings.

* Fri Feb 29 2008 David Woodhouse <dwmw2@infradead.org> - 3.10.1-2
- ppc64 port

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 3.10.1-1
- new upstream version 3.10.1

* Fri Jan  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.10.0-8
- patch for building with tcl/tk 8.5

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 3.10.0-7
- Run chrpath to delete rpaths used on some of the stublibs.
- Ignore Parsetree module in dependency calculation.
- Fixed ocaml-find-{requires,provides}.sh regexp calculation so it doesn't
  over-match module names.

* Mon Sep  3 2007 Richard W.M. Jones <rjones@redhat.com> - 3.10.0-6
- ocaml-runtime provides ocaml(runtime) = 3.10.0, and
  ocaml-find-requires.sh modified so that it adds this requires
  to other packages.  Now can upgrade base ocaml packages without
  needing to rebuild everything else.

* Mon Sep  3 2007 Richard W.M. Jones <rjones@redhat.com> - 3.10.0-5
- Don't include the release number in fedora-ocaml-release file, so
  that packages built against this won't depend on the Fedora release.

* Wed Aug 29 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.10.0-4
- added BR util-linux-ng

* Wed Aug 29 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.10.0-3
- added BR gawk

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.10.0-2
- Rebuild for selinux ppc32 issue.

* Sat Jun  2 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.10.0-1
- new version 3.10.0
- split off devel packages
- rename subpackages to use ocaml- prefix

* Thu May 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.09.3-2
- added ocamlobjinfo

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.3-1
- new version 3.09.3

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.2-2
- Rebuild for FE6

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.2-1
- new version 3.09.2

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.1-2
- Rebuild for Fedora Extras 5

* Thu Jan  5 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.1-1
- new version 3.09.1

* Sun Jan  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.09.0-1
- new version 3.09.0

* Sun Sep 11 2005 Gerard Milmeister <gemi@bluewin.ch> - 3.08.4-1
- New Version 3.08.4

* Wed May 25 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 3.08.3-5
- Bump and re-release as last build failed due to rawhide syncing.

* Sun May 22 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 3.08.3-4
- Fix for gcc4 and the 32 bit assembly in otherlibs/num.
- Fix to allow compilation with RPM_OPT_FLAG defined -O level.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 3.08.3-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar 26 2005 Gerard Milmeister <gemi@bluewin.ch> - 3.08.3-1
- New Version 3.08.3

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:3.08.2-2
- Added patch for removing rpath from shared libs

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:3.08.2-1
- New Version 3.08.2

* Thu Dec 30 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:3.07-6
- add -x11lib _prefix/X11R6/_lib to configure; fixes labltk build
  on x86_64

* Tue Dec  2 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:3.07-0.fdr.5
- ocamldoc -> ocaml-ocamldoc
- ocaml-doc -> ocaml-docs

* Fri Nov 28 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:3.07-0.fdr.4
- Make separate packages for labltk, camlp4, ocamldoc, emacs and documentation

* Thu Nov 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:3.07-0.fdr.2
- Changed license tag
- Register info files
- Honor RPM_OPT_FLAGS
- New Patch

* Fri Oct 31 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:3.07-0.fdr.1
- First Fedora release

* Mon Oct 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Updated to 3.07.

* Wed Apr  9 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Rebuilt for Red Hat 9.

* Tue Nov 26 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Added _mandir/mano/* entry
