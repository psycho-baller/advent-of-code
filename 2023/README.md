# Advent of Code Golang Starter

Decided to use Go for this year's Advent of Code. This is my workflow:

## create a new day

```bash
cp -r template 01 # or whatever day
```

## get the example input and output and place them in main_test.go

## run tests for day 1

```bash
go test aoc/01
```

## run the day 1

```bash
go run aoc/01
```

## Config

If you like read the inputs directly from web, you needs to set the environment
var `AOC_SESSION`. You can to get the session token from the cookie web browser.

Folder structure:

    ├── 01
    │   ├── main.go
    │   └── main_test.go
    ├── template
    │   ├── main.go
    │   └── main_test.go
    └── utils
        ├── read_file.go
        └── read_http.go

```

```
