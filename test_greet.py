from greet import greet

def test_rec1():
    assert greet("Bob") == "Hello, Bob."

def test_rec2():
    assert greet(None) == "Hello, my friend."

def test_rec3():
    assert greet("JERRY") == "HELLO JERRY!"

def test_rec4():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test_rec5():
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test_rec6():
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_rec7():
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."

def test_rec8():
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."
