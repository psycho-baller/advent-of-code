package utils

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func ReadHTTP(year, day int) (string, error) {
	url := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day)
	session := fmt.Sprintf("session=%s", os.Getenv("AOC_SESSION"))

	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Add("cookie", session)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	bodyBytes, err := ioutil.ReadAll(resp.Body)

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf(string(bodyBytes))
	}

	return string(bodyBytes), nil
}
