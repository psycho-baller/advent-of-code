package main

import (
	"fmt"
	"os"

	"aoc/utils"
)

func main() {
	// read from http request
	// session := os.Getenv("AOC_SESSION")
	input, err := utils.ReadHTTP(2023, 1)
	if err != nil {
		fmt.Println(err)
		os.Exit(0)
	}

	example_input := ``
	fmt.Println("--- Part One ---")
	fmt.Println("Result:", part1(input, example_input))
	fmt.Println("--- Part Two ---")
	fmt.Println("Result:", part2(input, example_input))

	os.Exit(0)
}

// part one
func part1(input string, example string) int {
	fmt.Println(input)
	return 0
}

// part two
func part2(input string, example string) int {
	return 0
}

