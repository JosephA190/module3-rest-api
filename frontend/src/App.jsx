import { useState, useEffect } from "react";
import { getIdeas, createIdea } from "./api.js";
import IdeaList from "./components/IdeaList.jsx";
import IdeaForm from "./components/IdeaForm.jsx";

function App() {
    const [ideas, setIdeas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [loadError, setLoadError] = useState(null);

    function loadIdeas() {
        setLoading(true);
        setLoadError(null);
        getIdeas().then(function(data) {
            setIdeas(data);
            setLoading(false);
        }).catch(function() {
            setLoadError("Failed to load ideas.");
            setLoading(false);
        });
    }

    useEffect(function() {
        let cancelled = false;
        setLoading(true);
        setLoadError(null);
        getIdeas().then(function(data) {
            if (!cancelled) {
                setIdeas(data);
                setLoading(false);
            }
        }).catch(function() {
            if (!cancelled) {
                setLoadError("Failed to load ideas.");
                setLoading(false);
            }
        });
        return function() { cancelled = true; };
    }, []);

    function handleIdeaCreated(title, category) {
        return createIdea(title, category).then(function(newIdea) {
            setIdeas(function(prev) { return [...prev, newIdea]; });
        });
    }

    return (
        <div>
            <h1>Campus Idea Board</h1>
            <h2>Add an Idea</h2>
            <IdeaForm onIdeaCreated={handleIdeaCreated} />
            <h2>Ideas</h2>
            {loading && <p>Loading ideas…</p>}
            {loadError && (
                <div>
                    <p style={{ color: "red" }}>{loadError}</p>
                    <button onClick={loadIdeas}>Retry</button>
                </div>
            )}
            {!loading && !loadError && <IdeaList ideas={ideas} />}
        </div>
    );
}

export default App;
