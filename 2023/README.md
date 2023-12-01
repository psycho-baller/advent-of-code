# Advent of Code Golang Starter

Decided to use Go for this year's Advent of Code. This is a starter template

## Usage

    # run tests for day01
    $ go test aoc/cmd/day01

    # run the day01
    $ go run aoc/cmd/day01

## Config

If you like read the inputs directly from web, you needs to set the environment
var `AOC_SESSION`. You can to get the session token from the cookie web browser.

Folder structure:

    ├── 01
    │   ├── main.go
    │   └── mian_test.go
    ├── template
    │   ├── main.go
    │   └── main_test.go
    └── utils
        ├── read_file.go
        └── read_http.go
