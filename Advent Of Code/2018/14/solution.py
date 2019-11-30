# %%
class recipes:
    def __init__(self):
        self.scoreboard = [3, 7]
        self.elf_1_pos = 0
        self.elf_2_pos = 1
        self.num_step = 0

    def __repr__(self):
        a = []

        for i in range(len(self.scoreboard)):
            if i == self.elf_1_pos:
                a.append(f'({self.scoreboard[i]})')
            elif i == self.elf_2_pos:
                a.append(f'[{self.scoreboard[i]}]')
            else:
                a.append(str(self.scoreboard[i]))
        return str(self.num_step) + ': ' + ' '.join(a)

    def step(self):
        self.num_step += 1
        elf_1_score = self.scoreboard[self.elf_1_pos]
        elf_2_score = self.scoreboard[self.elf_2_pos]

        a = elf_1_score + elf_2_score
        [self.scoreboard.append(int(d)) for d in str(a)]

        elf_1_steps = 1 + elf_1_score
        elf_2_steps = 1 + elf_2_score

        self.elf_1_pos = (self.elf_1_pos + elf_1_steps) % len(self.scoreboard)
        self.elf_2_pos = (self.elf_2_pos + elf_2_steps) % len(self.scoreboard)

    # part 1
    def extract_score(self, start):
        a = []
        for i in range(start, start + 10):
            a.append(self.scoreboard[i])
        return ''.join(map(str, a))

    # part 2
    def find_scores(self, s):
        if len(self.scoreboard) > len(s):
            a = self.scoreboard

            # test the last len(s) digits
            a = ''.join(map(str, a[len(a) - len(s):]))
            if a == s:
                return len(self.scoreboard) - len(s)

            # test the last len(s) digits except the last one
            # needed since sometimes we can two digits in step()
            a = self.scoreboard
            a = ''.join(map(str, a[len(a) - len(s) - 1:-1]))

            if a == s:
                return len(self.scoreboard) - len(s) - 1

        return 0


#####################
# part 1
input = 509671

# r = recipes()

# while len(r.scoreboard) <= (input + 10):
#     r.step()

# print(r.extract_score(input))

##################
# part 2
input = '509671'

r = recipes()

counter = 0
while True:
    counter += 1
    if (counter % 1000000) == 0:
        print(counter)
    r.step()

    num_re = r.find_scores(input)
    if num_re > 0:
        print(num_re)
        break
