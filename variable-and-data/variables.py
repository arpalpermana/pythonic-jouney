# All about Variables

govTax = 0.11  # How to initiate new variable ( no need to var or let )

inputNumber = int(
    input("How much you pay: ")
)  # takes an input from user, and cast it as integer

totalAmount = inputNumber + (
    govTax * inputNumber
)  # basic arithmatic operator (+ - / *)

print(
    f"You're paying : {inputNumber} \nbut the gov takes 11% on it, so it will be: {inputNumber+(inputNumber*govTax)}"
)  # as it named, print. wtf did you expected
