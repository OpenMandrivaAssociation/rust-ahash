# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate ahash

Name:           rust-ahash
Version:        0.8.11
Release:        1
Summary:        Non-cryptographic hash function using AES-NI for high performance
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ahash
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0~)
BuildRequires:  (crate(getrandom/default) >= 0.2.7 with crate(getrandom/default) < 0.3.0~)
BuildRequires:  (crate(once_cell) >= 1.18.0 with crate(once_cell) < 2.0.0~)
BuildRequires:  (crate(once_cell/alloc) >= 1.18.0 with crate(once_cell/alloc) < 2.0.0~)
BuildRequires:  (crate(version_check/default) >= 0.9.4 with crate(version_check/default) < 0.10.0~)
BuildRequires:  (crate(zerocopy) >= 0.7.31 with crate(zerocopy) < 0.8.0~)
BuildRequires:  (crate(zerocopy/simd) >= 0.7.31 with crate(zerocopy/simd) < 0.8.0~)
BuildRequires:  rust >= 1.60.0
%if %{with check}
BuildRequires:  (crate(criterion/default) >= 0.3.2 with crate(criterion/default) < 0.4.0~)
BuildRequires:  (crate(criterion/html_reports) >= 0.3.2 with crate(criterion/html_reports) < 0.4.0~)
BuildRequires:  (crate(fnv/default) >= 1.0.5 with crate(fnv/default) < 2.0.0~)
BuildRequires:  (crate(fxhash/default) >= 0.2.1 with crate(fxhash/default) < 0.3.0~)
BuildRequires:  (crate(hashbrown/default) >= 0.14.3 with crate(hashbrown/default) < 0.15.0~)
BuildRequires:  (crate(hex/default) >= 0.4.2 with crate(hex/default) < 0.5.0~)
BuildRequires:  (crate(no-panic/default) >= 0.1.10 with crate(no-panic/default) < 0.2.0~)
BuildRequires:  (crate(pcg-mwc/default) >= 0.2.1 with crate(pcg-mwc/default) < 0.3.0~)
BuildRequires:  (crate(rand/default) >= 0.8.5 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(seahash/default) >= 4.0.0 with crate(seahash/default) < 5.0.0~)
BuildRequires:  (crate(serde_json/default) >= 1.0.59 with crate(serde_json/default) < 2.0.0~)
BuildRequires:  (crate(smallvec/default) >= 1.13.1 with crate(smallvec/default) < 2.0.0~)
%endif

%global _description %{expand:
A non-cryptographic hash function using AES-NI for high performance.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash) = 0.8.11
Requires:       (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0~)
Requires:       (crate(once_cell) >= 1.18.0 with crate(once_cell) < 2.0.0~)
Requires:       (crate(once_cell/alloc) >= 1.18.0 with crate(once_cell/alloc) < 2.0.0~)
Requires:       (crate(version_check/default) >= 0.9.4 with crate(version_check/default) < 0.10.0~)
Requires:       (crate(zerocopy) >= 0.7.31 with crate(zerocopy) < 0.8.0~)
Requires:       (crate(zerocopy/simd) >= 0.7.31 with crate(zerocopy/simd) < 0.8.0~)
Requires:       cargo
Requires:       rust >= 1.60.0

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/FAQ.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/default) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11
Requires:       crate(ahash/runtime-rng) = 0.8.11
Requires:       crate(ahash/std) = 0.8.11

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+atomic-polyfill-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/atomic-polyfill) = 0.8.11
Requires:       (crate(atomic-polyfill/default) >= 1.0.1 with crate(atomic-polyfill/default) < 2.0.0~)
Requires:       (crate(once_cell/atomic-polyfill) >= 1.18.0 with crate(once_cell/atomic-polyfill) < 2.0.0~)
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+atomic-polyfill-devel %{_description}

This package contains library source intended for building other packages which
use the "atomic-polyfill" feature of the "%{crate}" crate.

%files       -n %{name}+atomic-polyfill-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compile-time-rng-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/compile-time-rng) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11
Requires:       crate(ahash/const-random) = 0.8.11

%description -n %{name}+compile-time-rng-devel %{_description}

This package contains library source intended for building other packages which
use the "compile-time-rng" feature of the "%{crate}" crate.

%files       -n %{name}+compile-time-rng-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+const-random-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/const-random) = 0.8.11
Requires:       (crate(const-random/default) >= 0.1.17 with crate(const-random/default) < 0.2.0~)
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+const-random-devel %{_description}

This package contains library source intended for building other packages which
use the "const-random" feature of the "%{crate}" crate.

%files       -n %{name}+const-random-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/getrandom) = 0.8.11
Requires:       (crate(getrandom/default) >= 0.2.7 with crate(getrandom/default) < 0.3.0~)
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-arm-aes-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/nightly-arm-aes) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+nightly-arm-aes-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly-arm-aes" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-arm-aes-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no-rng-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/no-rng) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+no-rng-devel %{_description}

This package contains library source intended for building other packages which
use the "no-rng" feature of the "%{crate}" crate.

%files       -n %{name}+no-rng-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+runtime-rng-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/runtime-rng) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11
Requires:       crate(ahash/getrandom) = 0.8.11

%description -n %{name}+runtime-rng-devel %{_description}

This package contains library source intended for building other packages which
use the "runtime-rng" feature of the "%{crate}" crate.

%files       -n %{name}+runtime-rng-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/serde) = 0.8.11
Requires:       (crate(serde/default) >= 1.0.117 with crate(serde/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(ahash/std) = 0.8.11
Requires:       cargo
Requires:       crate(ahash) = 0.8.11

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
