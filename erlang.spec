%define build_java 1

%{expand: %{?_with_java: %%global build_java 1}}
%{expand: %{?_without_java: %%global build_java 0}}

%define erts_version 5.6.5
%define appmon_version 2.1.9
%define asn1_version 1.6.2
%define common_test_version 1.3.4
%define compiler_version 4.5.5
%define cosEvent_version 2.1.4
%define cosEventDomain_version 1.1.4
%define cosFileTransfer_version 1.1.6
%define cosNotification_version 1.1.9
%define cosProperty_version 1.1.7
%define cosTime_version 1.1.4
%define cosTransactions_version 1.2.5
%define crypto_version 1.5.3
%define debugger_version 3.1.1.4
%define dialyzer_version 1.8.3
%define docbuilder_version 0.9.8.4
%define edoc_version 0.7.6.2
%define emacs_version 0.0.1
%define erl_interface_version 3.5.9
%define et_version 1.3
%define eunit_version 2.0
%define gs_version 1.5.9
%define hipe_version 3.6.9
%define ic_version 4.2.19
%define inets_version 5.0.12
%define inviso_version 0.6
%if %build_java
%define jinterface_version 1.4.2
%endif
%define kernel_version 2.12.5
%define megaco_version 3.9.1.1
%define mnesia_version 4.4.7
%define observer_version 0.9.7.4
%define odbc_version 2.10.3
%define orber_version 3.6.10
%define os_mon_version 2.1.8
%define otp_mibs_version 1.0.4.1
%define parsetools_version 1.4.5
%define percept_version 0.7.3
%define pman_version 2.6
%define public_key_version 0.1
%define runtime_tools_version 1.7.3
%define sasl_version 2.1.5.4
%define snmp_version 4.12
%define ssh_version 1.0.2
%define ssl_version 3.10
%define stdlib_version 1.15.5
%define syntax_tools_version 1.5.6
%define test_server_version 3.2.4
%define toolbar_version 1.3.0.1
%define tools_version 2.6.2
%define tv_version 2.1.4.2
%define typer_version 0.1.5
%define webtool_version 0.8.3.2
%define xmerl_version 1.1.10

%define erlang_libdir %{_libdir}/erlang/lib
%define realver R12B-5

Name:		erlang
Version:	%(echo %realver | sed -e 's/-//')
Release:	%mkrel 1
Summary:	General-purpose programming language and runtime environment
Group:		Development/Other
License:	MPL style
URL:		http://www.erlang.org
Source:		http://www.erlang.org/download/otp_src_%{realver}.tar.lzma
Source1:	http://www.erlang.org/download/otp_doc_html_%{realver}.tar.lzma
Source2:	http://www.erlang.org/download/otp_doc_man_%{realver}.tar.lzma
Patch0:		otp-links.patch
Patch1:		otp-install.patch
Patch2:		otp_src_R12B-3-rpath.patch
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
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
License:	MPL-like
Requires:	erlang-appmon
Requires:	erlang-asn1
Requires:	erlang-base
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
Requires:	erlang-manpages
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
Requires:	erlang-runtime_tools
Requires:	erlang-snmp
Requires:	erlang-ssh
Requires:	erlang-ssl
Requires:	erlang-syntax_tools
Requires:	erlang-test_server
Requires:	erlang-toolbar
Requires:	erlang-tools
Requires:	erlang-typer
Requires:	erlang-tv
Requires:	erlang-webtool
Requires:	erlang-xmerl
Group:		Development/Other
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
License:	MPL-like
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name}_otp erlang-gs_apps erlang-otp_libs
Group:		Development/Other

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
License:	MPL-like
Requires:	erlang-base
Provides:	%{name}-devel = %{version}-%{release}
Group:		Development/Other

%description -n %{name}-devel
Erlang headers.
This package is used to build some library.

%package -n %{name}-manpages
Summary:	Erlang man pages
License:	MPL-like
Requires:	%{name}-base
Group:		Development/Other

%description -n %{name}-manpages
Documentation for the Erlang programming language in `man' format. This
documentation can be read using the command `erl -man mod', where `mod' is
the name of the module you want documentation on.

%package -n %{name}-appmon
Summary:	Utility used to supervise Applications executing on several Erlang nodes
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-appmon
Appmon, is a graphical utility used to supervise applications executing
either locally or on remote nodes. The process tree of an application
can furthermore be monitored.

%package -n %{name}-dialyzer
Summary:	Static analysis tool
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-dialyzer
Dialyzer is a static analysis tool that identifies software discrepancies 
such as type errors, unreachable code, unnecessary tests, etc in single 
Erlang modules or entire (sets of) applications.

%package -n %{name}-edoc
Summary:	The Erlang program documentation generator
License:	MPL-like
Requires:	erlang-base
Requires:	erlang-syntax_tools
Requires:	erlang-xmerl
Group:		Development/Other

%description -n %{name}-edoc
This module provides the main user interface to EDoc.

%package -n %{name}-emacs
Summary:	Emacs support for The Erlang language
License:	GPL
Requires:	erlang-base
Group:		Development/Other
Requires:	emacs

%description -n %{name}-emacs
This module provides Erlang support to Emacs.

%if %build_java
%package -n %{name}-jinterface
Summary:	Low level interface to Java
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-jinterface
The Jinterface package provides a set of tools for communication with
Erlang processes. It can also be used for communication with other Java
processes using the same package, as well as C processes using the
Erl_Interface library.
%endif

%package -n %{name}-asn1
Summary:	Provides support for Abstract Syntax Notation One
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-asn1
Asn1 application contains modules with compile-time and run-time support for
ASN.1.

%package -n %{name}-common_test
Summary:	Portable framework for automatic testing
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-common_test
A portable Erlang framework for automatic testing.

%package -n %{name}-compiler
Summary:	Byte code compiler for Erlang which produces highly compact code
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-compiler
Compiler application compiles Erlang code to byte-code. The highly compact
byte-code is executed by the Erlang emulator.

%package -n %{name}-cosEvent
Summary:	Orber OMG Event Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosEvent
The cosEvent application is an Erlang implementation of a CORBA Service
CosEvent.

%package -n %{name}-cosEventDomain
Summary:	Orber OMG Event Domain Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosEventDomain
The cosEventDomain application is an Erlang implementation of a CORBA
Service CosEventDomainAdmin.

%package -n %{name}-cosFileTransfer
Summary:	Orber OMG File Transfer Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosFileTransfer
The cosFileTransfer Application is an Erlang implementation of the
OMG CORBA File Transfer Service.

%package -n %{name}-cosNotification
Summary:	Orber OMG Notification Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosNotification
The cosNotification application is an Erlang implementation of the OMG
CORBA Notification Service.

%package -n %{name}-cosProperty
Summary:	Orber OMG Property Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosProperty
The cosProperty Application is an Erlang implementation of the OMG
CORBA Property Service.

%package -n %{name}-cosTime
Summary:	Orber OMG Timer and TimerEvent Services
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosTime
The cosTime application is an Erlang implementation of the OMG
CORBA Time and TimerEvent Services.

%package -n %{name}-cosTransactions
Summary:	Orber OMG Transaction Service
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-cosTransactions
The cosTransactions application is an Erlang implementation of the OMG
CORBA Transaction Service.

%package -n %{name}-crypto
Summary:	Cryptographical support
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-crypto
Cryptographical support for erlang.

%package -n %{name}-debugger
Summary:	Debugger for debugging and testing of Erlang programs
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-debugger
Debugger is a graphical tool which can be used for debugging and testing
of Erlang programs. For example, breakpoints can be set, code can be single
stepped and variable values can be displayed and changed.

%package -n %{name}-docbuilder
Summary:	Tool for generating HTML documentation for Erlang programs
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-docbuilder
A tool for generating HTML documentation for Erlang programs.

%package -n %{name}-erl_interface
Summary:	Low level interface to C
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-erl_interface
Low level interface to C for erlang.

%package -n %{name}-et
Summary:	Event Tracer
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-et
The Event Tracer (ET) uses the built-in trace mechanism in Erlang and
provides tools for collection and graphical viewing of trace data.

%package -n %{name}-eunit
Summary:	Erlang support for unit testing
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-eunit
Erlang support for unit testing.

%package -n %{name}-gs
Summary:	Graphics System used to write platform independent user interfaces
License:	MPL-like
Requires:	erlang-base, tk, tcl
Group:		Development/Other

%description -n %{name}-gs
The Graphics System application, GS, is a library of routines for writing
graphical user interfaces. Programs written using GS work on all Erlang
platforms and do not depend upon the underlying windowing system.

%package -n %{name}-hipe
Summary:	High performance erlang
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-hipe
High-performance erlang.

%package -n %{name}-inviso
Summary:	Erlang trace tool
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-inviso
An Erlang trace tool.

%package -n %{name}-ic
Summary:	IDL compiler
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-ic
The IC application is an Erlang implementation of an IDL compiler.

%package -n %{name}-inets
Summary:	Set of services such as a Web server and a ftp client etc
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-inets
Inets is a container for Internet clients and servers. Currently a HTTP
server and a FTP client has been incorporated in Inets. The HTTP server
is an efficient implementation of HTTP 1.1 as defined in RFC 2616, i.e.
a Web server.

%package -n %{name}-megaco
Summary:	framework for building applications on top of the Megaco/H.248 protocol
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-megaco
Megaco/H.248 is a protocol for control of elements in a physically decomposed
multimedia gateway, enabling separation of call control from media conversion.

%package -n %{name}-mnesia
Summary:	Heavy duty real-time distributed database
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-mnesia
Mnesia is a distributed DataBase Management System (DBMS), appropriate for
telecommunications applications and other Erlang applications which require
continuous operation and exhibit soft real-time properties.

%package -n %{name}-observer
Summary:	Observer, tools for tracing and investigation of distributed systems
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-observer
The OBSERVER application contains tools for tracing and investigation of
distributed systems.

%package -n %{name}-odbc
Summary: 	Interface to relational SQL-databases built on ODBC
License: 	MPL-like
Requires: 	erlang-base
Group:		Development/Other

%description -n %{name}-odbc
The ODBC application is an interface to relational SQL-databases built 
on ODBC (Open Database.)

%package -n %{name}-orber
Summary:	CORBA Object Request Broker
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-orber
The Orber application is an Erlang implementation of a CORBA Object Request
Broker.

%package -n %{name}-os_mon
Summary:	Monitor which allows inspection of the underlying operating system
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-os_mon
The operating system monitor OS_Mon monitors operating system disk and memory
usage etc.

%package -n %{name}-otp_mibs
Summary:	Snmp management information base for Erlang
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-otp_mibs
The OTP_Mibs application provides an SNMP management information base for
Erlang nodes.

%package -n %{name}-parsetools
Summary:	Set of parsing and lexical analysis tools
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-parsetools
The Parsetools application contains utilities for parsing, e.g. the yecc
module. Yecc is an LALR-1 parser generator for Erlang, similar to yacc.
Yecc takes a BNF grammar definition as input, and produces Erlang code for
a parser as output.

%package -n %{name}-percept
Summary:	Concurrency profiler tool for Erlang
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-percept
A concurrency profiler tool for Erlang.

%package -n %{name}-pman
Summary:	Process manager used to inspect the state of an Erlang system
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-pman
The process manager Pman is a graphical tool used to inspect the Erlang
processes executing either locally or on remote nodes. It is also possible
to trace events in the individual processes.

%package -n %{name}-public_key
Summary:	Erlang API to public key infrastructure
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-public_key
Erlang API to public key infrastructure.

%package -n %{name}-runtime_tools
Summary:	Runtime tools, tools to include in a production system
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-runtime_tools
Runtime tools, tools to include in a production system.

%package -n %{name}-snmp
Summary:	Simple Network Management Protocol (SNMP) support
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-snmp
A multilingual Simple Network Management Protocol Extensible Agent, featuring
a MIB compiler and facilities for implementing SNMP MIBs etc.

%package -n %{name}-ssh
Summary:	Secure Shell application with ssh and sftp support
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-ssh
Secure Shell application with ssh and sftp support.

%package -n %{name}-ssl
Summary:	Interface to UNIX BSD sockets with Secure Sockets Layer
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-ssl
The SSL application provides secure communication over sockets.

%package -n %{name}-syntax_tools
Summary:	Set of modules for working with Erlang source code
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-syntax_tools
This package defines an abstract datatype that is compatible with the
`erl_parse' data structures, and provides modules for analysis and
manipulation, flexible pretty printing, and preservation of source-code
comments. Now includes `erl_tidy': automatic code tidying and checking.

%package -n %{name}-test_server
Summary:	The OTP test sewrver for Erlang
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-test_server
The OTP test sewrver for Erlang.

%package -n %{name}-toolbar
Summary:	Tool bar simplifying access to the Erlang tools
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-toolbar
The Toolbar application simplifies access to the Erlang/OTP tools. It
consists of a number of power buttons, one for each available tool.

%package -n %{name}-tools
Summary:	Set of programming tools including a coverage analyzer etc
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-tools
The Tools application contains a number of stand-alone tools, which are
useful when developing Erlang programs.

%package -n %{name}-typer
Summary:	Type annotator of Erlang code
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-typer
A type annotator of Erlang code.

%package -n %{name}-tv
Summary:	ETS and MNESIA graphical table visualizer
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-tv
The TV application enables the user to examine ETS and Mnesia tables.
Once a certain table has been opened in the tool, the content may be viewed
in various levels of detail.

%package -n %{name}-webtool
Summary:	Tool that simplifying the use of web based Erlang tools
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-webtool
Erlang Module to configure,and start the webserver httpd and the various
web based tools to Erlang/OTP.

%package -n %{name}-xmerl
Summary:	XML processing tools
License:	MPL-like
Requires:	erlang-base
Group:		Development/Other

%description -n %{name}-xmerl
Implements a set of tools for processing XML documents, as well as working
with XML-like structures in Erlang. The main attraction so far is a
single-pass, highly customizable XML processor. Other components are an
export/translation facility and an XPATH query engine. This version fixes
a few bugs in the scanner, and improves HTML export.

%prep
%setup -qn otp_src_%{realver}
%patch0 -p1 -b .links
%patch1 -p1 -b .install
%patch2 -p1 -b .rpath

%build
%serverbuild
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXLAGS=$CFLAGS
ERL_TOP=`pwd`; export ERL_TOP

# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
sed -i 's|^LD.*=.*|LD = gcc -shared|' lib/common_test/c_src/Makefile
%define __cputoolize true

%configure2_5x \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--datadir=%{_datadir} \
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
(setq load-path (cons "%{_libdir}/%{name}/lib/tools-%{tools_version}/emacs" load-path))
(add-to-list 'load-path "%{_datadir}/emacs/site-lisp/ess")
(load-library "erlang-start")
EOF

# remove buildroot from installed files
pushd %{buildroot}%{_libdir}/erlang
sed -i "s|%{buildroot}||" erts*/bin/{erl,start} releases/RELEASES bin/{erl,start}
popd

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
%doc AUTHORS EPLICENCE README

%files -n %{name}-base
%defattr(-,root,root)
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/bin
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
%{_libdir}/erlang/erts-%{erts_version}
%{_libdir}/erlang/misc/format_man_pages
%{_libdir}/erlang/misc/makewhatis
%{_libdir}/erlang/releases
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/to_erl
%{erlang_libdir}/kernel-%{kernel_version}
%{erlang_libdir}/stdlib-%{stdlib_version}
%{erlang_libdir}/sasl-%{sasl_version}

%files -n %{name}-devel
%defattr(-,root,root)
%dir %{_libdir}/%{name}/%{_includedir}
%dir %{_libdir}/%{name}/%{_prefix}/lib
%{_libdir}/%{name}/%{_includedir}/*
%{_libdir}/%{name}/%{_prefix}/lib/*

%files -n %{name}-appmon
%defattr(-,root,root)
%{erlang_libdir}/appmon-%{appmon_version}

%files -n %{name}-asn1
%defattr(-,root,root)
%{erlang_libdir}/asn1-%{asn1_version}

%files -n %{name}-compiler
%defattr(-,root,root)
%{erlang_libdir}/compiler-%{compiler_version}

%files -n %{name}-common_test
%defattr(-,root,root)
%{erlang_libdir}/common_test-%{common_test_version}

%files -n %{name}-cosEvent
%defattr(-,root,root)
%{erlang_libdir}/cosEvent-%{cosEvent_version}

%files -n %{name}-cosEventDomain
%defattr(-,root,root)
%{erlang_libdir}/cosEventDomain-%{cosEventDomain_version}

%files -n %{name}-cosFileTransfer
%defattr(-,root,root)
%{erlang_libdir}/cosFileTransfer-%{cosFileTransfer_version}

%files -n %{name}-cosNotification
%defattr(-,root,root)
%{erlang_libdir}/cosNotification-%{cosNotification_version}

%files -n %{name}-cosProperty
%defattr(-,root,root)
%{erlang_libdir}/cosProperty-%{cosProperty_version}

%files -n %{name}-cosTime
%defattr(-,root,root)
%{erlang_libdir}/cosTime-%{cosTime_version}

%files -n %{name}-cosTransactions
%defattr(-,root,root)
%{erlang_libdir}/cosTransactions-%{cosTransactions_version}

%files -n %{name}-crypto
%defattr(-,root,root)
%{erlang_libdir}/crypto-%{crypto_version}

%files -n %{name}-debugger
%defattr(-,root,root)
%{erlang_libdir}/debugger-%{debugger_version}

%files -n %{name}-docbuilder
%defattr(-,root,root)
%{erlang_libdir}/docbuilder-%{docbuilder_version}

%files -n %{name}-dialyzer
%defattr(-,root,root)
%{erlang_libdir}/dialyzer-%{dialyzer_version}
%{_libdir}/%{name}/bin/dialyzer

%files -n %{name}-edoc
%defattr(-,root,root)
%{erlang_libdir}/edoc-%{edoc_version}

%files -n %{name}-emacs
%defattr(-,root,root)
%{_sysconfdir}/emacs/site-start.d/erlang.el

%files -n %{name}-erl_interface
%defattr(-,root,root)
%{erlang_libdir}/erl_interface-%{erl_interface_version}

%files -n %{name}-et
%defattr(-,root,root)
%{erlang_libdir}/et-%{et_version}

%files -n %{name}-eunit
%defattr(-,root,root)
%{erlang_libdir}/eunit-%{eunit_version}

%files -n %{name}-gs
%defattr(-,root,root)
%{erlang_libdir}/gs-%{gs_version}

%files -n %{name}-hipe
%defattr(-,root,root)
%{erlang_libdir}/hipe-%{hipe_version}

%files -n %{name}-ic
%defattr(-,root,root)
%{erlang_libdir}/ic-%{ic_version}

%files -n %{name}-inets
%defattr(-,root,root)
%{erlang_libdir}/inets-%{inets_version}

%files -n %{name}-inviso
%defattr(-,root,root)
%{erlang_libdir}/inviso-%{inviso_version}

%if %build_java
%files -n %{name}-jinterface
%defattr(-,root,root)
%{erlang_libdir}/jinterface-%{jinterface_version}/priv/OtpErlang.jar
%{erlang_libdir}/jinterface-%{jinterface_version}/java_src/com/ericsson/otp/erlang/*
%endif

%files -n %{name}-manpages
%defattr(-,root,root)
%{_mandir}/*
%exclude %{_datadir}/COPYRIGHT
%exclude %{_datadir}/PR.template
%exclude %{_datadir}/README
         
%files -n %{name}-megaco
%defattr(-,root,root)
%{erlang_libdir}/megaco-%{megaco_version}

%files -n %{name}-mnesia
%defattr(-,root,root)
%{erlang_libdir}/mnesia-%{mnesia_version}

%files -n %{name}-observer
%defattr(-,root,root)
%{erlang_libdir}/observer-%{observer_version}

%files -n %{name}-odbc
%defattr(-,root,root)
%{erlang_libdir}/odbc-%{odbc_version}

%files -n %{name}-orber
%defattr(-,root,root)
%{erlang_libdir}/orber-%{orber_version}

%files -n %{name}-os_mon
%defattr(-,root,root)
%{erlang_libdir}/os_mon-%{os_mon_version}

%files -n %{name}-otp_mibs
%defattr(-,root,root)
%{erlang_libdir}/otp_mibs-%{otp_mibs_version}

%files -n %{name}-parsetools
%defattr(-,root,root)
%{erlang_libdir}/parsetools-%{parsetools_version}

%files -n %{name}-percept
%defattr(-,root,root)
%{erlang_libdir}/percept-%{percept_version}

%files -n %{name}-pman
%defattr(-,root,root)
%{erlang_libdir}/pman-%{pman_version}

%files -n %{name}-public_key
%defattr(-,root,root)
%{erlang_libdir}/public_key-%{public_key_version}

%files -n %{name}-runtime_tools
%defattr(-,root,root)
%{erlang_libdir}/runtime_tools-%{runtime_tools_version}

%files -n %{name}-snmp
%defattr(-,root,root)
%{erlang_libdir}/snmp-%{snmp_version}

%files -n %{name}-ssh
%defattr(-,root,root)
%{erlang_libdir}/ssh-%{ssh_version}

%files -n %{name}-ssl
%defattr(-,root,root)
%{erlang_libdir}/ssl-%{ssl_version}

%files -n %{name}-syntax_tools
%defattr(-,root,root)
%{erlang_libdir}/syntax_tools-%{syntax_tools_version}

%files -n %{name}-test_server
%defattr(-,root,root)
%{erlang_libdir}/test_server-%{test_server_version}

%files -n %{name}-toolbar
%defattr(-,root,root)
%{erlang_libdir}/toolbar-%{toolbar_version}

%files -n %{name}-tools
%defattr(-,root,root)
%{erlang_libdir}/tools-%{tools_version}

%files -n %{name}-typer
%defattr(-,root,root)
%{erlang_libdir}/typer-%{typer_version}
%{_libdir}/%{name}/bin/typer

%files -n %{name}-tv
%defattr(-,root,root)
%{erlang_libdir}/tv-%{tv_version}

%files -n %{name}-webtool
%defattr(-,root,root)
%{erlang_libdir}/webtool-%{webtool_version}

%files -n %{name}-xmerl
%defattr(-,root,root)
%{erlang_libdir}/xmerl-%{xmerl_version}
