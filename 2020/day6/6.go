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

func removeDuplicates(input string) []string {
	var found []string
	for _, char := range input {
		if !(helpers.Find(found, string(char))) {
			found = append(found, string(char))
		}
	}
	return found
}

func getDuplicates(a, b string) string {
	var found string
	for _, char := range a {
		if strings.Contains(b, string(char)) {
			found = found + string(char)
		}
	}
	return found
}

func p1(data []string) {
	defer helpers.TimeTrack(time.Now())
	var res int
	for _, group := range data {
		contains := removeDuplicates(strings.ReplaceAll(group, "\n", ""))
		res = res + len(contains)
	}
	fmt.Printf("Part 1: %d ", res)
}

func p2(data []string) {
	defer helpers.TimeTrack(time.Now())
	var res int
	var splitData [][]string
	for _, v := range data {
		splitData = append(splitData, strings.Split(v, "\n"))
	}
	for _, group := range splitData {
		ques := "abcdefghijklmnopqrstuvwxyz"
		for _, line := range group {
			ques = getDuplicates(ques, line)
		}
		res = res + len(ques)

	}
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day 6: Custom Customs")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day6/6.in"
	data, err := getInput(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
