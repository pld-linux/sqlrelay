#
# Conditional build:
%bcond_without	gtk		# GTK+ frontend
# Database options:
# ================
%bcond_with	db2		# DB2 connection
%bcond_with	freetds		# FreeTDS connection
%bcond_with	interbase	# Interbase connection
%bcond_with	mdbtools	# MDB Tools connection
%bcond_with	msql		# mSQL connection
%bcond_without	mysql		# MySQL connection
%bcond_with	odbc		# ODBC connection
%bcond_with	oracle		# Oracle connection
%bcond_with	postgresql	# PostgreSQL connection
%bcond_with	sqlite		# SQLite connection
%bcond_with	sybase		# Sybase connection
#
# Language options:
# ================
%bcond_with	java		# Java API
%bcond_without	perl		# Perl API
%bcond_without	php		# PHP API
%bcond_without	python		# Python API
%bcond_without	ruby		# Ruby API
%bcond_with	tcl		# Tcl API
%bcond_with	zope		# Zope API
#
Summary:	Persistent database connection system
Summary(pl.UTF-8):	System stałego połączenia z bazą danych
Name:		sqlrelay
Version:	0.38
Release:	0.1
License:	GPL/LGPL and Others
Group:		Daemons
Source0:	http://dl.sourceforge.net/sqlrelay/%{name}-%{version}.tar.gz
# Source0-md5:	93ce290a7f17b9e06e65c41fa47a2724
Source1:	%{name}.init
Source2:	%{name}.conf
Patch1:		%{name}-ac.patch
Patch2:		%{name}-defaults.patch
Patch3:		%{name}-reuseaddr.patch
URL:		http://sqlrelay.sourceforge.net
BuildRequires:	autoconf
%{?with_gtk:BuildRequires:	gtk+-devel}
BuildRequires:	libtool
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	ncurses-devel
%{?with_php:BuildRequires:	php-devel >= 4:5:0}
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	readline-devel >= 4.1
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	rudiments-devel >= 0.28.1
%{?with_tcl:BuildRequires:	tcl-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-client-runtime = %{version}-%{release}
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		phpextdir	%(php-config --extension-dir 2>/dev/null)
%define		_localstatedir	/var/lib
%define		_sysconfdir		/etc/%{name}

%description
SQL Relay is a persistent database connection pooling, proxying and
load balancing system for Unix and Linux supporting ODBC, Oracle,
MySQL, mSQL, PostgreSQL, Sybase, MS SQL Server, IBM DB2, Interbase,
Lago and SQLite with C, C++, Perl, Perl-DBD, Python, Python-DB, Zope,
PHP, Ruby, Java and TCL APIs, command line clients, a GUI
configuration tool and extensive documentation. The APIs support
advanced database operations such as bind variables, multi-row
fetches, client side result set caching and suspended transactions. It
is ideal for speeding up database-driven web-based applications,
accessing databases from unsupported platforms, migrating between
databases, distributing access to replicated databases and throttling
database access.

%description -l pl.UTF-8
SQL Relay to system utrzymywania, przekazywania i równoważenia
obciążenia stałego połączenia z bazą danych dla Uniksa i Linuksa z
obsługą baz danych ODBC, Oracle, MySQL, mSQL, PostgreSQL, Sybase, MS
SQL Server, IBM DB2, Interbase, Lago i SQLite oraz API C, C++, Perla,
Perl-DBD, Pythona, Python-DB, Zope, PHP, Ruby'ego, Javy i Tcl-a.
Zawiera także klientów działających z linii poleceń, graficzne
narzędzie do konfiguracji oraz wyczerpującą dokumentację. API
obsługują zaawansowane operacje na bazach danych, takie jak powiązane
zmienne, pobrania wielowierszowe, buforowanie wyników po stronie
klienta oraz transakcje zawieszone. System ten jest idealny do
przyspieszania aplikacji WWW opartych o bazy danych, dostępu do baz
danych z nieobsługiwanych platform, migracji między bazami danych,
rozpraszania dostępu do zreplikowanych baz danych oraz tłumienia
dostępu do baz danych.

%package devel
Summary:	Development libraries for SQL Relay
Summary(pl.UTF-8):	Biblioteki programistyczne dla SQL Relay
Group:		Development/Libraries
Requires:	%{name}-client-devel = %{version}-%{release}

%description devel
Static libraries for SQL Relay.

%description devel -l pl.UTF-8
Statyczne biblioteki SQL Relay.

%package clients
Summary:	Command line applications for accessing databases through SQL Relay
Summary(pl.UTF-8):	Aplikacje linii poleceń do dostępu do baz danych poprzez SQL Relay
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description clients
Command line applications for accessing databases through SQL Relay.

%description clients -l pl.UTF-8
Aplikacje linii poleceń do dostępu do baz danych poprzez SQL Relay.

%package client-runtime
Summary:	Runtime libraries for SQL Relay clients
Summary(pl.UTF-8):	Biblioteki uruchomieniowe dla klientów SQL Relay
Group:		Libraries
Requires(postun):	/sbin/ldconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd

%description client-runtime
Runtime dependencies for SQL Relay clients.

%description client-runtime -l pl.UTF-8
Biblioteki uruchomieniowe dla klientów SQL Relay.

%package client-devel
Summary:	Development files for developing programs in C/C++ that use SQL Relay
Summary(pl.UTF-8):	Pliki programistyczne do tworzenia programów C/C++ używających SQL Relay
Group:		Development/Libraries
Requires:	%{name}-client-runtime = %{version}-%{release}

%description client-devel
Header files to use for developing programs in C/C++ that use SQL
Relay.

%description client-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów w C/C++ używających SQL Relay.

%package client-static
Summary:	Static libraries for SQL Relay clients
Summary(pl.UTF-8):	Statyczne biblioteki dla klientów SQL Relay
Group:		Development/Libraries
Requires:	%{name}-client-devel = %{version}-%{release}

%description client-static
Static libraries for SQL Relay clients.

%description client-static -l pl.UTF-8
Statyczne biblioteki dla klientów SQL Relay.

%package client-mysql
Summary:	Drop in replacement library allowing MySQL clients to use SQL Relay instead
Summary(pl.UTF-8):	Biblioteka do podmiany pozwalająca klientom MySQL używać SQL Relay
Group:		Libraries
Requires:	%{name}-client-runtime = %{version}-%{release}

%description client-mysql
Drop in replacement library allowing MySQL clients to use SQL Relay
instead.

%description client-mysql -l pl.UTF-8
Biblioteka do podmiany pozwalająca klientom MySQL używać SQL Relay
zamiast bezpośrednio MySQL-a.

%package db2
Summary:	SQL Relay connection daemon for IBM DB2
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla IBM DB2
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description db2
SQL Relay connection daemon for IBM DB2.

%description db2 -l pl.UTF-8
Demon połączenia SQL Relay dla IBM DB2.

%package freetds
Summary:	SQL Relay connection daemon for FreeTDS (Sybase and MS SQL Server)
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla FreeTDS (Sybase i MS SQL Server)
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description freetds
SQL Relay connection daemon for FreeTDS (Sybase and MS SQL Server).

%description freetds -l pl.UTF-8
Demon połączenia SQL Relay dla FreeTDS (Sybase i MS SQL Server).

%package interbase
Summary:	SQL Relay connection daemon for Interbase
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla Interbase
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description interbase
SQL Relay connection daemon for Interbase.

%description interbase -l pl.UTF-8
Demon połączenia SQL Relay dla Interbase.

%package mdbtools
Summary:	SQL Relay connection daemon for MDB Tools (Microsoft Access)
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla MDB Tools (Microsoft Access)
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description mdbtools
SQL Relay connection daemon for MDB Tools (Microsoft Access).

%description mdbtools -l pl.UTF-8
Demon połączenia SQL Relay dla MDB Tools (Microsoft Access).

%package msql
Summary:	SQL Relay connection daemon for mSQL
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla mSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description msql
SQL Relay connection daemon for mSQL.

%description msql -l pl.UTF-8
Demon połączenia SQL Relay dla mSQL-a.

%package mysql
Summary:	SQL Relay connection daemon for MySQL
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla MySQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description mysql
SQL Relay connection daemon for MySQL.

%description mysql -l pl.UTF-8
Demon połączenia SQL Relay dla MySQL-a.

%package odbc
Summary:	SQL Relay connection daemon for ODBC
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla ODBC
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description odbc
SQL Relay connection daemon for ODBC.

%description odbc -l pl.UTF-8
Demon połączenia SQL Relay dla ODBC.

%package oracle7
Summary:	SQL Relay connection daemon for Oracle 7
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla Oracle 7
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description oracle7
SQL Relay connection daemon for Oracle 7.

%description oracle7 -l pl.UTF-8
Demon połączenia SQL Relay dla Oracle 7.

%package oracle8
Summary:	SQL Relay connection daemon for Oracle 8
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla Oracle 8
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description oracle8
SQL Relay connection daemon for Oracle 8.

%description oracle8 -l pl.UTF-8
Demon połączenia SQL Relay dla Oracle 8.

%package postgresql
Summary:	SQL Relay connection daemon for PostgreSQL
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description postgresql
SQL Relay connection daemon for PostgreSQL.

%description postgresql -l pl.UTF-8
Demon połączenia SQL Relay dla PostgreSQL-a.

%package sqlite
Summary:	SQL Relay connection daemon for SQLite
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla SQLite
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description sqlite
SQL Relay connection daemon for SQLite.

%description sqlite -l pl.UTF-8
Demon połączenia SQL Relay dla SQLite.

%package sybase
Summary:	SQL Relay connection daemon for Sybase
Summary(pl.UTF-8):	Demon połączenia SQL Relay dla Sybase
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description sybase
SQL Relay connection daemon for Sybase.

%description sybase -l pl.UTF-8
Demon połączenia SQL Relay dla Sybase.

%package -n perl-DBD-SQLRelay
Summary:	SQL Relay modules for Perl
Summary(pl.UTF-8):	Moduły SQL Relay dla Perla
Group:		Development/Languages
Requires:	%{name}-client-runtime = %{version}-%{release}
Requires:	perl-DBI

%description -n perl-DBD-SQLRelay
SQL Relay modules for Perl.

%description -n perl-DBD-SQLRelay -l pl.UTF-8
Moduły SQL Relay dla Perla.

%package -n php-%{name}
Summary:	SQL Relay modules for PHP
Summary(pl.UTF-8):	Moduły SQL Relay dla PHP
Group:		Development/Languages
Requires:	%{name}-client-runtime = %{version}-%{release}
Requires:	php-pear-DB

%description -n php-%{name}
SQL Relay modules for PHP.

%description -n php-%{name} -l pl.UTF-8
Moduły SQL Relay dla PHP.

%package -n python-%{name}
Summary:	SQL Relay modules for Python
Summary(pl.UTF-8):	Moduły SQL Relay dla Pythona
Group:		Development/Languages
Requires:	%{name}-client-runtime = %{version}-%{release}

%description -n python-%{name}
SQL Relay modules for Python.

%description -n python-%{name} -l pl.UTF-8
Moduły SQL Relay dla Pythona.

%package -n ruby-DBD-SQLRelay
Summary:	SQL Relay modules for Ruby
Summary(pl.UTF-8):	Moduły SQL Relay dla języka Ruby
Group:		Development/Languages
Requires:	%{name}-client-runtime = %{version}-%{release}

%description -n ruby-DBD-SQLRelay
SQL Relay modules for Ruby.

%description -n ruby-DBD-SQLRelay -l pl.UTF-8
Moduły SQL Relay dla języka Ruby.

%package gtk
Summary:	SQL Relay GUI configuration tool
Summary(pl.UTF-8):	Graficzne narzędzie konfiguracyjne dla SQL Relay
Group:		Applications/Databases
Requires:	%{name}-client-runtime = %{version}-%{release}

%description gtk
GTK-based configuration tool for SQL Relay.

%description gtk -l pl.UTF-8
Graficzne narzędzie konfiguracyjne dla SQL Relay.

%package doc
Summary:	Documentation for SQL Relay
Summary(pl.UTF-8):	Dokumentacja dla SQL Relay
Group:		Documentation

%description doc
Documentation for SQL Relay.

%description doc -l pl.UTF-8
Dokumentacja dla SQL Relay.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_db2:--disable-db2} \
	%{!?with_freetds:--disable-freetds} \
	%{!?with_interbase:--disable-interbase} \
	--disable-lago \
	%{!?with_mdbtools:--disable-mdbtools} \
	%{!?with_msql:--disable-msql} \
	%{!?with_odbc:--disable-odbc} \
	%{!?with_oracle:--disable-oracle} \
	%{!?with_postgresql:--disable-postgresql} \
	%{!?with_sqlite:--disable-sqlite} \
	%{!?with_sybase:--disable-sybase} \
	%{!?with_java:--disable-java} \
	%{!?with_tcl:--disable-tcl} \
	%{!?with_ruby:--disable-ruby} \
	%{!?with_zope:--disable-zope} \
	--%{!?with_python:dis}%{?with_python:en}able-python \
%if %{with mysql}
	--enable-mysql \
	--with-mysql-prefix=/usr \
%else
	--disable-mysql \
%endif
%if %{with php}
	--enable-php \
	--with-php-ext-dir=%{phpextdir} \
	--with-pear-db-dir=%{php_pear_dir}/DB \
%else
	--disable-php \
%endif
%if %{with perl}
	--enable-perl \
	--with-perl-site-arch=%{perl_vendorarch} \
	--with-perl-site-lib=%{perl_vendorlib} \
%else
	--disable-perl \
%endif

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/SQLRelay
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/SQLRelay
%py_postclean %{py_sitedir}/SQLRelay

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sqlrelay
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sqlrelay.conf
mv $RPM_BUILD_ROOT{/etc/sysconfig/sqlrelay,%{_sysconfdir}/sqlrelay.instances}
touch $RPM_BUILD_ROOT%{_localstatedir}/sqlrelay/sockseq
install -d $RPM_BUILD_ROOT/var/run/sqlrelay

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/{DBD/SQLRelay,SQLRelay/{Connection,Cursor}}/.packlist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/sqlrelay.conf.example

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add sqlrelay
%service sqlrelay restart

%preun
if [ "$1" = 0 ]; then
	%service sqlrelay stop
	/sbin/chkconfig --del sqlrelay
fi

%postun -p /sbin/ldconfig

%pre client-runtime
%groupadd -g 176 sqlrelay
%useradd -u 176 -c "SQL Relay" -s /bin/false -r -d %{_localstatedir}/sqlrelay -g sqlrelay sqlrelay

%post client-runtime -p /sbin/ldconfig

%postun client-runtime
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%userremove sqlrelay
	%groupremove sqlrelay
fi

%post	client-mysql -p /sbin/ldconfig
%postun	client-mysql -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%{_sysconfdir}/sqlrelay.dtd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,sqlrelay) %{_sysconfdir}/sqlrelay.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sqlrelay.instances
%attr(754,root,root) /etc/rc.d/init.d/sqlrelay
%attr(755,root,root) %{_bindir}/sqlr-cachemanager*
%attr(755,root,root) %{_bindir}/sqlr-listener*
%attr(755,root,root) %{_bindir}/sqlr-scaler*
%attr(755,root,root) %{_bindir}/sqlr-start*
%attr(755,root,root) %{_bindir}/sqlr-stop
%{_libdir}/libsqlrconnection*
# XXX: shouldn't it be -client-postgresql?
%attr(755,root,root) %{_libdir}/libpqsqlrelay-*.*.*.so.1.0.0
%{_libdir}/libsqlrutil*
%attr(775,root,sqlrelay) %{_localstatedir}/sqlrelay/tmp
%attr(775,root,sqlrelay) %{_localstatedir}/sqlrelay/debug
%attr(660,root,sqlrelay) %ghost %{_localstatedir}/sqlrelay/sockseq
%{_mandir}/man1/fields.1*
%{_mandir}/man1/sqlr-config-gtk.1*
%{_mandir}/man8/sqlr-cachemanager.8*
%{_mandir}/man8/sqlr-connection.8*
%{_mandir}/man8/sqlr-ipclean.8*
%{_mandir}/man8/sqlr-listener.8*
%{_mandir}/man8/sqlr-scaler.8*
%{_mandir}/man8/sqlr-start.8*
%{_mandir}/man8/sqlr-stop.8*
%dir %attr(775,root,sqlrelay) /var/run/sqlrelay

%files devel
%defattr(644,root,root,755)
# XXX: headers? separate -static?
# isn't it some PostgreSQL driver?
%attr(755,root,root) %{_libdir}/libpqsqlrelay.so
%{_libdir}/libpqsqlrelay.a
%{_libdir}/libpqsqlrelay.la

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/backupschema
%attr(755,root,root) %{_bindir}/fields
%attr(755,root,root) %{_bindir}/query
%attr(755,root,root) %{_bindir}/sqlr-export
%attr(755,root,root) %{_bindir}/sqlr-import
%attr(755,root,root) %{_bindir}/sqlrsh
%{_mandir}/man1/query.1*
%{_mandir}/man1/sqlrsh.1*

%files client-runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsqlrclient-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libsqlrclientwrapper-*.so.*.*.*
%dir %{_localstatedir}/sqlrelay
%attr(770,root,sqlrelay) %{_localstatedir}/sqlrelay/cache

%files client-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlrclient-config
%attr(755,root,root) %{_bindir}/sqlrclientwrapper-config
%attr(755,root,root) %{_libdir}/libsqlrclient.so
%attr(755,root,root) %{_libdir}/libsqlrclientwrapper.so
%{_libdir}/libsqlrclient.la
%{_libdir}/libsqlrclientwrapper.la
%dir %{_includedir}/sqlrelay
%{_includedir}/sqlrelay/private
%{_includedir}/sqlrelay/sqlrclient.h
%{_includedir}/sqlrelay/sqlrclientwrapper.h
%{_pkgconfigdir}/sqlrelay-c.pc
%{_pkgconfigdir}/sqlrelay-c++.pc

%files client-static
%defattr(644,root,root,755)
%{_libdir}/libsqlrclient.a
%{_libdir}/libsqlrclientwrapper.a

%files client-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmysql*sqlrelay-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libmysql*sqlrelay.so
# XXX: kill or separate -devel, -static?
%{_libdir}/libmysql*sqlrelay.a
%{_libdir}/libmysql*sqlrelay.la

%if %{with db2}
%files db2
%defattr(644,root,root,755)
%endif

%if %{with freetds}
%files freetds
%defattr(644,root,root,755)
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%endif

%if %{with mdbtools}
%files mdbtools
%defattr(644,root,root,755)
%endif

%if %{with msql}
%files msql
%defattr(644,root,root,755)
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlr-connection-mysql*
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%endif

%if %{with oracle}
%files oracle7
%defattr(644,root,root,755)

%files oracle8
%defattr(644,root,root,755)
%endif

%if %{with postgresql}
%files postgresql
%defattr(644,root,root,755)
%endif

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%endif

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%endif

%if %{with perl}
%files -n perl-DBD-SQLRelay
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/SQLRelay
%{perl_vendorarch}/SQLRelay/Connection.pm
%{perl_vendorarch}/SQLRelay/Cursor.pm
%dir %{perl_vendorarch}/auto/SQLRelay/Connection
%{perl_vendorarch}/auto/SQLRelay/Connection/Connection.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SQLRelay/Connection/Connection.so
%dir %{perl_vendorarch}/auto/SQLRelay/Cursor
%{perl_vendorarch}/auto/SQLRelay/Cursor/Cursor.bs
%dir %{perl_vendorarch}/auto/SQLRelay
%dir %{perl_vendorarch}/auto/SQLRelay/Cursor
%attr(755,root,root) %{perl_vendorarch}/auto/SQLRelay/Cursor/Cursor.so
%{perl_vendorlib}/DBD/SQLRelay.pm
%{_mandir}/man3/DBD::SQLRelay.3pm*
%{_mandir}/man3/SQLRelay::Connection.3pm*
%{_mandir}/man3/SQLRelay::Cursor.3pm*
%endif

%if %{with php}
%files -n php-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{phpextdir}/sql_relay.so
%{php_pear_dir}/DB/sqlrelay.php
%endif

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitedir}/SQLRelay
%attr(755,root,root) %{py_sitedir}/SQLRelay/CSQLRelay.so
%{py_sitedir}/SQLRelay/PySQLRClient.py[co]
%{py_sitedir}/SQLRelay/PySQLRDB.py[co]
%{py_sitedir}/SQLRelay/__init__.py[co]
%{_mandir}/man1/query.py.1*
%endif

%if %{with ruby}
%files -n ruby-DBD-SQLRelay
%defattr(644,root,root,755)
%dir %{ruby_sitelibdir}/DBD/SQLRelay
%{ruby_sitelibdir}/DBD/SQLRelay/SQLRelay.rb
%attr(755,root,root) %{ruby_sitearchdir}/sqlrelay.so
%endif

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlr-config-gtk
%endif

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}
