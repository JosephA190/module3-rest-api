# Reflection

## Request journey
When the page loads, React sends a GET request to the backend at /api/ideas. The backend receives the request, gets the list of ideas from the store, and sends them back as JSON. React then updates the state with the returned ideas and displays them on the page.

## Props versus state
State is data that lives inside a component and can change over time, like the list of ideas or the form input values. Props are values passed from a parent component to a child component, like passing the idea list from App to IdeaList or the submit handler from App to IdeaForm.

## Frontend versus backend validation
Frontend validation catches errors before sending a request, like checking if the title is empty or spaces only. This gives the user instant feedback without waiting for the server. Backend validation is a second check that makes sure invalid data never gets stored, even if someone sends a request directly through Postman or another tool.

## One bug I fixed
When I first ran the app the POST request was returning 422 instead of 400 for invalid input. I fixed it by adding a custom exception handler for RequestValidationError in main.py that returns 400 with a message of Invalid request.

## Refresh versus backend restart
When I refreshed the browser without restarting the backend, the idea I added was still there because the backend was still running and holding it in memory. When I restarted the backend, the added idea disappeared and only the two seed ideas came back because the memory resets on every restart.