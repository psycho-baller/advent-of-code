package utils

import "strings"

func SplitLines(input string) []string {
	return strings.Split(strings.TrimSpace(input), "\n")
}