def multiply_by(lists):
    return lists * 0.9


def subtract_number_from(k):
    return k - 10


def capital(m):
    new_m = str(m)
    return new_m.upper()


def add_number_to(election_r):
    return election_r + 15




election_results = [12, 8, 19, 22, 35, 58, 56, 90, 89, 44, 25, 20, 88]
election_results_names = ['atiku', 'obi', 'tinubu']
winner_of_election = list(map(lambda v : v * 0.9, election_results))
winner = list(map(lambda v: v + 15, election_results))
winners_of = list(map(lambda v: v - 12, election_results))
winners_of_names = list(map(capital, election_results_names))
# winner_of_elections = list(map(lambda n: n * 2, election_results))
print(winner_of_election)
print(winners_of)
print(winner)

print(winners_of_names)
