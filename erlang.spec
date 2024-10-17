%define build_java 1

%{expand: %{?_with_java: %%global build_java 1}}
%{expand: %{?_without_java: %%global build_java 0}}

%define erlang_libdir %{_libdir}/erlang/lib

Summary:	General-purpose programming language and runtime environment
Name:		erlang
Version:	25.1.1
Release:	1
Group:		Development/Other
License:	MPL
URL:		https://www.erlang.org
Source0:	https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz
Source1:	https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_doc_html_%{version}.tar.gz
Source2:	https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_doc_man_%{version}.tar.gz
Patch0:		otp-25.1.1-clang.patch
Patch1:		https://github.com/erlang/otp/pull/6023.patch
# fix linking by removing --no-undefined from WX_LIBS
#Patch4:		R14B03-remove-no-udefined-from-wx.patch
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libssl)
# needed for configure test
BuildRequires:	openssl
BuildRequires:	unixODBC-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%if %build_java
BuildRequires:	java-rpmbuild
%endif
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	valgrind-devel
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	m4
BuildRequires:	wxgtku3.2-devel
Requires:	tk
Requires:	tcl

%description 
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package stack
Summary:	Erlang bundle
License:	MPL
Group:		Development/Other
Requires:	erlang-base = %{version}-%{release}
Requires:	erlang-asn1
Requires:	erlang-common_test
Requires:	erlang-compiler
Requires:	erlang-crypto
Requires:	erlang-debugger
Requires:	erlang-dialyzer
Requires:	erlang-diameter
Requires:	erlang-edoc
Requires:	erlang-eldap
Requires:	erlang-emacs
Requires:	erlang-erl_docgen
Requires:	erlang-erl_interface
Requires:	erlang-et
Requires:	erlang-eunit
Requires:	erlang-inets
%if %build_java
Requires:	erlang-jinterface
%endif
Requires:	erlang-megaco
Requires:	erlang-mnesia
Requires:	erlang-observer
Requires:	erlang-odbc
Requires:	erlang-os_mon
Requires:	erlang-parsetools
Requires:	erlang-public_key
Requires:	erlang-reltool
Requires:	erlang-runtime_tools
Requires:	erlang-snmp
Requires:	erlang-ssh
Requires:	erlang-ssl
Requires:	erlang-syntax_tools
Requires:	erlang-tools
Requires:	erlang-typer
Requires:	erlang-wx
Requires:	erlang-xmerl

Obsoletes:	%{name}-mnesia_session
Obsoletes:	%{name}-mnemosyne

%description stack
Erlang bundle.

The Erlang/OTP system --- Erlang is a programming language which
has many features more commonly associated with an operating system
than with a programming language: concurrent processes, scheduling,
memory management, distribution, networking, etc. The development package
in addition contains the Erlang sources for all base libraries.
Includes the Erlang/OTP graphical libraries.

%package base
Summary:	Erlang architecture independent files
License:	MPL
Group:		Development/Other
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name}_otp
Obsoletes:	erlang-gs_apps
Obsoletes:	erlang-otp_libs

%description base
Erlang architecture independent files

The Erlang/OTP system --- Erlang is a programming language which
has many features more commonly associated with an operating system
than with a programming language: concurrent processes, scheduling,
memory management, distribution, networking, etc. The development package
in addition contains the Erlang sources for all base libraries.
Includes the Erlang/OTP graphical libraries.

%package devel
Summary:	Erlang header
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
Erlang headers.
This package is used to build some library.

%package manpages
Summary:	Erlang man pages
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description manpages
Documentation for the Erlang programming language in `man' format. This
documentation can be read using the command `erl -man mod', where `mod' is
the name of the module you want documentation on.

%package dialyzer
Summary:	Static analysis tool
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description dialyzer
Dialyzer is a static analysis tool that identifies software discrepancies 
such as type errors, unreachable code, unnecessary tests, etc in single 
Erlang modules or entire (sets of) applications.

%package diameter
Summary:	An implementation of the Diameter protocol as defined by RFC 3588
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description diameter
An implementation of the Diameter protocol as defined by RFC 3588.

%package edoc
Summary:	The Erlang program documentation generator
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Requires:	erlang-syntax_tools
Requires:	erlang-xmerl
Group:		Development/Other

%description edoc
This module provides the main user interface to EDoc.

%package eldap
Summary:	The Erlang LDAP library 
License:	MPL
Requires:	%{name}-asn1 = %{version}-%{release}
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-ssl = %{version}-%{release}
Group:		Development/Other

%description eldap
Eldap is a module which provides a client API to the Lightweight Directory
Access Protocol (LDAP).

%package emacs
Summary:	Emacs support for The Erlang language
License:	GPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other
Requires:	emacs

%description emacs
This module provides Erlang support to Emacs.

%if %build_java
%package jinterface
Summary:	Low level interface to Java
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description jinterface
The Jinterface package provides a set of tools for communication with
Erlang processes. It can also be used for communication with other Java
processes using the same package, as well as C processes using the
Erl_Interface library.
%endif

%package asn1
Summary:	Provides support for Abstract Syntax Notation One
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description asn1
Asn1 application contains modules with compile-time and run-time support for
ASN.1.

%package common_test
Summary:	Portable framework for automatic testing
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description common_test
A portable Erlang framework for automatic testing.

%package compiler
Summary:	Byte code compiler for Erlang which produces highly compact code
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description compiler
Compiler application compiles Erlang code to byte-code. The highly compact
byte-code is executed by the Erlang emulator.

%package crypto
Summary:	Cryptographical support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description crypto
Cryptographical support for erlang.

%package debugger
Summary:	Debugger for debugging and testing of Erlang programs
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description debugger
Debugger is a graphical tool which can be used for debugging and testing
of Erlang programs. For example, breakpoints can be set, code can be single
stepped and variable values can be displayed and changed.

%package erl_docgen
Summary:	Documentation generator
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description erl_docgen
Documentation generator for erlang.

%package erl_interface
Summary:	Low level interface to C
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description erl_interface
Low level interface to C for erlang.

%package et
Summary:	Event Tracer
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description et
The Event Tracer (ET) uses the built-in trace mechanism in Erlang and
provides tools for collection and graphical viewing of trace data.

%package eunit
Summary:	Erlang support for unit testing
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description eunit
Erlang support for unit testing.

%package inets
Summary:	Set of services such as a Web server and a ftp client etc
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description inets
Inets is a container for Internet clients and servers. Currently a HTTP
server and a FTP client has been incorporated in Inets. The HTTP server
is an efficient implementation of HTTP 1.1 as defined in RFC 2616, i.e.
a Web server.

%package megaco
Summary:	Framework for building applications on top of the Megaco/H.248 protocol
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description megaco
Megaco/H.248 is a protocol for control of elements in a physically decomposed
multimedia gateway, enabling separation of call control from media conversion.

%package mnesia
Summary:	Heavy duty real-time distributed database
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description mnesia
Mnesia is a distributed DataBase Management System (DBMS), appropriate for
telecommunications applications and other Erlang applications which require
continuous operation and exhibit soft real-time properties.

%package observer
Summary:	Observer, tools for tracing and investigation of distributed systems
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description observer
The OBSERVER application contains tools for tracing and investigation of
distributed systems.

%package odbc
Summary: 	Interface to relational SQL-databases built on ODBC
License: 	MPL
Requires: 	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description odbc
The ODBC application is an interface to relational SQL-databases built 
on ODBC (Open Database.)

%package os_mon
Summary:	Monitor which allows inspection of the underlying operating system
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description os_mon
The operating system monitor OS_Mon monitors operating system disk and memory
usage etc.

%package parsetools
Summary:	Set of parsing and lexical analysis tools
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description parsetools
The Parsetools application contains utilities for parsing, e.g. the yecc
module. Yecc is an LALR-1 parser generator for Erlang, similar to yacc.
Yecc takes a BNF grammar definition as input, and produces Erlang code for
a parser as output.

%package public_key
Summary:	Erlang API to public key infrastructure
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description public_key
Erlang API to public key infrastructure.

%package reltool
Summary:	A release management tool for Erlang
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description reltool
It analyses a given Erlang/OTP installation and determines various
dependencies between applications. The graphical frontend depicts
the dependencies and enables interactive customization of a
target system. The backend provides a batch interface for
generation of customized target systems.

%package runtime_tools
Summary:	Runtime tools, tools to include in a production system
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description runtime_tools
Runtime tools, tools to include in a production system.

%package snmp
Summary:	Simple Network Management Protocol (SNMP) support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description snmp
A multilingual Simple Network Management Protocol Extensible Agent, featuring
a MIB compiler and facilities for implementing SNMP MIBs etc.

%package ssh
Summary:	Secure Shell application with ssh and sftp support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description ssh
Secure Shell application with ssh and sftp support.

%package ssl
Summary:	Interface to UNIX BSD sockets with Secure Sockets Layer
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description ssl
The SSL application provides secure communication over sockets.

%package syntax_tools
Summary:	Set of modules for working with Erlang source code
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description syntax_tools
This package defines an abstract datatype that is compatible with the
`erl_parse' data structures, and provides modules for analysis and
manipulation, flexible pretty printing, and preservation of source-code
comments. Now includes `erl_tidy': automatic code tidying and checking.

%package tools
Summary:	Set of programming tools including a coverage analyzer etc
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description tools
The Tools application contains a number of stand-alone tools, which are
useful when developing Erlang programs.

%package typer
Summary:	Type annotator of Erlang code
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description typer
A type annotator of Erlang code.

%package wx
Summary:	Graphic system for Erlang
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description wx
A Graphics System used to write platform independent user interfaces
for Erlang.

%package xmerl
Summary:	XML processing tools
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description xmerl
Implements a set of tools for processing XML documents, as well as working
with XML-like structures in Erlang. The main attraction so far is a
single-pass, highly customizable XML processor. Other components are an
export/translation facility and an XPATH query engine. This version fixes
a few bugs in the scanner, and improves HTML export.

%prep
%autosetup -p1 -n otp_src_%{version}

%build
%serverbuild
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXLAGS=$CFLAGS
ERL_TOP=`pwd`; export ERL_TOP

# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
#define __cputoolize true
%define _disable_ld_no_undefined 1

%configure2_5x \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--datadir=%{_datadir} \
	%ifarch x86_64
	--enable-m64-build \
	%endif
	--enable-threads \
	--enable-kernel-poll \
	--enable-smp-support \
	--with-ssl \
	--disable-erlang-mandir \
	--enable-dynamic-ssl-lib

%make -j1

%install

%makeinstall_std INSTALL_PREFIX=%{buildroot}

# clean up
find %{buildroot}%{_libdir}/erlang -perm 0775 | xargs chmod 755
find %{buildroot}%{_libdir}/erlang -name Makefile | xargs chmod 644
find %{buildroot}%{_libdir}/erlang -name \*.bat | xargs rm -f
find %{buildroot}%{_libdir}/erlang -name index.txt.old | xargs rm -f

# doc
mkdir -p erlang_doc
mkdir -p %{buildroot}%{_mandir}/erlang
tar -C erlang_doc -xf %{SOURCE1}
tar -C %{buildroot}%{_datadir} -xf %{SOURCE2}

# make links to binaries
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
for file in erl erlc escript run_erl
do
  ln -sf ../%{_lib}/erlang/bin/$file .
done
popd

# (tpg) fixes bug #32318
mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat > %{buildroot}%{_sysconfdir}/emacs/site-start.d/erlang.el << EOF
(setq load-path (cons "%{_libdir}/%{name}/lib/tools-*/emacs" load-path))
(add-to-list 'load-path "%{_datadir}/emacs/site-lisp/ess")
(load-library "erlang-start")
EOF

# remove buildroot from installed files
pushd %{buildroot}%{_libdir}/erlang
sed -i "s|%{buildroot}||" erts*/bin/{erl,start} releases/RELEASES bin/{erl,start}
popd

# (tpg) remove not needed files
rm -rf %{buildroot}%{_datadir}/COPYRIGHT
rm -rf %{buildroot}%{_datadir}/PR.template
rm -rf %{buildroot}%{_datadir}/README

# (tpg) remove this manpages as they conflicts with openssl
rm -rf %{buildroot}%{_mandir}/man3/ssl.3.*
rm -rf %{buildroot}%{_mandir}/man3/crypto.3.*
rm -rf %{buildroot}%{_mandir}/man3/zlib.3.*

%post base
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null

%files stack
%doc AUTHORS README.md

%files base
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/bin
%dir %{_libdir}/erlang/lib
%dir %{_libdir}/erlang/misc
%{_bindir}/*
%{_libdir}/erlang/Install
%{_libdir}/erlang/bin/ct_run
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/bin/erl
%{_libdir}/erlang/bin/erl_call
%{_libdir}/erlang/bin/erlc
%{_libdir}/erlang/bin/escript
%{_libdir}/erlang/bin/start.boot
%{_libdir}/erlang/bin/start.script
%{_libdir}/erlang/bin/start_clean.boot
%{_libdir}/erlang/bin/start_sasl.boot
%{_libdir}/erlang/bin/no_dot_erlang.boot
%{_libdir}/erlang/erts-*
%{_libdir}/erlang/misc/format_man_pages
%{_libdir}/erlang/misc/makewhatis
%{_libdir}/erlang/releases
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/to_erl
%{erlang_libdir}/erts-*
%{erlang_libdir}/kernel-*
%{erlang_libdir}/stdlib-*
%{erlang_libdir}/sasl-*

%files devel
%dir %{_libdir}/%{name}/%{_includedir}
%dir %{_libdir}/%{name}/%{_prefix}/lib
%{_libdir}/%{name}/%{_includedir}/*
%{_libdir}/%{name}/%{_prefix}/lib/*

%files asn1
%{erlang_libdir}/asn1-*

%files compiler
%{erlang_libdir}/compiler-*

%files common_test
%{erlang_libdir}/common_test-*

%files crypto
%{erlang_libdir}/crypto-*

%files debugger
%{erlang_libdir}/debugger-*

%files dialyzer
%{erlang_libdir}/dialyzer-*
%{_libdir}/%{name}/bin/dialyzer

%files diameter
%{erlang_libdir}/diameter-*

%files edoc
%{erlang_libdir}/edoc-*

%files eldap
%{erlang_libdir}/eldap-*

%files emacs
%{_sysconfdir}/emacs/site-start.d/erlang.el

%files erl_docgen
%{erlang_libdir}/erl_docgen-*

%files erl_interface
%{erlang_libdir}/erl_interface-*

%files et
%{erlang_libdir}/et-*

%files eunit
%{erlang_libdir}/eunit-*

%files inets
%{erlang_libdir}/inets-*
%{erlang_libdir}/ftp-*
%{erlang_libdir}/tftp-*

%if %build_java
%files jinterface
%{erlang_libdir}/jinterface-*
%endif

%files manpages
%{_mandir}/*/*

%files megaco
%{erlang_libdir}/megaco-*

%files mnesia
%{erlang_libdir}/mnesia-*

%files observer
%{erlang_libdir}/observer-*

%files odbc
%{erlang_libdir}/odbc-*

%files os_mon
%{erlang_libdir}/os_mon-*

%files parsetools
%{erlang_libdir}/parsetools-*

%files public_key
%{erlang_libdir}/public_key-*

%files reltool
%{erlang_libdir}/reltool-*

%files runtime_tools
%{erlang_libdir}/runtime_tools-*

%files snmp
%{erlang_libdir}/snmp-*

%files ssh
%{erlang_libdir}/ssh-*

%files ssl
%{erlang_libdir}/ssl-*

%files syntax_tools
%{erlang_libdir}/syntax_tools-*

%files tools
%{erlang_libdir}/tools-*

%files typer
%{_libdir}/%{name}/bin/typer

%files wx
%{erlang_libdir}/wx-*

%files xmerl
%{erlang_libdir}/xmerl-*
