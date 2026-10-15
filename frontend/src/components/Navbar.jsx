import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-blue-700 text-white px-4 py-3 shadow flex items-center justify-between">
      <div className="font-bold text-xl">Gestion Camions</div>
      <div className="flex gap-4">
        <Link to="/camions" className="hover:underline">Camions</Link>
        <Link to="/chauffeurs" className="hover:underline">Chauffeurs</Link>
        <Link to="/itineraires" className="hover:underline">Itinéraires</Link>
        <Link to="/livraisons" className="hover:underline">Livraisons</Link>
        <Link to="/maintenance" className="hover:underline">Maintenance</Link>
        <Link to="/profil" className="hover:underline">Profil</Link>
        <Link to="/" className="hover:underline">Déconnexion</Link>
      </div>
    </nav>
  );
}
