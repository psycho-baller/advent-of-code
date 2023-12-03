package main

import (
	"fmt"
	"os"
	"time"

	"aoc/utils"
)

func main() {
	// get the day of the month using the current time
	day := time.Now().Day()
	// read from http request
	input, err := utils.ReadHTTP(2023, day)
	if err != nil {
		fmt.Println(err)
		os.Exit(0)
	}

	fmt.Println("--- Part One ---")
	fmt.Println("Result:", part1(input))
	fmt.Println("--- Part Two ---")
	fmt.Println("Result:", part2(input))

	os.Exit(0)
}

// part one
func part1(input string) int {
	return 0
}

// part two
func part2(input string) int {
	return 0
}
