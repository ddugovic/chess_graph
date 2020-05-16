import kif_parser


def test_parse_individual_games():
    kif = "kifs/habu-fujii-2006.kif"
    lst, ratios, kick_depth = kif_parser.parse_individual_games(kif, 5, False, color = 'both', name = '')
    assert len(lst) == 1

test_parse_individual_games()
