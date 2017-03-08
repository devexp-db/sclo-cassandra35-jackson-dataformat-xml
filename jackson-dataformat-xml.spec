%{?scl:%scl_package jackson-dataformat-xml}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jackson-dataformat-xml
Version:	2.7.6
Release:	4%{?dist}
Summary:	XML data binding extension for Jackson
License:	ASL 2.0
URL:		http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Source0:	https://github.com/FasterXML/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix}jackson-parent
BuildRequires:	%{?scl_prefix}jackson-annotations
BuildRequires:	%{?scl_prefix}jackson-core
BuildRequires:	%{?scl_prefix}jackson-databind
BuildRequires:	%{?scl_prefix}jackson-module-jaxb-annotations
BuildRequires:	%{?scl_prefix_maven}woodstox-core
BuildRequires:	%{?scl_prefix}replacer
BuildRequires:	%{?scl_prefix_java_common}bea-stax-api
BuildRequires:	%{?scl_prefix_java_common}junit
BuildRequires:	%{?scl_prefix_maven}stax2-api
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}maven-plugin-build-helper
BuildRequires:	%{?scl_prefix}fasterxml-oss-parent
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Data format extension for Jackson (http://jackson.codehaus.org)
to offer alternative support for serializing POJOs as XML and
deserializing XML as POJOs. Support implemented on top of Stax API
(javax.xml.stream), by implementing core Jackson Streaming API types
like JsonGenerator, JsonParser and JsonFactory. Some data-binding types
overridden as well (ObjectMapper sub-classed as XmlMapper).

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# change woodstox-core dependency version for scl package
%{?scl:%pom_change_dep :woodstox-core: org.codehaus.woodstox:woodstox-core-asl:4.1.2}

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# see https://github.com/FasterXML/jackson-jaxrs-providers/issues/20
%mvn_build -- -Dmaven.test.failure.ignore=true
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Mar 08 2017 Tomas Repik <trepik@redhat.com> - 2.7.6-4
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 2.7.6-2
- Remove BR on site-plugin and enforcer-plugin

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 2.7.6-1
- update to 2.7.6

* Fri Jun 24 2016 gil cattaneo <puntogil@libero.it> 2.6.7-1
- update to 2.6.7

* Thu May 26 2016 gil cattaneo <puntogil@libero.it> 2.6.6-1
- update to 2.6.6

* Thu May 05 2016 gil cattaneo <puntogil@libero.it> 2.6.3-3
- fix for CVE-2016-3720 (rhbz#1332727,1328427)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 gil cattaneo <puntogil@libero.it> 2.6.3-1
- update to 2.6.3

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5.0-1
- update to 2.5.0

* Sat Sep 20 2014 gil cattaneo <puntogil@libero.it> 2.4.2-1
- update to 2.4.2

* Fri Jul 04 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- update to 2.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Sep 07 2013 gil cattaneo <puntogil@libero.it> 2.2.2-3
- remove sub-package doc

* Thu Aug 15 2013 gil cattaneo <puntogil@libero.it> 2.2.2-2
- add sub-package doc

* Wed Jul 17 2013 gil cattaneo <puntogil@libero.it> 2.2.2-1
- initial rpm
