package main

import (
	"fmt"
	"os"

	"aoc/utils"
	"strconv"
	"strings"
)

func main() {
	// read from http request
	input, err := utils.ReadHTTP(2023, 1)
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

func isNumber(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}
// part one
func part1(input string) int {
	counter := 0
	// loop through input
	for _, line := range utils.SplitLines(input) {
		firstNumber := ""
		lastNumber := ""
		// while the first or last characters are nil, keep removing from both sides until they are not
		for firstNumber == "" || lastNumber == "" {
			if len(line) == 0 {
				break
			} else if len(line) == 1 {
				firstNumber = string(line[0])
				lastNumber = string(line[0])
				break
			}
			if isNumber(string(line[0])) {
				firstNumber = string(line[0])
			} else {
				line = line[1:]
			}
			if isNumber(string(line[len(line)-1])) {
				lastNumber = string(line[len(line)-1])
			} else {
				line = line[:len(line)-1]
			}
		}
		// concatenate the first and last numbers to make a new number
		newNumber, _ := strconv.Atoi(firstNumber + lastNumber)
		counter += newNumber
	}
	return counter
}

// part two
func part2(input string) int {
	counter := 0
	// replace string text of numbers with the number itself
	input = strings.ReplaceAll(input, "one", "one1one")
	input = strings.ReplaceAll(input, "two", "two2two")
	input = strings.ReplaceAll(input, "three", "three3three")
	input = strings.ReplaceAll(input, "four", "four4four")
	input = strings.ReplaceAll(input, "five", "five5five")
	input = strings.ReplaceAll(input, "six", "six6six")
	input = strings.ReplaceAll(input, "seven", "seven7seven")
	input = strings.ReplaceAll(input, "eight", "eight8eight")
	input = strings.ReplaceAll(input, "nine", "nine9nine")
	// loop through input
	for _, line := range utils.SplitLines(input) {

		firstNumber := ""
		lastNumber := ""
		// while the first or last characters are nil, keep removing from both sides until they are not
		for firstNumber == "" || lastNumber == "" {
			if len(line) == 0 {
				break
			} else if len(line) == 1 {
				firstNumber = string(line[0])
				lastNumber = string(line[0])
			} else {
				if isNumber(string(line[0])) {
					firstNumber = string(line[0])
				} else {
					line = line[1:]
				}
				if isNumber(string(line[len(line)-1])) {
					lastNumber = string(line[len(line)-1])
				} else {
					line = line[:len(line)-1]
				}
			}
		}
		// concatenate the first and last numbers to make a new number
		newNumber, _ := strconv.Atoi(firstNumber + lastNumber)
		counter += newNumber
	}
	return counter
}
