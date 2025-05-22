import { useState } from 'react';
import CareerForm from '../components/CareerForm';
import SuggestionsPanel from '../components/SuggestionsPanel';

export default function Home() {
  const [result, setResult] = useState('');

  return (
    <main className="min-h-screen bg-gray-100 py-10">
      <h1 className="text-3xl text-center font-bold text-blue-700 mb-8">AI Career Coach</h1>
      <CareerForm onResult={setResult} />
      <SuggestionsPanel result={result} />
    </main>
  );
}
