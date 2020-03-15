import Foundation

struct Drink {
    let title: String
    let alcohol: Float
    var volume: Float
    
    var amountEthanol: Float {
        let totalEthanol = alcohol * volume / 100
        return totalEthanol
    }
}

var currentDrink = Drink(title: "Wine", alcohol: 5, volume: 25)

struct Human {
    let gender: String
    var weight: Float
    var coefficient: Float
    
    var weightCoef: Float {
        let weightAfterCoef = weight * coefficient
        return weightAfterCoef
    }
}

var currentUser = Human(gender: "male", weight: 76, coefficient: 0.7)

if currentUser.gender == "male" {
    currentUser.coefficient = 0.7
}
else if currentUser.gender == "female" {
    currentUser.coefficient = 0.6
}
else {
    print("Please specify your gender")
}

let bloodAlcoholIndex : Float = currentDrink.amountEthanol / currentUser.weightCoef
let bloodAlcoholIndexFormatted = String(format: "%.2f", bloodAlcoholIndex)

var soberTimeDuration : Float = bloodAlcoholIndex * 300
var soberTimeHours : Int = Int(soberTimeDuration) / 60
var soberTimeMinutes : Int = Int(soberTimeDuration) % 60

print("You drunk \(currentDrink.volume) ml of \(currentDrink.title) (amount of ethanol \(currentDrink.amountEthanol) ml)")
print("Now your blood alcohol index is \(bloodAlcoholIndexFormatted) ‰")

if bloodAlcoholIndex > 3.5 {
    print("Great risk of coma or death")
}
else if bloodAlcoholIndex >= 2 && bloodAlcoholIndex <= 3.5 {
    print("Deep sleep")
}
else if bloodAlcoholIndex >= 1 && bloodAlcoholIndex <= 2 {
    print("Difficulty controlling the body, impaired balance and double vision.")
}
else if bloodAlcoholIndex >= 0.4 && bloodAlcoholIndex <= 1 {
    print("Impairment of vision, speech and coordination.")
}
else if bloodAlcoholIndex >= 0.1 && bloodAlcoholIndex <= 0.4 {
    print("Loss of certain inhibitions and overestimation of your own abilities.")
}
else {
    print("You are sober!")
}

if soberTimeMinutes <= 5 {
    print("You can drive now!")
}
else {
    print("You can drive in \(soberTimeHours) h \(soberTimeMinutes) min")
}
