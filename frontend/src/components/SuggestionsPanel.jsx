export default function SuggestionsPanel({ result }) {
  if (!result) return null;

  return (
    <div className="mt-6 bg-white border rounded-lg shadow p-4 max-w-xl mx-auto">
      <h2 className="text-xl font-bold text-gray-800 mb-2">Suggerimento AI</h2>
      <p className="text-gray-700 whitespace-pre-wrap">{result}</p>
    </div>
  );
}
