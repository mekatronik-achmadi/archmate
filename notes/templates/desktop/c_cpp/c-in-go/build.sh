#!/bin/bash

# note: cgo using comment as hint

# install module first
#go env -w GO111MODULE=off

export CGO_CPPFLAGS="-I /usr/include"
export CGO_LDFLAGS="-L /usr/lib -lm"

go build main.go

