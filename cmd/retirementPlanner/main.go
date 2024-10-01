package main

import (
	"fmt"
	"os"
)

func main() {

	var spouseWorking bool
	var spouseIncome float64

	file, err := os.Create("FIN6776_team_6_retirement_plan.txt")
	if err != nil {
		fmt.Println("Error creating the file:", err)
		return
	}
	defer file.Close()

	for {

		fmt.Println("Welcome to retirement planning advisor, please listen to the following prompts.")
		age := getValue("Please enter your age: ")
		currentIncome := getValue("What is your current income?: ")
		ageToRetire := getRetirementAge("At what age do you want to retire?: ", age)
		marritalStatus := getBoolValue("Are you married? Please enter y or n: ")
		if marritalStatus {
			spouseWorking = getBoolValue("Is your spouse working? Please enter y or n: ")
			if spouseWorking {
				spouseIncome = getValue("Please enter your spouse's income: ")
			}
		}
		numOfKids := getKids("How many kids do you have or are you planning to have?: ")
		retirementTargetAmount := getValue("What is the target value you want for your savings?: ")
		houseOwnership := getBoolValue("Do you own a house or plan to buy one? Please enter y or n: ")

		fmt.Fprintf(file,
			"Your age is %.0f\nYour current income is $%.2f\nYour target retirement age is %.0f\nYour marital status is %t\nIs your spouse working? %t\nYour spouse's income is $%.2f\nNumber of kids: %.0f\nYour target retirement amount is %.2f\nDo you own a house?: %t\n",
			age, currentIncome, ageToRetire, marritalStatus, spouseWorking, spouseIncome, numOfKids, retirementTargetAmount, houseOwnership)
		return
	}
}

func getValue(text string) float64 {
	for {
		var userInput float64
		fmt.Print(text)
		_, err := fmt.Scanln(&userInput)
		if err != nil {
			fmt.Println("Please enter a positive number that is greater than 0.")
			continue
		}
		if userInput > 0 {
			return userInput
		} else {
			fmt.Println("Enter a value greater than 0")
			continue
		}
	}
}

func getBoolValue(text string) bool {
	for {
		var userInput string
		fmt.Print(text)
		_, err := fmt.Scanln(&userInput)
		if err != nil {
			fmt.Println("Please enter either y for yes, or n for no")
			continue
		}
		if userInput == "y" || userInput == "Y" {
			return true
		} else if userInput == "n" || userInput == "N" {
			return false
		}
	}
}

func getKids(text string) float64 {
	for {
		var userInput float64
		fmt.Print(text)
		_, err := fmt.Scanln(&userInput)
		if err != nil {
			fmt.Println("Please enter a positive number that is less than 26 or greater than 0.")
			continue
		}
		if userInput > 0 || userInput <= 25 {
			return userInput
		} else {
			fmt.Println("Please enter a positive number that is less than 26 or greater than 0.")
			continue

		}
	}
}

func getRetirementAge(text string, age float64) float64 {
	for {
		var userInput float64
		fmt.Print(text)
		_, err := fmt.Scanln(&userInput)
		if err != nil {
			fmt.Printf("Please enter a positive number that is greater than %.0f\n", age)
			continue
		}
		if userInput <= age {
			fmt.Printf("Please enter an age greater than %.0f\n", age)
			continue
		} else {
			return userInput
		}
	}
}
