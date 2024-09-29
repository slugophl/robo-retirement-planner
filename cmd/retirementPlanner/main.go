package main

import "fmt"

func main() {
	var spouseIncome float64
	for {

		fmt.Println("Welcome to retirement planning advisor, please listen to the following prompts.")
		age := getValue("Please enter your age: ")
		currentIncome := getValue("What is your current income?: ")
		ageToRetire := getValue("At what age do you want to retire?: ")
		marritalStatus := getBoolValue("Are you married? Please enter y or n: ")
		spouseWorking := getBoolValue("Is your spouse working? Please enter y or n: ")
		if spouseWorking {
			spouseIncome = getValue("Please enter your spouse's income: ")
		}
		numOfKids := getKids("How many kids do you have or are you planning to have?: ")
		retirementTargetAmount := getValue("What is the target value you want for your savings?: ")
		houseOwnership := getBoolValue("Do you own a house or plan to buy one? Please enter y or n: ")

		fmt.Printf(
			"Your age is %.2f\nYour current income is %.2f\nYour target retirement age is %.2f\nYour marital status is %t\nIs your spouse working? %t\nYour spouse's income is %.2f\nNumber of kids: %.2f\nYour target retirement amount is %.2f\nDo you own a house?: %t\n",
			age, currentIncome, ageToRetire, marritalStatus, spouseWorking, spouseIncome, numOfKids, retirementTargetAmount, houseOwnership)
		return
	}
}

func getValue(text string) float64 {
	for {
		var userInput float64
		fmt.Print(text)
		fmt.Scan(&userInput)
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
		fmt.Scan(&userInput)
		if userInput == "y" || userInput == "Y" {
			return true
		} else if userInput == "n" || userInput == "N" {
			return false
		} else {
			fmt.Println("Please enter either y for yes, or n for no")
			continue
		}
	}
}

func getKids(text string) float64 {
	for {
		var userInput float64
		fmt.Print(text)
		fmt.Scan(&userInput)
		if userInput < 0 || userInput > 50 {
			fmt.Println("Please enter a positive number that is less than 50 or greater than 0.")
			continue
		} else {
			return userInput
		}
	}
}
