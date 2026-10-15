import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Camions() {
  const [camions, setCamions] = useState([]);
  const [marque, setMarque] = useState('');
  const [modele, setModele] = useState('');
  const [capacite, setCapacite] = useState('');
  const [message, setMessage] = useState('');

  const token = localStorage.getItem('token');
  const fetchCamions = async () => {
    try {
      const res = await axios.get('http://localhost:8000/camions/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setCamions(res.data);
    } catch (err) {
      setMessage('Erreur lors du chargement des camions');
    }
  };

  useEffect(() => {
    fetchCamions();
  }, []);

  const ajouterCamion = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/camions/', {
        marque,
        modele,
        capacite: parseFloat(capacite),
      }, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setMessage('Camion ajouté !');
      setMarque(''); setModele(''); setCapacite('');
      fetchCamions();
    } catch (err) {
      setMessage("Erreur lors de l'ajout du camion");
    }
  };

  const supprimerCamion = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/camions/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchCamions();
    } catch {
      setMessage("Erreur lors de la suppression");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-2xl mx-auto bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl mb-4">Gestion des Camions</h2>
        <form onSubmit={ajouterCamion} className="flex space-x-2 mb-4">
          <input type="text" placeholder="Marque" value={marque} onChange={e => setMarque(e.target.value)} className="p-2 border rounded w-1/4" required />
          <input type="text" placeholder="Modèle" value={modele} onChange={e => setModele(e.target.value)} className="p-2 border rounded w-1/4" required />
          <input type="number" step="0.1" placeholder="Capacité" value={capacite} onChange={e => setCapacite(e.target.value)} className="p-2 border rounded w-1/4" required />
          <button className="bg-green-500 text-white p-2 rounded">Ajouter</button>
        </form>
        <p className="mb-4 text-red-500">{message}</p>
        <table className="min-w-full bg-white rounded shadow">
          <thead>
            <tr>
              <th className="px-4 py-2">Marque</th>
              <th className="px-4 py-2">Modèle</th>
              <th className="px-4 py-2">Capacité</th>
              <th className="px-4 py-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            {camions.map(camion => (
              <tr key={camion.id}>
                <td className="border px-4 py-2">{camion.marque}</td>
                <td className="border px-4 py-2">{camion.modele}</td>
                <td className="border px-4 py-2">{camion.capacite}</td>
                <td className="border px-4 py-2">
                  <button onClick={() => supprimerCamion(camion.id)} className="bg-red-500 text-white px-2 py-1 rounded">Supprimer</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <table className="w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2">Marque</th>
              <th className="border p-2">Modèle</th>
              <th className="border p-2">Capacité</th>
              <th className="border p-2">État</th>
            </tr>
          </thead>
          <tbody>
            {camions.map(camion => (
              <tr key={camion.id}>
                <td className="border p-2">{camion.marque}</td>
                <td className="border p-2">{camion.modele}</td>
                <td className="border p-2">{camion.capacite}</td>
                <td className="border p-2">{camion.etat}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <a href="/profil" className="block mt-4 text-blue-600">Retour au profil</a>
      </div>
    </div>
  );
}
