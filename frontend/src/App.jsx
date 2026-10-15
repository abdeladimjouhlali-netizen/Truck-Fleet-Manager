import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Connexion from './pages/Connexion';
import Inscription from './pages/Inscription';
import Profil from './pages/Profil';
import Camions from './pages/Camions';
import Chauffeurs from './pages/Chauffeurs';
import Itineraires from './pages/Itineraires';
import Livraisons from './pages/Livraisons';
import Maintenance from './pages/Maintenance';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="max-w-5xl mx-auto py-6">
        <Routes>
          <Route path="/" element={<Connexion />} />
          <Route path="/inscription" element={<Inscription />} />
          <Route path="/profil" element={<Profil />} />
          <Route path="/camions" element={<Camions />} />
          <Route path="/chauffeurs" element={<Chauffeurs />} />
          <Route path="/itineraires" element={<Itineraires />} />
          <Route path="/livraisons" element={<Livraisons />} />
          <Route path="/maintenance" element={<Maintenance />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
