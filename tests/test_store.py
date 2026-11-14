import pytest
import tempfile
import os
from app.models import IdeaRequest
from app.store import IdeaStore

@pytest.fixture
def db_path():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        path = f.name
    yield path
    try:
        os.unlink(path)
    except OSError:
        pass

def test_fresh_store_is_empty(db_path):
    store = IdeaStore(db_path=db_path)
    assert len(store.find_all()) == 0

def test_adding_idea_stores_title_and_category(db_path):
    store = IdeaStore(db_path=db_path)
    request = IdeaRequest(title="Test idea", category="testing")
    result = store.add(request)
    assert result.title == "Test idea"
    assert result.category == "testing"
    assert any(idea.title == "Test idea" for idea in store.find_all())

def test_two_new_ideas_receive_different_ids(db_path):
    store = IdeaStore(db_path=db_path)
    request1 = IdeaRequest(title="First idea", category="clubs")
    request2 = IdeaRequest(title="Second idea", category="sports")
    result1 = store.add(request1)
    result2 = store.add(request2)
    assert result1.id != result2.id
    assert len(store.find_all()) == 2

def test_idea_persists_after_store_reopened(db_path):
    store1 = IdeaStore(db_path=db_path)
    request = IdeaRequest(title="Persistent idea", category="clubs")
    created = store1.add(request)

    store2 = IdeaStore(db_path=db_path)
    ideas = store2.find_all()
    assert any(
        idea.id == created.id and idea.title == created.title and idea.category == created.category
        for idea in ideas
    )
