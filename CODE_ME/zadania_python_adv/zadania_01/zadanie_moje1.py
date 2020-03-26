class Team:
    def __init__(self, name, points, gf, ga):
        self.name = name
        self.pts = points
        self.gf = gf  # goals for
        self.ga = ga  # goals against

    def __lt__(self, other):
        if self.pts < other.pts:
            return True
        elif self.pts == other.pts:
            if self.gf < other.gf:
                return True
        else:
            return False

    def __repr__(self):
        return f'{self.name}, {self.pts} punktów, różnica bramkowa {self.gf - self.ga}'


if __name__ == '__main__':
    # stan tabeli na 29.01.2020
    league_table = [
        Team('Tottenham Hotspur', points=34, gf=38, ga=32),
        Team('Manchester City', points=51, gf=65, ga=27),
        Team('Manchester United', points=34, gf=36, ga=29),
        Team('Chelsea', points=40, gf=41, ga=32),
        Team('Leicester', points=48, gf=52, ga=24),
        Team('Liverpool', points=70, gf=56, ga=15),
    ]

    league_table.sort()
    league_table.reverse()

    print(league_table)
    print()

    print("{:<25} {:^10} {:^10} {:^10}".format('Team', 'Points', 'Goals For', 'Goals Against'))
    for t in league_table:
        print("{:<25} {:^10} {:^10} {:^10}".format(t.name, t.pts, t.gf, t.ga))
