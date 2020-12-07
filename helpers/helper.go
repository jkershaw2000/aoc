package helpers

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

func TimeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Printf("in %s.\n", elapsed)
}

func GetInputStringByLine(fileName string) ([]string, error) {
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

func GetInputIntByLine(fileName string) ([]int, error) {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(data), "\n")
	var nums []int
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		num, err := strconv.Atoi(line)
		if err != nil {
			return nil, err
		}
		nums = append(nums, num)
	}
	return nums, nil
}