package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"time"

	"../helpers"
)

func getInput(fileName string) ([]string, error) {
	// Split by 2 line so can't use standard method
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(data), "\n\n")
	var contents []string
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		contents = append(contents, string(line))
	}
	return contents, nil
}

func p1(data []string) {
	defer helpers.TimeTrack(time.Now())
	res := 0
	for _, passport := range data {

	}
	fmt.Printf("Part 1: %d ", res)
}

func p2(data []string) {
	defer helpers.TimeTrack(time.Now())
	res := 0
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day N: ")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day4/4.in"
	data, err := getInput(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
