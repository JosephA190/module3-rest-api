import { useState } from "react";
import { isValidTitle } from "../validation.mjs";

function IdeaForm({ onIdeaCreated }) {
    const [title, setTitle] = useState("");
    const [category, setCategory] = useState("");
    const [saving, setSaving] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);
    const [validationError, setValidationError] = useState(null);

    function handleSubmit(event) {
        event.preventDefault();
        setValidationError(null);
        setError(null);
        setSuccess(false);

        if (!isValidTitle(title)) {
            setValidationError("Title cannot be empty or spaces only.");
            return;
        }

        setSaving(true);
        onIdeaCreated(title.trim(), category).then(function() {
            setTitle("");
            setCategory("");
            setSuccess(true);
            setSaving(false);
        }).catch(function() {
            setError("Failed to save idea. Please try again.");
            setSaving(false);
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="title">Title</label>
                <input
                    id="title"
                    type="text"
                    value={title}
                    onChange={function(e) { setTitle(e.target.value); }}
                />
            </div>
            <div>
                <label htmlFor="category">Category</label>
                <input
                    id="category"
                    type="text"
                    value={category}
                    onChange={function(e) { setCategory(e.target.value); }}
                />
            </div>
            {validationError && <p style={{ color: "red" }}>{validationError}</p>}
            {error && <p style={{ color: "red" }}>{error}</p>}
            {success && <p style={{ color: "green" }}>Idea added successfully!</p>}
            <button type="submit" disabled={saving}>
                {saving ? "Saving..." : "Add Idea"}
            </button>
        </form>
    );
}

export default IdeaForm;
