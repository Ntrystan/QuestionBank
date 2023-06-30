import uuid


class MChoice:
    def __init__(self, qtext: str, correct: str, choices: list[str]):
        self.id = uuid.uuid1()
        self.dline = f".. mchoice:: {self.id}"
        self.question = qtext.strip().split("\n")
        self.correct = correct
        self.choices = choices
        self.options = {}
        self.indent = 4

    def __str__(self):
        rlist = [self.dline]
        ind = " " * self.indent
        for key, val in self.options.items():
            key = f":{key}:"
            rlist.append(f"{ind}{key} {val}")
        rlist.append("")
        rlist.extend(f"{ind}{line}" for line in self.question)
        rlist.append("")
        for idx, choice in enumerate(self.choices):
            rlist.extend((f"{ind}- {choice}", ""))
            if idx == self.correct:
                rlist.append(f"{ind}  + correct")
            else:
                rlist.append(f"{ind}  - incorrect")
            rlist.append("")
        return "\n".join(rlist)
