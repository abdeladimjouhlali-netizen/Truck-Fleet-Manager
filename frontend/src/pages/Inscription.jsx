import React, { useState } from 'react';
import axios from 'axios';

export default function Inscription() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/auth/register', {
        email,
        password,
      });
      setMessage('Inscription réussie ! Connectez-vous.');
      setTimeout(() => window.location.href = '/', 1000);
    } catch (err) {
      setMessage("Erreur lors de l'inscription");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md w-80">
        <h2 className="text-2xl mb-4">Inscription</h2>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          className="w-full p-2 mb-2 border rounded"
          required
        />
        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="w-full p-2 mb-2 border rounded"
          required
        />
        <button className="w-full bg-green-500 text-white p-2 rounded">S'inscrire</button>
        <p className="mt-2 text-red-500">{message}</p>
        <a href="/" className="block mt-2 text-blue-600">Déjà inscrit ? Se connecter</a>
      </form>
    </div>
  );
}
