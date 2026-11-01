import random

total_overlap = 0
total_pure = 0
total_luck = 0
total_mostly = 0

ASTRONAUTS = 18300
TRIALS = 1000

# for these questions i did readability because im taking time to solve this lmao

for _ in range(TRIALS):
    astronauts = []
    for i in range(ASTRONAUTS):
        pureSkillScore = random.uniform(0, 100)
        luckScore = random.uniform(0, 100)
        mostlySkillScore = 0.95 * pureSkillScore + 0.05 * luckScore             # For E, just change the value from 0.95 to 0.99 and 0.05 to 0.01
        astronauts.append((i, pureSkillScore, luckScore, mostlySkillScore))

    pure_astronauts = sorted(astronauts, key=lambda a: a[1])[-11:]
    mostly_astronauts = sorted(astronauts, key=lambda a: a[3])[-11:]

    pure_ids = [a[0] for a in pure_astronauts]
    mostly_ids = [a[0] for a in mostly_astronauts]

    total_overlap += len([i for i in pure_ids if i in mostly_ids])
    total_pure += sum(a[1] for a in pure_astronauts) / 11
    total_luck += sum(a[2] for a in mostly_astronauts) / 11
    total_mostly += sum(a[1] for a in mostly_astronauts) / 11

print(f"a. avg pure skill of pure-skill astronauts: {total_pure / TRIALS:.2f}")
print(f"b. avg percent overlap: {total_overlap / 11 / TRIALS * 100:.2f}%")
print(f"c. avg luck of mostly-skill astronauts: {total_luck / TRIALS:.2f}")
print(f"d. avg pure skill of mostly-skill astronauts: {total_mostly / TRIALS:.2f}")

"""
For Letter E., just change the luck value of 0.05 to 0.01 and pure value of 0.95 to 0.99

Sample Test (for easier comparison):

Run of 0.05 Luck:

a. avg pure skill of pure-skill astronauts: 99.97
b. avg percent overlap: 14.43%
c. avg luck of mostly-skill astronauts: 94.77
d. avg pure skill of mostly-skill astronauts: 99.73

Run of 0.01 Luck:

a. avg pure skill of pure-skill astronauts: 99.97
b. avg percent overlap: 30.61%
c. avg luck of mostly-skill astronauts: 87.94
d. avg pure skill of mostly-skill astronauts: 99.88


Answer to E:
Percent overlap is way higher because luck matters less, which results in lower avg luck of mostly-skill astronauts. However, luck still matters a lot in 
determining the mostly-skill astronauts because the mostly-skill astronauts have high pure-skill in the first place (according to simulation, around 99.88),
meaning that a difference of the luck score of high pure skill astronauts has a very big effect on determining who makes it into the mostly-skill astronauts.


Reflection Thing:
After doing this task, I did expect luck to matter a bit, but not to this extent. Even a 5% weight has enough power to skew a success result (which explains why I'm
doing not so great in FILI-12), however, I noticed that the mostly-skill astronauts still have a high pure skill score to begin with, and they made it because their
luck score essentially pushed them to be better than then astronauts that had let's say a score of 99.9 but have an abysmal luck score. The difference in pure skill
for these high scoring astronauts is less than a whole number for determining the ones who will make it in, and with 18300 astronauts and 1000 trials, the results 
explain why the percent overlap (for 5% luck) is only around 15%, as the luck score can be so varied among the high scoring astronauts. There are obviously limitations
to this simulation model, such as literally having only 2 variables, but I think that this is a good simple simulation model on real world scenarios, such as in the
saying of "chance favors the prepared mind."
"""

