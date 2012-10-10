#!/usr/bin/env bash

mkdir -p generated
parallel -j6 python {0} ::: *.py
