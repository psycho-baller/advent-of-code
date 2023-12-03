package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"

	"aoc/utils"
)

func main() {
	// read from http request
	day := 2
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
	games := utils.SplitLines(input)
	sumOfWinningGameNumbers := 0
	maxRed := 12
	maxGreen := 13
	maxBlue := 14
	fmt.Println(games)
	for i, game := range games {
		// game_num := i + 1
		// split with ":"
		game = strings.Split(game, ": ")[1]
		// split with ";"
		rounds := strings.Split(game, "; ")
		gameIsValid := true
		for _, round := range rounds {
			// split with ","
			var numbersColors []string = strings.Split(round, ", ")
			for _, numberColor := range numbersColors {
				// split with " " to get the number and color
				numberColorTuple := strings.Split(numberColor, " ")
				number, err := strconv.Atoi(numberColorTuple[0])
				if err != nil {
					// handle the error
					fmt.Println(err)
					continue
				}
				color := numberColorTuple[1]
				fmt.Println(number, color)
				// check if the number is greater than the max, if so, the game is invalid
				if (color == "red" && number > maxRed) || (color == "green" && number > maxGreen) || (color == "blue" && number > maxBlue) {
					gameIsValid = false
					break
				}
			}
		}
		if gameIsValid {
			// if all colors have a number less than the max, add the number to the ids
			sumOfWinningGameNumbers += i + 1
		}
	}
	// sum of ids
	return sumOfWinningGameNumbers
}

// part two
func part2(input string) int {
	games := utils.SplitLines(input)
	// var ids []int
	sumOfWinningGameNumbers := 0
	fmt.Println(games)
	for _, game := range games {
		// game_num := i + 1
		// split with ":"
		fmt.Println(game)
		game = strings.Split(game, ": ")[1]
		fmt.Println(game)
		// split with ";"
		rounds := strings.Split(game, "; ")
		maxRed := 0
		maxGreen := 0
		maxBlue := 0
		for _, round := range rounds {
			// split with ","
			var numbersColors []string = strings.Split(round, ", ")
			for _, numberColor := range numbersColors {
				// split with " " to get the number and color
				numberColorTuple := strings.Split(numberColor, " ")
				number, err := strconv.Atoi(numberColorTuple[0])
				if err != nil {
					// handle the error
					fmt.Println(err)
					continue
				}
				color := numberColorTuple[1]
				fmt.Println(number, color)
				// check if the number is greater than the max, if so, then set the max to the number
				if (color == "red" && number > maxRed){
					maxRed = number
				} else if (color == "green" && number > maxGreen) {
					maxGreen = number
				} else if (color == "blue" && number > maxBlue) {
					maxBlue = number
				}
			}
		}
		power := maxRed * maxGreen * maxBlue
		sumOfWinningGameNumbers += power
		//
	}
	// sum of ids
	return sumOfWinningGameNumbers
}
