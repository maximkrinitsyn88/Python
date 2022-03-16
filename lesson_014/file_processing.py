from bowling import get_score


def record_of_results(filename, filename_result):
    players = {}
    log_players = []
    with open(file=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            if "winner" not in line:
                line = line.split()
                score = get_score(line[1])
                scores = {line[0]: score}
                players.update(scores)
                player = ('{name:8} {frames:22} {score} \n'.format(name=line[0], frames=line[1], score=score))
                log_players.append(player)

    with open(filename_result, 'w', encoding='utf-8') as file_result:
        winner = max(players, key=players.get)
        winner = 'winner is {winner}'.format(winner=winner)
        for player in log_players:
            file_result.write(player)
        file_result.write(winner)

