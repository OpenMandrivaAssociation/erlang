%define build_java 1

%{expand: %{?_with_java: %%global build_java 1}}
%{expand: %{?_without_java: %%global build_java 0}}

%define erlang_libdir %{_libdir}/erlang/lib
%define realver R14B

Summary:	General-purpose programming language and runtime environment
Name:		erlang
Version:	%(echo %realver | sed -e 's/-//')
Release:	%mkrel 1
Group:		Development/Other
License:	MPL
URL:		http://www.erlang.org
Source0:	http://www.erlang.org/download/otp_src_%{realver}.tar.xz
Source1:	http://www.erlang.org/download/otp_doc_html_%{realver}.tar.xz
Source2:	http://www.erlang.org/download/otp_doc_man_%{realver}.tar.xz
Patch0:		otp-links.patch
Patch1:		otp-install.patch
Patch2:		otp_src_R13B01-rpath.patch
Patch3:		otp_src_R12B-5-fix-format-errors.patch
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
# needed for configure test
BuildRequires:	openssl
BuildRequires:	unixODBC-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%if %build_java
BuildRequires:  java-rpmbuild
%endif
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libgd-devel
BuildRequires:	valgrind
BuildRequires:	libgd-devel
BuildRequires:	m4
BuildRequires:	wxgtku-devel
Requires:	tk
Requires:	tcl
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description 
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package -n %{name}-stack
Summary:	Erlang bundle
License:	MPL
Group:		Development/Other
Requires:	erlang-base = %{version}-%{release}
Requires:	erlang-appmon
Requires:	erlang-asn1
Requires:	erlang-common_test
Requires:	erlang-compiler
Requires:	erlang-cosEvent
Requires:	erlang-cosEventDomain
Requires:	erlang-cosFileTransfer
Requires:	erlang-cosNotification
Requires:	erlang-cosProperty
Requires:	erlang-cosTime
Requires:	erlang-cosTransactions
Requires:	erlang-crypto
Requires:	erlang-debugger
Requires:	erlang-dialyzer
Requires:	erlang-docbuilder
Requires:	erlang-edoc
Requires:	erlang-emacs
Requires:	erlang-erl_docgen
Requires:	erlang-erl_interface
Requires:	erlang-et
Requires:	erlang-eunit
Requires:	erlang-gs
Requires:	erlang-hipe
Requires:	erlang-ic
Requires:	erlang-inets
Requires:	erlang-inviso
%if %build_java
Requires:	erlang-jinterface
%endif
#Requires:	erlang-kernel
Requires:	erlang-megaco
Requires:	erlang-mnesia
Requires:	erlang-observer
Requires:	erlang-odbc
Requires:	erlang-orber
Requires:	erlang-os_mon
Requires:	erlang-otp_mibs
Requires:	erlang-parsetools
Requires:	erlang-percept
Requires:	erlang-pman
Requires:	erlang-public_key
Requires:	erlang-reltool
Requires:	erlang-runtime_tools
#Requires:	erlang-sasl
Requires:	erlang-snmp
Requires:	erlang-ssh
Requires:	erlang-ssl
#Requires:	erlang-stdlib
Requires:	erlang-syntax_tools
Requires:	erlang-test_server
Requires:	erlang-toolbar
Requires:	erlang-tools
Requires:	erlang-tv
Requires:	erlang-typer
Requires:	erlang-webtool
Requires:	erlang-wx
Requires:	erlang-xmerl

Obsoletes:	%{name}-mnesia_session
Obsoletes:	%{name}-mnemosyne

%description -n %{name}-stack
Erlang bundle.

The Erlang/OTP system --- Erlang is a programming language which
has many features more commonly associated with an operating system
than with a programming language: concurrent processes, scheduling,
memory management, distribution, networking, etc. The development package
in addition contains the Erlang sources for all base libraries.
Includes the Erlang/OTP graphical libraries.

%package -n %{name}-base
Summary:	Erlang architecture independent files
License:	MPL
Group:		Development/Other
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name}_otp
Obsoletes:	erlang-gs_apps
Obsoletes:	erlang-otp_libs

%description -n %{name}-base
Erlang architecture independent files

The Erlang/OTP system --- Erlang is a programming language which
has many features more commonly associated with an operating system
than with a programming language: concurrent processes, scheduling,
memory management, distribution, networking, etc. The development package
in addition contains the Erlang sources for all base libraries.
Includes the Erlang/OTP graphical libraries.

%package -n %{name}-devel
Summary:	Erlang header
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{name}-devel
Erlang headers.
This package is used to build some library.

%package -n %{name}-manpages
Summary:	Erlang man pages
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-manpages
Documentation for the Erlang programming language in `man' format. This
documentation can be read using the command `erl -man mod', where `mod' is
the name of the module you want documentation on.

%package -n %{name}-appmon
Summary:	Utility used to supervise Applications executing on several Erlang nodes
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-appmon
Appmon, is a graphical utility used to supervise applications executing
either locally or on remote nodes. The process tree of an application
can furthermore be monitored.

%package -n %{name}-dialyzer
Summary:	Static analysis tool
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-dialyzer
Dialyzer is a static analysis tool that identifies software discrepancies 
such as type errors, unreachable code, unnecessary tests, etc in single 
Erlang modules or entire (sets of) applications.

%package -n %{name}-edoc
Summary:	The Erlang program documentation generator
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Requires:	erlang-syntax_tools
Requires:	erlang-xmerl
Group:		Development/Other

%description -n %{name}-edoc
This module provides the main user interface to EDoc.

%package -n %{name}-emacs
Summary:	Emacs support for The Erlang language
License:	GPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other
Requires:	emacs

%description -n %{name}-emacs
This module provides Erlang support to Emacs.

%if %build_java
%package -n %{name}-jinterface
Summary:	Low level interface to Java
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-jinterface
The Jinterface package provides a set of tools for communication with
Erlang processes. It can also be used for communication with other Java
processes using the same package, as well as C processes using the
Erl_Interface library.
%endif

%package -n %{name}-asn1
Summary:	Provides support for Abstract Syntax Notation One
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-asn1
Asn1 application contains modules with compile-time and run-time support for
ASN.1.

%package -n %{name}-common_test
Summary:	Portable framework for automatic testing
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-common_test
A portable Erlang framework for automatic testing.

%package -n %{name}-compiler
Summary:	Byte code compiler for Erlang which produces highly compact code
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-compiler
Compiler application compiles Erlang code to byte-code. The highly compact
byte-code is executed by the Erlang emulator.

%package -n %{name}-cosEvent
Summary:	Orber OMG Event Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosEvent
The cosEvent application is an Erlang implementation of a CORBA Service
CosEvent.

%package -n %{name}-cosEventDomain
Summary:	Orber OMG Event Domain Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosEventDomain
The cosEventDomain application is an Erlang implementation of a CORBA
Service CosEventDomainAdmin.

%package -n %{name}-cosFileTransfer
Summary:	Orber OMG File Transfer Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosFileTransfer
The cosFileTransfer Application is an Erlang implementation of the
OMG CORBA File Transfer Service.

%package -n %{name}-cosNotification
Summary:	Orber OMG Notification Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosNotification
The cosNotification application is an Erlang implementation of the OMG
CORBA Notification Service.

%package -n %{name}-cosProperty
Summary:	Orber OMG Property Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosProperty
The cosProperty Application is an Erlang implementation of the OMG
CORBA Property Service.

%package -n %{name}-cosTime
Summary:	Orber OMG Timer and TimerEvent Services
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosTime
The cosTime application is an Erlang implementation of the OMG
CORBA Time and TimerEvent Services.

%package -n %{name}-cosTransactions
Summary:	Orber OMG Transaction Service
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-cosTransactions
The cosTransactions application is an Erlang implementation of the OMG
CORBA Transaction Service.

%package -n %{name}-crypto
Summary:	Cryptographical support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-crypto
Cryptographical support for erlang.

%package -n %{name}-debugger
Summary:	Debugger for debugging and testing of Erlang programs
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-debugger
Debugger is a graphical tool which can be used for debugging and testing
of Erlang programs. For example, breakpoints can be set, code can be single
stepped and variable values can be displayed and changed.

%package -n %{name}-docbuilder
Summary:	Tool for generating HTML documentation for Erlang programs
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-docbuilder
A tool for generating HTML documentation for Erlang programs.

%package -n %{name}-erl_docgen
Summary:	Documentation generator
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-erl_docgen
Documentation generator for erlang.

%package -n %{name}-erl_interface
Summary:	Low level interface to C
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-erl_interface
Low level interface to C for erlang.

%package -n %{name}-et
Summary:	Event Tracer
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-et
The Event Tracer (ET) uses the built-in trace mechanism in Erlang and
provides tools for collection and graphical viewing of trace data.

%package -n %{name}-eunit
Summary:	Erlang support for unit testing
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-eunit
Erlang support for unit testing.

%package -n %{name}-gs
Summary:	Graphics System used to write platform independent user interfaces
License:	MPL
Requires:	%{name}-base = %{version}-%{release}, tk, tcl
Group:		Development/Other

%description -n %{name}-gs
The Graphics System application, GS, is a library of routines for writing
graphical user interfaces. Programs written using GS work on all Erlang
platforms and do not depend upon the underlying windowing system.

%package -n %{name}-hipe
Summary:	High performance erlang
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-hipe
High-performance erlang.

%package -n %{name}-inviso
Summary:	Erlang trace tool
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-inviso
An Erlang trace tool.

%package -n %{name}-ic
Summary:	IDL compiler
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-ic
The IC application is an Erlang implementation of an IDL compiler.

%package -n %{name}-inets
Summary:	Set of services such as a Web server and a ftp client etc
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-inets
Inets is a container for Internet clients and servers. Currently a HTTP
server and a FTP client has been incorporated in Inets. The HTTP server
is an efficient implementation of HTTP 1.1 as defined in RFC 2616, i.e.
a Web server.

%package -n %{name}-megaco
Summary:	Framework for building applications on top of the Megaco/H.248 protocol
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-megaco
Megaco/H.248 is a protocol for control of elements in a physically decomposed
multimedia gateway, enabling separation of call control from media conversion.

%package -n %{name}-mnesia
Summary:	Heavy duty real-time distributed database
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-mnesia
Mnesia is a distributed DataBase Management System (DBMS), appropriate for
telecommunications applications and other Erlang applications which require
continuous operation and exhibit soft real-time properties.

%package -n %{name}-observer
Summary:	Observer, tools for tracing and investigation of distributed systems
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-observer
The OBSERVER application contains tools for tracing and investigation of
distributed systems.

%package -n %{name}-odbc
Summary: 	Interface to relational SQL-databases built on ODBC
License: 	MPL
Requires: 	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-odbc
The ODBC application is an interface to relational SQL-databases built 
on ODBC (Open Database.)

%package -n %{name}-orber
Summary:	CORBA Object Request Broker
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-orber
The Orber application is an Erlang implementation of a CORBA Object Request
Broker.

%package -n %{name}-os_mon
Summary:	Monitor which allows inspection of the underlying operating system
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-os_mon
The operating system monitor OS_Mon monitors operating system disk and memory
usage etc.

%package -n %{name}-otp_mibs
Summary:	Snmp management information base for Erlang
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-otp_mibs
The OTP_Mibs application provides an SNMP management information base for
Erlang nodes.

%package -n %{name}-parsetools
Summary:	Set of parsing and lexical analysis tools
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-parsetools
The Parsetools application contains utilities for parsing, e.g. the yecc
module. Yecc is an LALR-1 parser generator for Erlang, similar to yacc.
Yecc takes a BNF grammar definition as input, and produces Erlang code for
a parser as output.

%package -n %{name}-percept
Summary:	Concurrency profiler tool for Erlang
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-percept
A concurrency profiler tool for Erlang.

%package -n %{name}-pman
Summary:	Process manager used to inspect the state of an Erlang system
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-pman
The process manager Pman is a graphical tool used to inspect the Erlang
processes executing either locally or on remote nodes. It is also possible
to trace events in the individual processes.

%package -n %{name}-public_key
Summary:	Erlang API to public key infrastructure
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-public_key
Erlang API to public key infrastructure.

%package -n %{name}-reltool
Summary:	A release management tool for Erlang
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-reltool
It analyses a given Erlang/OTP installation and determines various
dependencies between applications. The graphical frontend depicts
the dependencies and enables interactive customization of a
target system. The backend provides a batch interface for
generation of customized target systems.

%package -n %{name}-runtime_tools
Summary:	Runtime tools, tools to include in a production system
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-runtime_tools
Runtime tools, tools to include in a production system.

%package -n %{name}-snmp
Summary:	Simple Network Management Protocol (SNMP) support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-snmp
A multilingual Simple Network Management Protocol Extensible Agent, featuring
a MIB compiler and facilities for implementing SNMP MIBs etc.

%package -n %{name}-ssh
Summary:	Secure Shell application with ssh and sftp support
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-ssh
Secure Shell application with ssh and sftp support.

%package -n %{name}-ssl
Summary:	Interface to UNIX BSD sockets with Secure Sockets Layer
License:	MPL
Requires:	%{name}-base = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-ssl
The SSL application provides secure communication over sockets.

%package -n %{name}-syntax_tools
Summary:	Set of modules for working with Erlang source code
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-syntax_tools
This package defines an abstract datatype that is compatible with the
`erl_parse' data structures, and provides modules for analysis and
manipulation, flexible pretty printing, and preservation of source-code
comments. Now includes `erl_tidy': automatic code tidying and checking.

%package -n %{name}-test_server
Summary:	The OTP test sewrver for Erlang
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-test_server
The OTP test sewrver for Erlang.

%package -n %{name}-toolbar
Summary:	Tool bar simplifying access to the Erlang tools
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-toolbar
The Toolbar application simplifies access to the Erlang/OTP tools. It
consists of a number of power buttons, one for each available tool.

%package -n %{name}-tools
Summary:	Set of programming tools including a coverage analyzer etc
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-tools
The Tools application contains a number of stand-alone tools, which are
useful when developing Erlang programs.

%package -n %{name}-typer
Summary:	Type annotator of Erlang code
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-typer
A type annotator of Erlang code.

%package -n %{name}-tv
Summary:	ETS and MNESIA graphical table visualizer
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-tv
The TV application enables the user to examine ETS and Mnesia tables.
Once a certain table has been opened in the tool, the content may be viewed
in various levels of detail.

%package -n %{name}-webtool
Summary:	Tool that simplifying the use of web based Erlang tools
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-webtool
Erlang Module to configure,and start the webserver httpd and the various
web based tools to Erlang/OTP.

%package -n %{name}-wx
Summary:	Graphic system for Erlang
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-wx
A Graphics System used to write platform independent user interfaces
for Erlang.

%package -n %{name}-xmerl
Summary:	XML processing tools
License:	MPL
Group:		Development/Other
Requires:	%{name}-base = %{version}-%{release}

%description -n %{name}-xmerl
Implements a set of tools for processing XML documents, as well as working
with XML-like structures in Erlang. The main attraction so far is a
single-pass, highly customizable XML processor. Other components are an
export/translation facility and an XPATH query engine. This version fixes
a few bugs in the scanner, and improves HTML export.

%prep
%setup -qn otp_src_%{realver}
#%patch0 -p1 -b .links
#%patch1 -p1 -b .install fixd
#%patch2 -p1 -b .rpath rediff
%patch3 -p1 -b .format

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
	--enable-hipe \
	--enable-smp-support \
	--with-ssl \
	--disable-erlang-mandir \
	--enable-dynamic-ssl-lib

%make -j1

%install
rm -rf %{buildroot}

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

%clean
rm -rf

%post -n %{name}-base
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null

%if %mdkversion < 200900
%post -n %{name}-crypto -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{name}-crypto -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{name}-asn1 -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{name}-asn1 -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{name}-runtime_tools -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{name}-runtime_tools -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{name}-megaco -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{name}-megaco -p /sbin/ldconfig
%endif

%files -n %{name}-stack
%defattr(-,root,root)
%doc AUTHORS EPLICENCE README.md

%files -n %{name}-base
%defattr(-,root,root)
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/bin
%dir %{_libdir}/erlang/lib
%dir %{_libdir}/erlang/misc
%{_bindir}/*
%{_libdir}/erlang/Install
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/bin/erl
%{_libdir}/erlang/bin/erlc
%{_libdir}/erlang/bin/escript
%{_libdir}/erlang/bin/start.boot
%{_libdir}/erlang/bin/start.script
%{_libdir}/erlang/bin/start_clean.boot
%{_libdir}/erlang/bin/start_sasl.boot
%{_libdir}/erlang/erts-*
%{_libdir}/erlang/misc/format_man_pages
%{_libdir}/erlang/misc/makewhatis
%{_libdir}/erlang/releases
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/run_test
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/to_erl
%{erlang_libdir}/erts-*
%{erlang_libdir}/kernel-*
%{erlang_libdir}/stdlib-*
%{erlang_libdir}/sasl-*

%files -n %{name}-devel
%defattr(-,root,root)
%dir %{_libdir}/%{name}/%{_includedir}
%dir %{_libdir}/%{name}/%{_prefix}/lib
%{_libdir}/%{name}/%{_includedir}/*
%{_libdir}/%{name}/%{_prefix}/lib/*

%files -n %{name}-appmon
%defattr(-,root,root)
%{erlang_libdir}/appmon-*

%files -n %{name}-asn1
%defattr(-,root,root)
%{erlang_libdir}/asn1-*

%files -n %{name}-compiler
%defattr(-,root,root)
%{erlang_libdir}/compiler-*

%files -n %{name}-common_test
%defattr(-,root,root)
%{erlang_libdir}/common_test-*

%files -n %{name}-cosEvent
%defattr(-,root,root)
%{erlang_libdir}/cosEvent-*

%files -n %{name}-cosEventDomain
%defattr(-,root,root)
%{erlang_libdir}/cosEventDomain-*

%files -n %{name}-cosFileTransfer
%defattr(-,root,root)
%{erlang_libdir}/cosFileTransfer-*

%files -n %{name}-cosNotification
%defattr(-,root,root)
%{erlang_libdir}/cosNotification-*

%files -n %{name}-cosProperty
%defattr(-,root,root)
%{erlang_libdir}/cosProperty-*

%files -n %{name}-cosTime
%defattr(-,root,root)
%{erlang_libdir}/cosTime-*

%files -n %{name}-cosTransactions
%defattr(-,root,root)
%{erlang_libdir}/cosTransactions-*

%files -n %{name}-crypto
%defattr(-,root,root)
%{erlang_libdir}/crypto-*

%files -n %{name}-debugger
%defattr(-,root,root)
%{erlang_libdir}/debugger-*

%files -n %{name}-docbuilder
%defattr(-,root,root)
%{erlang_libdir}/docbuilder-*

%files -n %{name}-dialyzer
%defattr(-,root,root)
%{erlang_libdir}/dialyzer-*
%{_libdir}/%{name}/bin/dialyzer

%files -n %{name}-edoc
%defattr(-,root,root)
%{erlang_libdir}/edoc-*

%files -n %{name}-emacs
%defattr(-,root,root)
%{_sysconfdir}/emacs/site-start.d/erlang.el

%files -n %{name}-erl_docgen
%defattr(-,root,root)
%{erlang_libdir}/erl_docgen-*

%files -n %{name}-erl_interface
%defattr(-,root,root)
%{erlang_libdir}/erl_interface-*

%files -n %{name}-et
%defattr(-,root,root)
%{erlang_libdir}/et-*

%files -n %{name}-eunit
%defattr(-,root,root)
%{erlang_libdir}/eunit-*

%files -n %{name}-gs
%defattr(-,root,root)
%{erlang_libdir}/gs-*

%files -n %{name}-hipe
%defattr(-,root,root)
%{erlang_libdir}/hipe-*

%files -n %{name}-ic
%defattr(-,root,root)
%{erlang_libdir}/ic-*

%files -n %{name}-inets
%defattr(-,root,root)
%{erlang_libdir}/inets-*

%files -n %{name}-inviso
%defattr(-,root,root)
%{erlang_libdir}/inviso-*

%if %build_java
%files -n %{name}-jinterface
%defattr(-,root,root)
%{erlang_libdir}/jinterface-*/priv/OtpErlang.jar
%{erlang_libdir}/jinterface-*/java_src/com/ericsson/otp/erlang/*
%endif

%files -n %{name}-manpages
%defattr(-,root,root)
%{_mandir}/*

%files -n %{name}-megaco
%defattr(-,root,root)
%{erlang_libdir}/megaco-*

%files -n %{name}-mnesia
%defattr(-,root,root)
%{erlang_libdir}/mnesia-*

%files -n %{name}-observer
%defattr(-,root,root)
%{erlang_libdir}/observer-*

%files -n %{name}-odbc
%defattr(-,root,root)
%{erlang_libdir}/odbc-*

%files -n %{name}-orber
%defattr(-,root,root)
%{erlang_libdir}/orber-*

%files -n %{name}-os_mon
%defattr(-,root,root)
%{erlang_libdir}/os_mon-*

%files -n %{name}-otp_mibs
%defattr(-,root,root)
%{erlang_libdir}/otp_mibs-*

%files -n %{name}-parsetools
%defattr(-,root,root)
%{erlang_libdir}/parsetools-*

%files -n %{name}-percept
%defattr(-,root,root)
%{erlang_libdir}/percept-*

%files -n %{name}-pman
%defattr(-,root,root)
%{erlang_libdir}/pman-*

%files -n %{name}-public_key
%defattr(-,root,root)
%{erlang_libdir}/public_key-*

%files -n %{name}-reltool
%defattr(-,root,root)
%{erlang_libdir}/reltool-*

%files -n %{name}-runtime_tools
%defattr(-,root,root)
%{erlang_libdir}/runtime_tools-*

%files -n %{name}-snmp
%defattr(-,root,root)
%{erlang_libdir}/snmp-*

%files -n %{name}-ssh
%defattr(-,root,root)
%{erlang_libdir}/ssh-*

%files -n %{name}-ssl
%defattr(-,root,root)
%{erlang_libdir}/ssl-*

%files -n %{name}-syntax_tools
%defattr(-,root,root)
%{erlang_libdir}/syntax_tools-*

%files -n %{name}-test_server
%defattr(-,root,root)
%{erlang_libdir}/test_server-*

%files -n %{name}-toolbar
%defattr(-,root,root)
%{erlang_libdir}/toolbar-*

%files -n %{name}-tools
%defattr(-,root,root)
%{erlang_libdir}/tools-*

%files -n %{name}-typer
%defattr(-,root,root)
%{erlang_libdir}/typer-*
%{_libdir}/%{name}/bin/typer

%files -n %{name}-tv
%defattr(-,root,root)
%{erlang_libdir}/tv-*

%files -n %{name}-webtool
%defattr(-,root,root)
%{erlang_libdir}/webtool-*

%files -n %{name}-wx
%defattr(-,root,root)
%{erlang_libdir}/wx-*

%files -n %{name}-xmerl
%defattr(-,root,root)
%{erlang_libdir}/xmerl-*
