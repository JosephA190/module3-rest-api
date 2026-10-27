const BASE_URL = "http://localhost:8080";

export function getIdeas() {
    return fetch(BASE_URL + "/api/ideas").then(function(res) {
        if (!res.ok) {
            throw new Error("Failed to load ideas");
        }
        return res.json();
    });
}

export function createIdea(title, category) {
    return fetch(BASE_URL + "/api/ideas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title, category: category })
    }).then(function(res) {
        if (!res.ok) {
            throw new Error("Failed to save idea");
        }
        return res.json();
    });
}
