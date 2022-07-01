# this is a basic program that finds out if you have the same name as me.
realAnswer = "max"
secretAnswer = "tyler"

print("FIND OUT IF YOUR NAME IS THE SAME AS MINE!")
print("Please, enter your name: ")

givenName = str(input())
lowerGiven = givenName.lower()

print("...")

if lowerGiven == realAnswer:
    print("Congratulations " + lowerGiven.upper() + ", youre a damn cool cucumber")
if lowerGiven == secretAnswer:
    print("EXTRA EXTRA: IDIOT BOY " + lowerGiven.upper() + " LEARNS HOW TO TYPE! MORE AT 5PM")
if lowerGiven != realAnswer or secretAnswer:
    print("Damn, we have different names " + lowerGiven.upper() + "... Get lost rumpboyt");
