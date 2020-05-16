import new_parser


def test_parse_games():
    psn = "psns/games.nak_thomas.txt"
    lst, ratios, kick_depth = new_parser.parse_games(psn, 5, False, color = 'both', name = '')
    assert len(lst) == 1

test_parse_games()
