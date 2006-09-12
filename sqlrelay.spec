Summary:	Persistent database connection system
Name:		sqlrelay
Version:	0.37.1
Release:	0.4
License:	GPL/LGPL and Others
Group:		Daemons
Source0:	http://dl.sourceforge.net/sqlrelay/%{name}-%{version}.tar.gz
# Source0-md5:	4628782233e548a1436c6149f913fd89
Source1:	%{name}.init
URL:		http://sqlrelay.sourceforge.net
BuildRequires:	mysql-devel
BuildRequires:	php-devel >= 4:5:0
BuildRequires:	python >= 1:2.3
BuildRequires:	rudiments-devel >= 0.28.1
Requires:	readline >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		phpextdir	%(php-config --extension-dir 2>/dev/null)

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

%package devel
Summary:	Development libraries for SQL Relay
Group:		Development/Libraries

%description devel
Static libraries for SQL Relay.

%package clients
Summary:	Command line applications for accessing databases through SQL Relay
Group:		Applications/Databases

%description clients
Command line applications for accessing databases through SQL Relay.

%package client-runtime
Summary:	Runtime libraries for SQL Relay clients
Group:		Libraries

%description client-runtime
Runtime dependencies for SQL Relay clients

%package client-devel
Summary:	Development files for developing programs in C/C++ that use SQL Relay
Group:		Development/Libraries

%description client-devel
Header files and static libraries to use for developing programs in
C/C++ that use SQL Relay.

%package client-mysql
Summary:	Drop in replacement library allowing MySQL clients to use SQL Relay instead
Group:		Libraries

%description client-mysql
Drop in replacement library allowing MySQL clients to use SQL Relay
instead.

%package mysql
Summary:	SQL Relay connection daemon for MySQL
Group:		Applications/Databases

%description mysql
SQL Relay connection daemon for MySQL.

%package perl
Summary:	SQL Relay modules for Perl
Group:		Development/Languages

%description perl
SQL Relay modules for Perl.

%package php
Summary:	SQL Relay modules for PHP
Group:		Development/Languages

%description php
SQL Relay modules for PHP.

%package python
Summary:	SQL Relay modules for Python
Group:		Development/Languages

%description python
SQL Relay modules for Python.

%prep
%setup -q

%build
%configure \
	--disable-gtk \
	--disable-db2 \
	--disable-freetds \
	--disable-interbase \
	--disable-lago \
	--disable-mdbtools \
	--disable-msql \
	--disable-odbc \
	--disable-oracle \
	--disable-postgresql \
	--disable-sqlite \
	--disable-sybase \
	--disable-java \
	--disable-tcl \
	--disable-ruby \
	--disable-zope
	--enable-python \
	--enable-mysql \
	--enable-php \
	--enable-perl \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sqlrelay
mv $RPM_BUILD_ROOT%{_sysconfdir}/sqlrelay.conf{.example,}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}
%config %attr(600,root,root) %{_sysconfdir}/sqlrelay.conf
%config %attr(600,root,root) %{_sysconfdir}/sqlrelay.dtd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/sqlrelay
%attr(754,root,root) /etc/rc.d/init.d/sqlrelay
%attr(755,root,root) %{_bindir}/sqlr-cachemanager*
%attr(755,root,root) %{_bindir}/sqlr-listener*
%attr(755,root,root) %{_bindir}/sqlr-scaler*
%attr(755,root,root) %{_bindir}/sqlr-start*
%attr(755,root,root) %{_bindir}/sqlr-stop
%{_libdir}/libsqlrconnection*
%attr(755,root,root) %{_libdir}/libpqsqlrelay-*.*.*.so.1.0.0
%{_libdir}/libsqlrutil*
/var/sqlrelay/tmp
/var/sqlrelay/debug
%{_mandir}/man1/fields.1*
%{_mandir}/man1/query.py.1*
%{_mandir}/man1/sqlr-config-gtk.1*
%{_mandir}/man8/sqlr-cachemanager.8*
%{_mandir}/man8/sqlr-connection.8*
%{_mandir}/man8/sqlr-ipclean.8*
%{_mandir}/man8/sqlr-listener.8*
%{_mandir}/man8/sqlr-scaler.8*
%{_mandir}/man8/sqlr-start.8*
%{_mandir}/man8/sqlr-stop.8*

%files devel
%defattr(644,root,root,755)
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
%attr(755,root,root) %{_libdir}/libsqlrclient-*.so.*
/var/sqlrelay/cache
%attr(755,root,root) %{_libdir}/libsqlrclientwrapper-*.so.*

%files client-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlrclient-config
%{_includedir}/sqlrelay/sqlrclient.h
%{_includedir}/sqlrelay/private
%{_libdir}/libsqlrclient.a
%{_libdir}/libsqlrclient.la
%{_libdir}/libsqlrclient.so
%{_pkgconfigdir}/sqlrelay-c++.pc
%attr(755,root,root) %{_bindir}/sqlrclientwrapper-config
%{_includedir}/sqlrelay/sqlrclientwrapper.h
%{_libdir}/libsqlrclientwrapper.a
%{_libdir}/libsqlrclientwrapper.la
%{_libdir}/libsqlrclientwrapper.so
%{_pkgconfigdir}/sqlrelay-c.pc

%files client-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmysql*sqlrelay-*.so.*
%{_libdir}/libmysql*sqlrelay.so
%{_libdir}/libmysql*sqlrelay.a
%{_libdir}/libmysql*sqlrelay.la

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlr-connection-mysql*

%files perl
%defattr(644,root,root,755)
%{perl_sitelib}/DBD/SQLRelay.pm
%{perl_sitearch}/auto/DBD/SQLRelay
%{perl_sitearch}/SQLRelay/Connection.pm
%{perl_sitearch}/SQLRelay/Cursor.pm
%{perl_sitearch}/auto/SQLRelay/Connection
%{perl_sitearch}/auto/SQLRelay/Cursor
%{_mandir}/man3/DBD::SQLRelay.3pm*
%{_mandir}/man3/SQLRelay::Connection.3pm*
%{_mandir}/man3/SQLRelay::Cursor.3pm*

%files php
%defattr(644,root,root,755)
%attr(755,root,root) %{phpextdir}/sql_relay.so
%{php_pear_dir}/DB/sqlrelay.php

%files python
%defattr(644,root,root,755)
%dir %{py_sitedir}/SQLRelay
%attr(755,root,root) %{py_sitedir}/SQLRelay/CSQLRelay.so
%{py_sitedir}/SQLRelay/PySQLRClient.py
%{py_sitedir}/SQLRelay/PySQLRDB.py
%{py_sitedir}/SQLRelay/__init__.py
