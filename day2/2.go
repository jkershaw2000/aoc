package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"../helpers"
)

func getPolicy(password string) (string, []string, string) {
	pass := strings.Split(password, " ")
	passRange := strings.Split(pass[0], "-")
	char := pass[1][0]
	passString := pass[2]
	return string(char), passRange, string(passString)
}

func xor(a bool, b bool) bool {
	return (a || b) && !(a && b)
}

func p1(data []string) {
	defer helpers.TimeTrack(time.Now())
	count := 0
	for _, password := range data {
		char, passRange, passString := getPolicy(password)
		occurences := strings.Count(passString, char)
		low, _ := strconv.Atoi(passRange[0])
		high, _ := strconv.Atoi(passRange[1])
		if low <= occurences && high >= occurences {
			count++
		}
	}
	fmt.Printf("Part 1: %d ", count)
}

func p2(data []string) {
	defer helpers.TimeTrack(time.Now())
	count := 0
	for _, password := range data {
		char, passRange, passString := getPolicy(password)
		low, _ := strconv.Atoi(passRange[0])
		high, _ := strconv.Atoi(passRange[1])
		a := string(passString[low-1]) == char
		b := string(passString[high-1]) == char
		if xor(a, b) {
			count++
		}
	}
	fmt.Printf("Part 1: %d ", count)
}

func main() {
	fmt.Println("Day 2: Password Philosophy")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day2/2.in"
	data, err := helpers.GetInputStringByLine(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
