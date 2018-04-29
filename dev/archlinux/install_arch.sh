#!/bin/#!/usr/bin/env bash

# tar.gz of the development folder
tar -zcv \
    --exclude=".git" \
    --exclude="arch" \
    --exclude="__pycache__" \
    -f sysbead.tar.gz ../../../sysbead

#Create of the dev-package fo arch
makepkg

# Install package in arch
yaourt -U ./*.xz

# Remove produced files
rm -rf src pkg *.xz *.gz
