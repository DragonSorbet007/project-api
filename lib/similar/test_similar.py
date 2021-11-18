import similar 

example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD"),
    ("User1", "FilmE")
]


def test_sampledataset():
    assert len(example) == 5

def test_sampledataset2():
    assert ("User1", "FilmA") in example