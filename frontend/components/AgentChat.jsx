"use client";
import { useState } from "react";

export default function AgentTaskInput({ onTaskChange }) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    if (!input.trim()) return;
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/agent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input }),
      });
      const data = await res.json();
      setResult(data.output);
      onTaskChange();
    } catch {
      setResult("Error: Could not reach the agent.");
    }
    setLoading(false);
    setInput("");
  }

  return (
    <div className="max-w-lg mx-auto my-6 p-6 bg-slate-50 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">
        Add Task via AI Agent
      </h2>
      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          placeholder="Describe your task..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring focus:ring-blue-200"
        />
        <button
          type="submit"
          disabled={loading}
          className="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded-lg disabled:opacity-50 cursor-pointer"
        >
          {loading ? "Adding..." : "Add"}
        </button>
      </form>
      {result && <p className="mt-4 text-green-600 font-medium">{result}</p>}
    </div>
  );
}
