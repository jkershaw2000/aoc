package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func getInput(fileName string) ([]string, error) {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(data), "\n")
	var contents []string
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		contents = append(contents, string(line))
	}
	return contents, nil
}

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

func p1(data []string) int {
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
	return count
}

func p2(data []string) int {
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
	return count
}

func main() {
	fileName := "/Users/jack/Documents/Github/aoc-2020/day2/2.in"
	data, err := getInput(fileName)
	if err != nil {
		panic(err)
	}
	fmt.Println(p1(data))
	fmt.Println(p2(data))
}
