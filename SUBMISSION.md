# Phase 1 submission
Name: Joseph Alvarado
Course or section:INEW-2434-Advanced Web Programming
Chosen track: Python FastAPI

## My campus idea
A place where students can post and share ideas to improve campus life.

## Evidence log
Record method, URL, status, and response. Attach screenshots or paste terminal output.
1. Personalized GET /api/hello: GET http://localhost:8000/api/hello — 200 OK — {"message": "Hello from the Campus Idea Board! - Joseph"}
2. GET /api/ideas before creating: GET http://localhost:8000/api/ideas — 200 OK — returned the 2 seed ideas
3. Valid POST /api/ideas: POST http://localhost:8000/api/ideas — 201 Created — returned new idea with id, title, and category
4. GET /api/ideas after creating: GET http://localhost:8000/api/ideas — 200 OK — now showed 3 ideas including the one I added
5. Blank title POST (400) and unchanged list: POST with empty title — 400 Bad Request — {"message": "Invalid request"}, list still had same ideas
6. Malformed JSON POST (400): POST with bad JSON — 400 Bad Request — {"message": "Invalid request"}
7. Restart the server and GET /api/ideas (two seed ideas again): after restarting, GET returned only the 2 original seed ideas

## Reflection
1. What does a controller do? A controller handles incoming requests and sends back responses. It connects the route to the logic.
2. How is GET different from POST? GET is used to read data and POST is used to send or create data.
3. How do JSON title and category become Java data? The framework reads the JSON body and maps the values into a model object automatically.
4. Why does our added idea disappear after restarting? Because we are storing ideas in memory, not in a database. When the server restarts everything resets.
5. What would the React frontend need to know to use this API? It would need the base URL, the available endpoints, what JSON to send in the body, and what status codes to expect back.

## Debugging story
Symptom: My POST test was returning 422 instead of 400 for invalid input.
Hypothesis: FastAPI was using its default validation error handler instead of mine.
Change: I added a custom exception handler for RequestValidationError that returns 400 with {"message": "Invalid request"}.
Observed result: The test passed and returned 400 as expected.

## Assistance disclosure
I used the FastAPI documentation and course materials. I verified all tests myself by running pytest and checking the results.

## Automated test evidence
Command and summary: ran `pytest` in the terminal — all 5 tests passed
Two completed unit tests (names and assertions):
- test_fresh_store_contains_two_seed_ideas: checks that a new IdeaStore has 2 ideas
- test_two_new_ideas_receive_different_ids: checks that two added ideas get unique IDs that are not 1 or 2
Completed POST API test (name and assertions):
- test_valid_post_returns_created_idea: sends a POST request and checks that status is 201, id is not null, title and category match what was sent
Explain why unit tests differ from Postman requests: Unit tests run in code automatically and test individual functions. Postman sends real HTTP requests and lets you manually check the full response.
Confirm no required test is skipped or disabled: No tests are skipped or disabled. All 5 passed.