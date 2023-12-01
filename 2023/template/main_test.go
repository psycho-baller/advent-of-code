package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test(t *testing.T) {
	assert := assert.New(t)
	input := `` // edit this

	t.Run("part 1", func(t *testing.T) {
		expected := 0 // edit this
		actual := part1(input)

		assert.Equal(actual, expected)
	})

	t.Run("part 2", func(t *testing.T) {
		expected := 0 // edit this
		actual := part2(input)

		assert.Equal(actual, expected)
	})
}
