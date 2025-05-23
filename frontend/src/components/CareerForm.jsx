import { useState } from 'react';
import { dispatchAgent } from '../services/api';

export default function CareerForm({ onResult }) {
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input) return;

    setLoading(true);
    try {
      const result = await dispatchAgent("LLM", input);
      onResult(result.response || result.output || result.answer);
    } catch (err) {
      onResult("Si è verificato un errore. Riprova.");
    }
    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-xl mx-auto p-4">
      <label className="block text-lg font-semibold text-gray-800">Descrivi il tuo profilo o obiettivo di carriera:</label>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        rows={5}
        placeholder="Esempio: Sono una sviluppatrice fullstack con 3 anni di esperienza in backend, voglio lavorare con AI e leadership..."
        className="w-full p-3 rounded border border-gray-300 shadow-sm focus:outline-none focus:ring focus:border-blue-300"
      />
      <button
        type="submit"
        disabled={loading}
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Elaborazione..." : "Ottieni suggerimenti"}
      </button>
    </form>
  );
}
