import pytest
from app.models import IdeaRequest
from app.store import IdeaStore

def test_fresh_store_contains_two_seed_ideas():
    store = IdeaStore()
    assert len(store.find_all()) == 2

def test_adding_idea_stores_title_and_category():
    store = IdeaStore()
    request = IdeaRequest(title="Test idea", category="testing")
    result = store.add(request)
    assert result.title == "Test idea"
    assert result.category == "testing"
    assert any(idea.title == "Test idea" for idea in store.find_all())

def test_two_new_ideas_receive_different_ids():
    store = IdeaStore()
    request1 = IdeaRequest(title="First idea", category="clubs")
    request2 = IdeaRequest(title="Second idea", category="sports")
    result1 = store.add(request1)
    result2 = store.add(request2)
    assert result1.id != result2.id
    assert result1.id not in [1, 2]
    assert result2.id not in [1, 2]
    assert len(store.find_all()) == 4
