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

var currentDrink = Drink(title: "Wine", alcohol: 12, volume: 375)
currentDrink.amountEthanol

struct Human {
    let gender: String
    let weight: Float
    let coefficient: Float
    
    var weightCoef: Float {
        let weightAfterCoef = weight * coefficient
        return weightAfterCoef
    }
}

let currentUser = Human(gender: "male", weight: 76, coefficient: 0.7)
currentUser.weightCoef

let bloodAlcoholIndex : Float = currentDrink.amountEthanol / currentUser.weightCoef
let bloodAlcoholIndexFormatted = String(format: "%.2f", bloodAlcoholIndex)

var soberTimeDuration : Float = bloodAlcoholIndex * 300
var soberTimeHours : Int = Int(soberTimeDuration) / 60
var soberTimeMinutes : Int = Int(soberTimeDuration) % 60

print("You drunk \(currentDrink.volume) ml of \(currentDrink.title) (amount of ethanol \(currentDrink.amountEthanol) ml)")
print("Now your blood alcohol index is \(bloodAlcoholIndexFormatted) ‰")
print("You can drive in \(soberTimeHours) h \(soberTimeMinutes) min")
