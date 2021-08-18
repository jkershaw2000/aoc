package main

import (
	"fmt"
	"strconv"
	"time"

	"../helpers"
)

func p1(instructions []string) []bool {
	defer helpers.TimeTrack(time.Now())
	pc, acc := 0, 0
	seen := make([]bool, len(instructions)) // All init to false
	for pc < len(instructions) && !(seen[pc]) {
		seen[pc] = true
		cmd := instructions[pc][:3]
		val, _ := strconv.Atoi(instructions[pc][4:])
		pc++
		if cmd == "acc" {
			acc += val
		} else if cmd == "jmp" {
			pc = pc + val - 1
		}
	}
	fmt.Printf("Part 1: %d ", acc)
	return seen
}

func run(instructions []string) (int, int) {
	pc, acc := 0, 0
	seen := make([]bool, len(instructions)) // All init to false
	for pc < len(instructions) && !(seen[pc]) {
		seen[pc] = true
		cmd := instructions[pc][:3]
		val, _ := strconv.Atoi(instructions[pc][4:])
		pc++
		if cmd == "acc" {
			acc += val
		} else if cmd == "jmp" {
			pc = pc + val - 1
		}
	}
	return acc, pc
}

func p2(instructions []string, seen []bool) int {
	defer helpers.TimeTrack(time.Now())
	//var editedInstructions []string
	cmds := []string{"jmp", "nop"}
	swap := map[string]string{"jmp": "nop", "nop": "jmp"}
	var intsrLength int = len(instructions)
	for i, used := range seen {
		// Not good. Should not need to regenerate input. How are values passed into funtions.
		instructions, _ := helpers.GetInputStringByLine("/Users/jack/Documents/Github/aoc-2020/day8/8.in")
		cmd, val := instructions[i][:3], instructions[i][4:]
		if used == true && helpers.Find(cmds, cmd) {
			instructions[i] = swap[cmd] + val
		}
		acc, pc := run(instructions)
		if pc == intsrLength {
			fmt.Printf("Part 2: %d ", acc)
			return acc
		}
	}
	return -1
}

func main() {
	fmt.Println("Day 8: Handheld Halting")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day8/8.in"
	data, err := helpers.GetInputStringByLine(fileName)
	if err != nil {
		panic(err)
	}
	seen := p1(data)
	p2(data, seen)
}
