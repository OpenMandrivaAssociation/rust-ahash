# check disabled to avoid circular dependencies
%bcond_with check
%global debug_package %{nil}

%global crate ahash

Name:           rust-%{crate}
Version:        0.7.2
Release:        1%{?dist}
Summary:        Non-cryptographic hash function using AES-NI for high performance

# Upstream license specification: MIT OR Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ahash
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(getrandom/default) >= 0.2.0 with crate(getrandom/default) < 0.3.0)
BuildRequires:  (crate(once_cell/alloc) >= 1.5.2 with crate(once_cell/alloc) < 2.0.0)
BuildRequires:  (crate(once_cell/unstable) >= 1.5.2 with crate(once_cell/unstable) < 2.0.0)
BuildRequires:  (crate(version_check/default) >= 0.9.0 with crate(version_check/default) < 0.10.0)
%if %{with check}
BuildRequires:  (crate(criterion/default) >= 0.3.2 with crate(criterion/default) < 0.4.0)
BuildRequires:  (crate(fnv/default) >= 1.0.5 with crate(fnv/default) < 2.0.0)
BuildRequires:  (crate(fxhash/default) >= 0.2.1 with crate(fxhash/default) < 0.3.0)
BuildRequires:  (crate(hex/default) >= 0.4.2 with crate(hex/default) < 0.5.0)
BuildRequires:  (crate(no-panic/default) >= 0.1.10 with crate(no-panic/default) < 0.2.0)
BuildRequires:  (crate(rand/default) >= 0.7.3 with crate(rand/default) < 0.8.0)
BuildRequires:  (crate(seahash/default) >= 4.0.0 with crate(seahash/default) < 5.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.59 with crate(serde_json/default) < 2.0.0)
%endif
%endif

%global _description %{expand:
Non-cryptographic hash function using AES-NI for high performance.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash) = 0.7.2
Requires:       cargo
Requires:       (crate(getrandom/default) >= 0.2.0 with crate(getrandom/default) < 0.3.0)
Requires:       (crate(once_cell/unstable) >= 1.5.2 with crate(once_cell/unstable) < 2.0.0)
Requires:	(crate(once_cell/alloc) >= 1.5.2 with crate(once_cell/alloc) < 2.0.0)
Requires:       (crate(version_check/default) >= 0.9.0 with crate(version_check/default) < 0.10.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash/default) = 0.7.2
Requires:       cargo
Requires:       crate(ahash) = 0.7.2
Requires:       crate(ahash/std) = 0.7.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compile-time-rng-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash/compile-time-rng) = 0.7.2
Requires:       cargo
Requires:       (crate(const-random/default) >= 0.1.12 with crate(const-random/default) < 0.2.0)
Requires:       (crate(const-random/default) >= 0.1.12 with crate(const-random/default) < 0.2.0)
Requires:       crate(ahash) = 0.7.2

%description -n %{name}+compile-time-rng-devel %{_description}

This package contains library source intended for building other packages
which use "compile-time-rng" feature of "%{crate}" crate.

%files       -n %{name}+compile-time-rng-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+const-random-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash/const-random) = 0.7.2
Requires:       cargo
Requires:       (crate(const-random/default) >= 0.1.12 with crate(const-random/default) < 0.2.0)
Requires:       (crate(const-random/default) >= 0.1.12 with crate(const-random/default) < 0.2.0)
Requires:       crate(ahash) = 0.7.2

%description -n %{name}+const-random-devel %{_description}

This package contains library source intended for building other packages
which use "const-random" feature of "%{crate}" crate.

%files       -n %{name}+const-random-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash/serde) = 0.7.2
Requires:       cargo
Requires:       (crate(serde/default) >= 1.0.117 with crate(serde/default) < 2.0.0)
Requires:       (crate(serde/default) >= 1.0.117 with crate(serde/default) < 2.0.0)
Requires:       crate(ahash) = 0.7.2

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ahash/std) = 0.7.2
Requires:       cargo
Requires:       crate(ahash) = 0.7.2

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
