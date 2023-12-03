package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test(t *testing.T) {
	assert := assert.New(t)
	input := `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

	t.Run("part 1", func(t *testing.T) {
		expected := 142
		actual := part1(input)

		assert.Equal(actual, expected)
	})

	t.Run("part 2", func(t *testing.T) {
		expected := 281
		actual := part2(`two1nine
		eightwothree
		abcone2threexyz
		xtwone3four
		4nineeightseven2
		zoneight234
		7pqrstsixteen`)

		assert.Equal(actual, expected)
	})
}
