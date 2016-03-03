#Dyce
Building the UDice System in Python for the Python Study Group

## What is the UDice System?
The UDice System is an abstract dice roller system that supports (almost?) any dice system from any game. There are 2 large abstractions that exist within the system: the Die model and the Rollers.

### The Die Model
The Die model is many-layered, beginning at the top with the `Die` itself, drilling down to the `Unit`.

##### Die
A `Die`, as in real life is really just the sum of its `Face`s. It also needs some form of identification, which will be a name in this system. When a `Die` is rolled, it returns a `Roll`, which provides all the necessary information about what was rolled, such as which `Die` it was rolled from and the `Face` it landed on. It also provides "shortcuts" to the data on the `Face`.

##### Face
A `Face` is a collection of `FaceValue`s. Many might think that it pretty much stops there; A die's face just has a number on it, right? Wrong. That may be the case for most dice, but it's not universally true, and this is a *universal* dice-rolling system. So, a `Face` has 0 (a blank face) or more `FaceValue`s, none of which can have the same `Unit`. Each `Face` will have a local identifier that is just its index within the collection of `Faces` on the `Die`.

##### FaceValue
A `FaceValue` is a simple combination of a numeric value (at this point, it is assumed to be an integer since I haven't seen a system yet that uses decimal amounts) and the `Unit` that it applies to.

##### Unit
Lastly, a `Unit` is just like a unit of measure, in that it clarifies what a value of it means. It does this through its primary method of transforming a value into its corresponding output. In a success-based system, the "success" `Unit` would turn a 0 or lower into `"Failure"`, a 1 into `"1 Success"`, and any other positive *n* into`"n Successes"`.

Most `Unit`s work like this, providing different outputs for certain ranges of values, so a specific `RangedUnit` class will be created, with its nested element `OutputRange`. This is not important at this time.

### The Roller Model
The Roller model consists of a Composite Pattern of `Roller`s.

`Roller`s nest within each other to provide sort of a syntax tree of what to do with `Roll`s and `Result`s, which are what `Roller`s wrap `Roll`s in. Each `Result` type is tailored to the `Roller` it came from. For instance, a specific `Roller` might roll twice and choose the better of the two. In that case, the `Result` will keep both `Roll`s but only use the results of the better one for the final "score". This is so that the final output can show both rolls.
