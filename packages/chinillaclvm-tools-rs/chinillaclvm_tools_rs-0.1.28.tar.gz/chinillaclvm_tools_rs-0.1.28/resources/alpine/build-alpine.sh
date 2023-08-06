#!/bin/sh

. $HOME/.cargo/env
cd /root/chinillaclvm_tools_rs
CC=gcc maturin build --release --strip --compatibility musllinux_1_1 --target x86_64-unknown-linux-musl
