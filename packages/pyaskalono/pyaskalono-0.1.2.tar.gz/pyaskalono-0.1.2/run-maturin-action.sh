#!/bin/bash
set -e
echo "::group::Install Rust"
which rustup > /dev/null || curl --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain stable
export PATH="$HOME/.cargo/bin:$PATH"
rustup override set stable
rustup component add llvm-tools-preview || true
echo "::endgroup::"
export PATH="$PATH:/opt/python/cp36-cp36m/bin:/opt/python/cp37-cp37m/bin:/opt/python/cp38-cp38/bin:/opt/python/cp39-cp39/bin"
echo "::group::Install maturin"
curl -L https://github.com/PyO3/maturin/releases/download/v0.14.4/maturin-x86_64-unknown-linux-musl.tar.gz | tar -xz -C /usr/local/bin
maturin --version || true
which patchelf > /dev/null || python3 -m pip install patchelf
echo "::endgroup::"
echo "::group::Install Rust target"
if [[ ! -d $(rustc --print target-libdir --target x86_64-unknown-linux-gnu) ]]; then rustup target add x86_64-unknown-linux-gnu; fi
echo "::endgroup::"
maturin publish -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDVlMGI3ZmM2LThhYTQtNDBkYi04NGM0LWIxMGFmMzRmMjljNAACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgwxDa_mm-7ik7w96Wd1uchwLXA-jS7KRCshNFsHjoGws -r pypi -i python3.11 --target x86_64-unknown-linux-gnu