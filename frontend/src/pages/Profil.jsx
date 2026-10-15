import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Profil() {
  const [profil, setProfil] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchProfil = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get('http://localhost:8000/auth/users/me', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setProfil(res.data);
      } catch (err) {
        setMessage('Erreur lors de la récupération du profil');
      }
    };
    fetchProfil();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded shadow-md w-80">
        <h2 className="text-2xl mb-4">Profil utilisateur</h2>
        {profil ? (
          <>
            <p>Email : {profil.email}</p>
            <p>ID : {profil.id}</p>
            <a href="/camions" className="block mt-4 text-blue-600">Gérer les camions</a>
          </>
        ) : (
          <p>{message || 'Chargement...'}</p>
        )}
        <a href="/" className="block mt-4 text-red-500">Se déconnecter</a>
      </div>
    </div>
  );
}
