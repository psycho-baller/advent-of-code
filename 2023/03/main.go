package main

import (
	"fmt"
	"os"
	"time"
	"strconv"

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

func isSpecialChar(char string) bool {
	return char != "." && !utils.IsNumber(char)
}

// part one
func part1(input string) int {
	numbers := make(map[string][][3]int)
	sumOfPartNumbers := 0
	lines := utils.SplitLines(input)
	
	for i, line := range lines {
		currentNumber := ""
		startIndex := 0
		for j, char := range line {
			if char >= '0' && char <= '9' {
				if currentNumber == "" {
					startIndex = j
				}
				currentNumber += string(char)
			} else {
				if currentNumber != "" {
					numbers[currentNumber] = append(numbers[currentNumber], [3]int{i, startIndex, j - 1})
					currentNumber = ""
				}
			}
		}
		// Add the last number in the line if it exists
		if currentNumber != "" {
				numbers[currentNumber] = append(numbers[currentNumber], [3]int{i, startIndex, len(line) - 1})
		}
	}

	// loop through the map
	for number, positions := range numbers {
		partNumber, err := strconv.Atoi(number)
		if err != nil {
			fmt.Println(err)
			os.Exit(0)
		}
		// loop through the positions
		for _, position := range positions {
			lineNumber := position[0]
			startIndex := position[1]
			endIndex := position[2]
			// check if the charachers to the left and right are dots, if so, add the part number to the sum then continue
			prevIndex := startIndex - 1
			nextIndex := endIndex + 1
			// check if the characters to the left are dots
			if prevIndex >= 0 {
				if lineNumber > 0 && isSpecialChar(string(lines[lineNumber - 1][prevIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
				if isSpecialChar(string(lines[lineNumber][prevIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
				if lineNumber < len(lines) - 1 && isSpecialChar(string(lines[lineNumber + 1][prevIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
			}
			// check if the characters to the right are dots
			if nextIndex < len(lines[lineNumber]) {
				if lineNumber > 0 && isSpecialChar(string(lines[lineNumber - 1][nextIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
				if isSpecialChar(string(lines[lineNumber][nextIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
				if lineNumber < len(lines) - 1 && isSpecialChar(string(lines[lineNumber + 1][nextIndex])) {
					sumOfPartNumbers += partNumber
					continue
				}
			}
			// check if the characters above and below are dots
			for i := startIndex; i <= endIndex; i++ {
				lineAbove := lineNumber - 1
				lineBelow := lineNumber + 1
				// check if the character above is a dot
				if lineAbove >= 0 && isSpecialChar(string(lines[lineAbove][i])) {
					sumOfPartNumbers += partNumber
					continue
				}
				// check if the character below is a dot
				if lineBelow < len(lines) && isSpecialChar(string(lines[lineBelow][i])) {
					sumOfPartNumbers += partNumber
					continue
				}
			}
		}
	}

	return sumOfPartNumbers
}

// part two
func part2(input string) int {
	return 0
}
