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
    assert ("User1", "FilmA") in example

def test_vectorize():
    assert [{"FilmA", "FilmB"}, {"FilmC", "FilmD"}] == similar.vectorize(example)

def test_overlap():
    assert 1 == similar.overlap({"FilmA", "FilmB"}, {"FilmA", "FilmB"})
    assert 0 == similar.overlap({"FilmA", "FilmB"}, {"FilmC", "FilmD"})

def test_most_similar():
    assert (1.0, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA", "FilmB"}, example)
    assert (1.0, {"FilmA", "FilmC"}) == similar.most_similar({"FilmA", "FilmC"}, example)
    assert (1.0, {"FilmA", "FilmD"}) == similar.most_similar({"FilmA", "FilmD"}, example)
    assert (1.0, {"FilmA", "FilmE"}) == similar.most_similar({"FilmA", "FilmE"}, example)
    assert (0.5, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA"}, example)
    assert (0.5, {"FilmA", "FilmB"}) == similar.most_similar({"FilmB"}, example)
    assert (0.5, {"FilmB", "FilmC"}) == similar.most_similar({"FilmB"}, example)
    assert (0.5, {"FilmC", "FilmD"}) == similar.most_similar({"FilmC"}, example)
