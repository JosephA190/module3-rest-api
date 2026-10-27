import { test } from "node:test";
import assert from "node:assert/strict";
import { isValidTitle } from "../src/validation.mjs";

test("a normal title is accepted", function() {
    assert.equal(isValidTitle("Start a coding club"), true);
});

test("an empty string is rejected", function() {
    assert.equal(isValidTitle(""), false);
});

test("a spaces-only string is rejected", function() {
    assert.equal(isValidTitle("   "), false);
});
